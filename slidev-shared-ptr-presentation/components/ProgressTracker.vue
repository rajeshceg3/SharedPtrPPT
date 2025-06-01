<template>
  <div class="progress-tracker">
    Slide {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
  </div>
</template>

<style scoped>
.progress-tracker {
  position: fixed;
  bottom: 10px;
  right: 15px;
  font-size: 0.8em;
  color: #888;
  background-color: rgba(0,0,0,0.1); /* Optional: for better visibility */
  padding: 3px 8px;
  border-radius: 3px;
}
</style>
