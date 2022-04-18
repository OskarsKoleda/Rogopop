<template>
  <div class="container">
    <section class="d-flex justify-content-between align-items-center">
      <h1 class="mt-3 mb-3"><b>Concert List</b></h1>

      <input
        v-on:input="searchHandler"
        class="form-control"
        type="search"
        placeholder="Search event..."
      />
    </section>
    <div v-if="eventsAreLoading">
      <base-spinner></base-spinner>
    </div>
    <div v-else-if="!eventsAreLoading && eventsCount === 0">
      <h2 class="mb-3">Nothing was found. Try again.</h2>
    </div>
    <div v-else>
      <table class="table table-striped table-hover table-light">
        <thead>
          <tr>
            <th scope="col">
              Event<i
                @click="toggleOrdering('title')"
                class="fas fa-sort ms-2"
              ></i>
            </th>
            <th scope="col">City</th>
            <th scope="col">Date</th>
            <th scope="col">Price</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="event in events" :key="event.slug">
            <td>
              <router-link
                class="link-to-details"
                :to="{ name: 'concert-details', params: { slug: event.slug } }"
              >
                {{ event.title }}
              </router-link>
            </td>
            <td>{{ event.city }}</td>
            <td>{{ event.date }}</td>
            <td>{{ event.ticket_price }} &euro;</td>
            <td class="d-flex justify-content-end">
              <button
                @click="toggleVisit(event.user_has_participated, event.slug)"
                class="btn btn-sm ms-2 btn-visit"
                :class="{
                  'btn-success': event.user_has_participated,
                  'btn-outline-success': !event.user_has_participated,
                }"
              >
                {{ event.user_has_participated ? '&#10004;' : '&#10007;' }}
              </button>

              <router-link
                v-if="isStaff === 'true' || requestUser === event.created_by"
                class="btn btn-sm btn-warning ms-2"
                :to="{ name: 'concert-editor', params: { slug: event.slug } }"
                >Edit</router-link
              >
              <button
                v-if="isStaff === 'true' || requestUser === event.created_by"
                class="btn btn-sm btn-danger ms-2"
                @click="showDialog(event.title, event.slug)"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="">
        <concerts-pagination v-show="!eventsAreLoading"></concerts-pagination>
        <router-link
          v-show="!eventsAreLoading"
          :to="{ name: 'concert-creator' }"
          class="btn btn-lg btn-warning"
        >
          <b>Add New Concert</b>
        </router-link>
      </div>
    </div>

    <base-modal @close="hideDialog" v-if="dialogIsVisible">
      <template v-slot:header><b>DELETION</b></template>
      <template v-slot:body
        >Are you sure you want to delete this event: <br />
        <b>{{ eventToDelete }}</b
        >?</template
      >
      <template v-slot:footer>
        <div class="d-flex justify-content-end">
          <button class="btn btn-info btn-sm" @click="hideDialog">
            I've changed my mind!
          </button>
          <button class="btn btn-danger btn-sm ms-2" @click="removeEvent">
            Delete
          </button>
        </div>
      </template>
    </base-modal>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import debounce from 'lodash.debounce';
import ConcertsPagination from './ConcertsPagination.vue';
export default {
  components: { ConcertsPagination },
  data() {
    return {
      error: null,
      eventsAreLoading: false,
      dialogIsVisible: false,
      eventToDelete: '',
      eventToDeleteSlug: '',
      pageToGo: '',
      searchQuery: '',
      orderColumn: '',
      ascending: false,
    };
  },
  computed: {
    ...mapGetters('concerts', ['eventsCount']),
    events() {
      return this.$store.getters['concerts/events'];
    },
    isStaff() {
      return window.localStorage.getItem('is_staff');
    },
    requestUser() {
      return window.localStorage.getItem('username');
    },
  },
  created() {
    this.debounceHandler = debounce((searchQuery) => {
      this.$router.push({
        name: 'concerts',
        params: { page: '1' },
        query: { search: searchQuery },
      });
    }, 1000);
  },
  watch: {
    pageToGo() {
      this.getUserConcerts(this.pageToGo, this.searchQuery, this.orderColumn);
    },
    searchQuery() {
      this.getUserConcerts(this.pageToGo, this.searchQuery, this.orderColumn);
    },
    orderColumn() {
      this.getUserConcerts(this.pageToGo, this.searchQuery, this.orderColumn);
    },
  },
  methods: {
    searchHandler(event) {
      let val = event.target.value;
      this.$store.dispatch('concerts/storeOrdering', null);
      this.debounceHandler(val, this.orderColumn);
    },
    async removeEvent() {
      try {
        await this.$store.dispatch(
          'concerts/removeEvent',
          this.eventToDeleteSlug
        );
      } catch (error) {
        this.error =
          error.message || `Could not delete event: ${this.eventToDelete}`;
      }
      this.hideDialog();
      this.getUserConcerts(1);
    },
    showDialog(title, slug) {
      this.dialogIsVisible = true;
      this.eventToDelete = title;
      this.eventToDeleteSlug = slug;
    },
    hideDialog() {
      this.dialogIsVisible = false;
      this.eventToDelete = null;
      this.eventToDeleteSlug = null;
    },
    toggleOrdering(columnName) {
      let order = this.ascending ? columnName : '-' + columnName;
      this.$store.dispatch('concerts/storeOrdering', order);
      this.ascending = !this.ascending;
      this.$router.push({
        name: 'concerts',
        params: { page: this.pageToGo || 1 },
        query: {
          search: this.searchQuery || undefined,
          ordering: order,
        },
      });
    },
    async toggleVisit(userParticipated, eventSlug) {
      try {
        if (!userParticipated) {
          await this.$store.dispatch('concerts/joinEvent', eventSlug);
        } else {
          await this.$store.dispatch('concerts/unjoinEvent', eventSlug);
        }
      } catch (error) {
        this.error =
          error.message ||
          (userParticipated
            ? 'Could not unjoin event'
            : 'Could not join event');
      }
    },
    async getUserConcerts(page, searchString, ordering) {
      const payload = {};
      this.eventsAreLoading = true;
      try {
        if (page) {
          payload['page'] = page;
        }
        if (searchString) {
          payload['searchString'] = searchString;
        }
        if (ordering) {
          payload['ordering'] = ordering;
        }
        await this.$store.dispatch('concerts/fetchEvents', payload);
      } catch (error) {
        this.error = error.message || 'Could not retrieve events';
      }
      this.eventsAreLoading = false;
    },
  },
  async beforeRouteEnter(to, from, next) {
    return await next((vm) => {
      vm.pageToGo = to.params.page || 1;
      vm.searchQuery = to.query.search || '';
      vm.orderColumn = to.query.ordering || '';
    });
  },
  async beforeRouteUpdate(to, from, next) {
    this.pageToGo = to.params.page;
    this.searchQuery = to.query.search || '';
    this.orderColumn = to.query.ordering || '';
    next();
  },
  beforeUnmount() {
    this.debounceHandler.cancel();
  },
};
</script>

<style scoped>
.container {
  width: 80%;
}
.btn-visit {
  min-width: 30px;
}

.form-control {
  width: 30%;
  height: 20%;
}

.link-to-details {
  text-decoration: none;
  color: inherit;
  font-weight: 600;
}

th > i {
  cursor: pointer;
}
</style>
