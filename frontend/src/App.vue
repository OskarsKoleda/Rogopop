<template>
  <div class="">
    <the-header></the-header>
    <router-view />
  </div>
</template>

<script>
import TheHeader from './components/layout/TheHeader.vue';

export default {
  components: { TheHeader },
  async created() {
    try {
      await this.$store.dispatch('setUser');
    } catch (error) {
      this.error = error.message || 'Could not retrieve user info';
    }
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap');

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  background-color: #b5cc91;
  color: #151515;
  font-family: 'Roboto Slab', serif;
}
</style>
