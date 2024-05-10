<template>
  <div>
    <h1>발표 순서 입찰</h1>
    <Vote 
      v-for="vote in store.votes"
      :key="vote.id"
      :vote="vote"
    ></Vote>
  </div>
</template>

<script setup>
  import Vote from '@/components/Vote.vue'
  import { ref, onMounted } from 'vue'
  import { useVoteStore } from '@/stores/vote';
  const store = useVoteStore()
  onMounted(() => {
    store.getVoteInfo()
  })

  
</script>

<style scoped>

</style>