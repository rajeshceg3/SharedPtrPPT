<template>
  <div class="visual-ref-counter">
    <p class="label">Reference Count:</p>
    <p class="count">{{ count }}</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  count: {
    type: Number,
    required: true,
    default: 0
  }
})
</script>

<style scoped>
.visual-ref-counter {
  background-color: rgba(128, 128, 128, 0.1);
  border: 1px solid rgba(128, 128, 128, 0.3);
  padding: 15px;
  border-radius: 8px;
  text-align: center;
  margin: 10px auto; /* Center block if it's not full width */
  width: fit-content; /* Adjust width to content */
}
.label {
  font-size: 0.9em;
  color: #aaa;
  margin-bottom: 5px;
}
.count {
  font-size: 2.5em;
  font-weight: bold;
  color: #30c8c8; /* Using a color similar to cyan accents in the presentation */
}
</style>
