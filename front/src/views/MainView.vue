<template>
  <div>
    <h1>발표 순서 입찰</h1>
    <section class="flex">
      <Vote 
        v-for="vote in store.votes"
        :key="vote.id"
        :vote="vote"
      ></Vote>
    </section>
  </div>
</template>

<script setup>
  import Vote from '@/components/Vote.vue'
  import { ref, onMounted } from 'vue'
  import { useVoteStore } from '@/stores/vote';
  const store = useVoteStore()
  onMounted(() => {
    store.getVoteInfo()
    // setInterval(() => store.getVoteInfo(), 10000)
  })

  
</script>

<style scoped>
.flex {
  display: flex;
  margin: auto;
  width: 80%;
  flex-wrap: wrap;

}
</style>