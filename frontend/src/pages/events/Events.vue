<template>
  <div class="container">
    <div class="tab-bar d-flex justify-content-center align-items-center">
      <router-link class="tab" :to="{ name: 'concerts' }">CONCERTS</router-link>
      <router-link class="tab" :to="{ name: 'bands' }">BANDS</router-link>
    </div>
    <hr />
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
/* a:first-of-type { */
/* margin-right: 1.5rem;
} */

hr {
  margin: 0;
}
.tab-bar {
  height: 3.6rem;
}
a {
  padding: 0.7rem;
  text-decoration: none;
  font-size: 1.5rem;
  background-color: #9ab86b;
  border: 2px solid transparent;
}
a:active,
a:hover {
  background-color: #89b444;
}
a.router-link-active {
  background-color: #89b444;
  border-left: 2px solid black;
  border-right: 2px solid black;
}

a:visited {
  color: inherit;
}

a:not(.router-link-exact-active):hover {
  background-color: #77b317;
}
</style>
