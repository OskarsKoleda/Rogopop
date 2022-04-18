<template>
  <div class="d-flex justify-content-between">
    <nav aria-label="Page navigation example">
      <ul class="pagination mt-2">
        <li class="page-item">
          <router-link
            class="btn btn-small btn-secondary"
            :class="{ disabled: !previousPageNumber }"
            :to="firstPageLink"
            >First</router-link
          >
        </li>
        <li class="page-item" v-show="previousPageNumber">
          <router-link
            class="btn btn-small btn-secondary ms-2"
            :to="previousPageLink"
          >
            {{ previousPageNumber }}
          </router-link>
        </li>
        <li class="page-item">
          <button class="btn btn-small btn-secondary ms-2">
            {{ currentPageNumber }}
          </button>
        </li>
        <li class="page-item" v-show="nextPageNumber">
          <router-link
            class="btn btn-small btn-secondary ms-2"
            :to="nextPageLink"
          >
            {{ nextPageNumber }}
          </router-link>
        </li>
        <li class="page-item">
          <router-link
            class="btn btn-small btn-secondary ms-2"
            :class="{ disabled: currentPageNumber === lastPageNumber }"
            :to="lastPageLink"
            >Last</router-link
          >
        </li>
      </ul>
    </nav>
    <span>Page {{ currentPageNumber }} of {{ lastPageNumber }}</span>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  data() {
    return {
      error: null,
    };
  },
  computed: {
    ...mapGetters('concerts', [
      'previousPageNumber',
      'nextPageNumber',
      'eventsCount',
      'eventsPerPage',
      'currentPageNumber',
      'currentSearchQuery',
      'currentOrdering',
    ]),
    lastPageNumber() {
      let quotient = Math.floor(this.eventsCount / this.eventsPerPage);
      let remainder = this.eventsCount % this.eventsPerPage;
      return remainder === 0 ? quotient : quotient + 1;
    },
    firstPageLink() {
      return {
        name: 'concerts',
        param: { page: 1 },
        query: {
          search: this.currentSearchQuery,
          ordering: this.currentOrdering || undefined,
        },
      };
    },
    previousPageLink() {
      return {
        name: 'concerts',
        param: { page: this.previousPageNumber },
        query: {
          search: this.currentSearchQuery,
          ordering: this.currentOrdering || undefined,
        },
      };
    },
    nextPageLink() {
      return {
        name: 'concerts',
        params: { page: this.nextPageNumber },
        query: {
          search: this.currentSearchQuery,
          ordering: this.currentOrdering || undefined,
        },
      };
    },
    lastPageLink() {
      return {
        name: 'concerts',
        params: { page: this.lastPageNumber },
        query: {
          search: this.currentSearchQuery,
          ordering: this.currentOrdering || undefined,
        },
      };
    },
  },
};
</script>

<style scoped>
.disabled {
  opacity: 0.5;
  pointer-events: none;
}

a {
  outline: none;
}
input[type='button']::-moz-focus-inner {
  border: 0;
}
</style>
