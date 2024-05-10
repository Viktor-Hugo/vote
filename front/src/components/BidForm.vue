<template>
  <form @submit.prevent="useVoteStore().bid({vote, payment})">
    <input type="number" name="payment" id="payment" :placeholder="vote.price+10" v-model="payment">
    <input type="submit" value="입찰">
  </form>
</template>

<script setup>
  import { useVoteStore } from '@/stores/vote';
  import { ref, watch } from 'vue'
  const props = defineProps({
    vote: Object
  })
  
  const payment = ref(props.vote.price + 10)
  
  watch(() => props.vote.price, (newVal) => {
    payment.value = newVal + 10
  })

 
</script>

<style scoped>

</style>