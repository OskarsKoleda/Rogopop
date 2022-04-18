<template>
  <div class="container">
    <h1 class="mt-3">{{ create ? 'Add New Concert' : 'Update Concert' }}</h1>
    <form @submit.prevent class="form-control g-3">
      <div class="mb-3">
        <label for="title" class="form-label">Event Title</label>
        <input class="form-control" id="title" v-model="title" />
      </div>
      <div class="mb-3">
        <label for="city" class="form-label">City</label>
        <input class="form-control" id="city" v-model="city" />
      </div>
      <div class="mb-3">
        <label for="price" class="form-label">Ticket Price</label>
        <input type="number" class="form-control" id="price" v-model="price" />
      </div>
      <div class="mb-3">
        <label class="form-label">Bands Participated</label>
        <multiselect-menu
          @dropdown-change="storeBands"
          :allOptions="this.bandsList"
          :currentOptions="this.bandsParticipated"
        ></multiselect-menu>
      </div>

      <div class="mb-3">
        <label for="date" class="form-label">Date</label>
        <input type="date" class="form-control" id="date" v-model="date" />
      </div>
      <div class="mb-3">
        <div class="d-flex justify-content-between">
          <label for="poster" class="form-label">Poster</label>
          <p v-if="this.oldPoster">
            Currently selected poster:
            <a :href="this.oldPoster">{{ this.imageName }}</a>
          </p>
        </div>

        <input
          accept="image/*"
          type="file"
          class="form-control"
          id="date"
          @change="previewFile"
        />
      </div>
      <div class="mb-3">
        <label for="comment" class="form-label">Comment</label>
        <textarea
          class="form-control"
          id="comment"
          rows="3"
          v-model="comment"
        ></textarea>
      </div>
      <button @click="eventButtonAction" class="btn btn-primary" type="submit">
        {{ create ? 'Add' : 'Update' }}
      </button>
    </form>
  </div>
</template>

<script>
import { axios } from '../../../common/api.service';
import MultiselectMenu from '../../../components/ui/BaseMultiselect.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'ConcertEditor',
  components: {
    MultiselectMenu,
  },
  data() {
    return {
      eventSlug: '',
      title: 'Rogo-test',
      comment: 'this is just a test comment',
      price: 69,
      city: 'Edmonton',
      date: '2022-02-13',
      create: false,
      error: '',
      newPoster: '',
      oldPoster: '',
      updatingEvent: false,
      imageName: '',
      bandsParticipated: [],
    };
  },
  created() {
    try {
      this.$store.dispatch('bands/fetchBands');
    } catch (error) {
      this.error = error.message || 'Could not fetch Bands';
    }
  },
  computed: {
    ...mapGetters('bands', ['bandsList']),
    eventButtonAction() {
      return this.create ? this.addEvent : this.updateEvent;
    },
  },
  methods: {
    previewFile(event) {
      this.newPoster = event.target.files[0];
    },
    storeBands(bands) {
      this.bandsParticipated = bands;
    },
    getPayload() {
      let formData = new FormData();
      formData.append('title', this.title);
      formData.append('ticket_price', this.price);
      formData.append('date', this.date);
      formData.append('comment', this.comment);
      formData.append('city', this.city);
      formData.append('bandsParticipated', this.bandsParticipated);
      if (this.newPoster) {
        formData.append('poster', this.newPoster);
      }
      return formData;
    },
    async addEvent() {
      let payload = this.getPayload();
      try {
        await this.$store.dispatch('concerts/addEvent', payload);
      } catch (error) {
        this.error = error.message || 'Could not add event';
      }
      this.$router.push({
        name: 'concerts',
      });
    },
    async updateEvent() {
      this.updatingEvent = true;
      let payload = this.getPayload();
      try {
        await this.$store.dispatch('concerts/updateEvent', {
          slug: this.eventSlug,
          body: payload,
        });
      } catch (error) {
        this.error = error.message || 'Could not update event';
      }
      this.updatingEvent = true;
      this.$router.push({
        name: 'concerts',
      });
    },
  },
  async beforeRouteEnter(to, from, next) {
    if (to.fullPath === '/concert/add') {
      return next((vm) => {
        vm.create = true;
      });
    } else {
      const endpoint = `/api/v1/concert/${to.params.slug}/`;
      try {
        const response = await axios.get(endpoint);
        return next((vm) => {
          vm.title = response.data.title;
          vm.comment = response.data.comment;
          vm.price = response.data.ticket_price;
          vm.city = response.data.city;
          vm.date = response.data.date;
          vm.eventSlug = response.data.slug;
          vm.oldPoster = response.data.poster;
          vm.imageName = response.data.image_name;
          vm.bandsParticipated = response.data.bands_participated.map(
            (band) => band.name
          );
        });
      } catch (error) {
        console.log(error);
      }
    }
  },
};
</script>

<style scoped>
.container {
  width: 60%;
  background-color: rgb(235, 252, 215);
  padding: 0 1rem 1rem 1rem;
}
</style>
