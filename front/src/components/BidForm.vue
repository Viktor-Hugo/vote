<template>
  <form @submit.prevent="useVoteStore().bid({vote, payment})">
    <input type="number" name="payment" id="payment" :placeholder="vote.price+10" v-model="payment">
    <input type="submit" value="입찰">
  </form>
  <form 
    @submit.prevent="useVoteStore().bidCancle({vote})"
    v-show="vote.teams.includes(useAccountStore().userInfo.id)"
  >
    <input type="submit" value="입찰 취소">
  </form>
</template>

<script setup>
  import { useVoteStore } from '@/stores/vote';
  import { useAccountStore } from '@/stores/accounts';
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