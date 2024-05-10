<template>
  <form @submit.prevent="useAccountStore().login(user)">
    <input type="text" name="username" id="username" v-model="user.username">
    <input type="password" name="password" id="password" v-model="user.password">
    <input type="submit" value="Login">
  </form>
</template>

<script setup>
  import { useAccountStore } from '@/stores/accounts';
  import { ref } from 'vue'
  const user = ref({
    username: '',
    password: '',
  })
</script>

<style scoped>

</style>