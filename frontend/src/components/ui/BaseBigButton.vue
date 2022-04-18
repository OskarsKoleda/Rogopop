<template>
  <button v-if="!link" :class="mode">
    <slot></slot>
  </button>
  <router-link v-else :to="to" :class="mode">
    <slot></slot>
  </router-link>
</template>
<script>
export default {
  props: {
    mode: {
      type: String,
      required: false,
      default: null,
    },
    link: {
      type: Boolean,
      required: false,
      default: false,
    },
    to: {
      type: String,
      required: false,
      default: '/',
    },
  },
};
</script>

<style scoped>
button,
a {
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  font: inherit;
  background-color: #37cc86;
  border: 1px solid #16a060;
  color: white;
  cursor: pointer;
  margin-right: 0.5rem;
  margin-left: 0.5rem;
  display: inline-block;
}

a:hover,
a:active,
button:hover,
button:active {
  background-color: #0dad63;
  border-color: #c7ddd3;
}


</style>
