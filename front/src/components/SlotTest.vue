<template>
  <div>
    <slot name="header">
      HEADER
    </slot>
  </div>
  <div>
    <slot name="footer">
      footer
    </slot>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
 
</script>

<style scoped>

</style>