<template>
  <div class="container mt-5">
    <div class="d-flex justify-content-center">
      <div class="card">
        <h3 class="card-header">Your Profile</h3>
        <div class="card-body">
          <p class="card-text">
            This is some text within a card body.
          </p>
          <div v-if="profileIsLoading">
            <base-spinner></base-spinner>
          </div>
          <ul class="list-group list-group-flush" v-else>
            <li class="list-group-item">
              First Name: <b>{{ this.firstName }}</b>
            </li>
            <li class="list-group-item">
              Last Name: <b>{{ this.lastName }}</b>
            </li>
            <li class="list-group-item">
              Events Visited: <b>{{ this.eventCount }}</b>
            </li>
            <li class="list-group-item">
              Total Money Spent: <b>{{ this.moneySpent }} &euro;</b>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      error: null,
      profileIsLoading: false,
    };
  },
  computed: {
    firstName() {
      return this.$store.getters['profile/getFirstName'];
    },
    lastName() {
      return this.$store.getters['profile/getLastName'];
    },
    eventCount() {
      return this.$store.getters['profile/getNumberOfEvents'];
    },
    moneySpent() {
      return this.$store.getters['profile/getTotalMoneySpent'];
    },
  },
  methods: {
    async getProfileData() {
      this.profileIsLoading = true;
      try {
        await this.$store.dispatch('profile/getProfile');
      } catch (error) {
        this.error = error.message || 'Something went wrong!';
      }
      this.profileIsLoading = false;
    },
  },
  created() {
    this.getProfileData();
  },
};
</script>

<style scoped>
.card {
  width: 60%;
}
</style>
