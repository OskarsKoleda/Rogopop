<template>
  <div class="container d-flex justify-content-center">
    <div class="poster">
      <img :src="poster" alt="...event poster..." />
    </div>
    <div class="card d-flex align-items-center justify-content-center">
      <p class="title">{{ title }}</p>
      <hr />
      <p>City: {{ city }}</p>
      <hr />
      <p>Price: {{ price }} &euro;</p>
      <hr />
      <p>Date: {{ date }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['slug'],
  data() {
    return {
      error: null,
      title: '',
      city: '',
      price: '',
      comments: '',
      date: '',
      poster: '',
    };
  },
  async created() {
    try {
      const response = await this.$store.dispatch(
        'concerts/fetchOneEvent',
        this.slug
      );
      this.title = response.title;
      this.city = response.city;
      this.price = response.ticket_price;
      this.comments = response.comments;
      this.date = response.date;
      this.poster = response.poster;
    } catch (error) {
      this.error = error.message || "Couldn't fetch event!";
    }
  },
};
</script>

<style scoped>
.title {
  font-size: 2rem;
}
hr {
  width: 80%;
}
p {
  margin: 0 2rem;
}
.container {
  margin-top: 3.5rem;
  font-size: 1.5rem;
}
.poster {
  min-width: 450px;
  max-width: 550px;
}
img {
  width: 95%;
}

.card {
  border: none;
  min-width: 300px;
  border-radius: 0%;
  background-color: #a63d40;
  color: azure;
}
</style>
