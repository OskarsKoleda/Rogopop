<template>
  <div>
    <div class="backdrop" @click="$emit('close')"></div>
    <div class="card">
        <div class="card-header">
          <slot name="header"></slot>
        </div>
        <div class="card-body">
          <slot name="body"></slot>
        </div>
        <div class="card-footer">
          <slot name="footer"></slot>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ['close'],
};
</script>

<style scoped>
.backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: 10;
  background-color: rgba(0, 0, 0, 0.75);
}

.card {
  position: fixed;
  top: 30vh;
  width: 30rem;
  left: calc(50% - 15rem);
  margin: 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  /* border-radius: 12px; */
  /* padding: 1rem; */
  background-color: white;
  z-index: 100;
  border: none;
}
</style>
