<template>
  <div>
    {{  }}
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useAccountStore } from '@/stores/accounts';
  import axios from 'axios'
  
  const API_URL = import.meta.env.VITE_API_URL
  const result = ref([])
  onMounted(() => {
    axios({
      method: 'GET',
      url: `${API_URL}/api/v1/winner/`,
      headers: {
        Authorization: `Token ${useAccountStore().userInfo.token}`,
      },
    })
      .then(res => console.log(res.data))
      .catch(err => null)
  })
 
</script>

<style scoped>

</style>