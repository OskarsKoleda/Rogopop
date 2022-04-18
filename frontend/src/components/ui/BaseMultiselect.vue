<template>
  <div>
    <multiselect
      v-model="value"
      :options="allAvailableOptions"
      searchable
      placeholder="Select..."
      noResultsText="Nothing was found"
      mode="tags"
      @close="onSelectClose"
    >
    </multiselect>
  </div>
</template>

<script>
import Multiselect from '@vueform/multiselect';
export default {
  props: ['allOptions', 'currentOptions'],
  emits: ['dropdown-change'],
  components: {
    Multiselect,
  },
  data() {
    return {
      value: null,
    };
  },
  computed: {
    allAvailableOptions() {
      return this.allOptions;
    },
    selectedOptions() {
      return this.currentOptions;
    },
  },
  watch: {
    selectedOptions() {
      this.value = this.selectedOptions;
    },
  },
  methods: {
    onSelectClose() {
      this.$emit('dropdown-change', this.value);
    },
  },
};
</script>

<style src="@vueform/multiselect/themes/default.css"></style>
