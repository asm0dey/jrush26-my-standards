<template>
  <footer v-if="$slidev.nav.currentPage > 1" class="deck-footer">
    @asm0dey <span>|</span> #JRush <span>|</span> #AIcoding
  </footer>
</template>

<style scoped>
.deck-footer {
  position: absolute;
  left: 1.6rem;
  bottom: 0.9rem;
  font-size: 0.72rem;
  letter-spacing: 0.04em;
  opacity: 0.6;
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
}
.deck-footer span { opacity: 0.5; margin: 0 0.3rem; }
</style>
