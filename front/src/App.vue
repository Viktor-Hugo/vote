<template>
  <h1>보유 포인트 : {{ useAccountStore().balance }} </h1>
  <RouterView />
</template>

<script setup>
  import { RouterView } from 'vue-router'
  import { useAccountStore } from './stores/accounts';
</script>

<style scoped>
</style>
