<template>
  <header
    v-show="useAccountStore().userInfo.username === 'admin'"
  >
    <button 
      @click="deadline"
    >
      마감
    </button>
    <RouterLink :to="{name:'result'}">Result</RouterLink>
  </header>
  <button 
    @click="isActivate = !isActivate"
    v-show="!isActivate"
    class="tip-button"
  >
    도움말
  </button>
  <Tip
    v-show="isActivate"
    :isActivate="isActivate"
    @toggle="isActivate = !isActivate"
  />
  <h1 v-if="useAccountStore().isAuthenticated">보유 포인트 : {{ useAccountStore().balance }} </h1>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'
  import { useAccountStore } from './stores/accounts';
  import Tip from './components/Tip.vue';
  import { ref } from 'vue';
  import axios from 'axios'
  
  const API_URL = import.meta.env.VITE_API_URL
  const isActivate = ref(false)
  const deadline = function () {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/deadline/`,
      headers: {
        Authorization: `Token ${useAccountStore().userInfo.token}`,
      },
    })
      .then(res => null)
      .catch(err => null)
  }
</script>

<style scoped>
.tip-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #ffab91; /* Matching the theme color */
  color: #fff;
  border: none;
  border-radius: 50px;
  padding: 10px 20px;
  font-size: 1em;
  cursor: pointer;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
  transition: background-color 0.3s ease; /* Smooth transition */
}

.tip-button:hover {
  background-color: #ff7043; /* Darker orange on hover */
}
</style>
