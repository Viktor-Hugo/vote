<template>
  <div :class="{'last-bid-team': isLastBidTeam}">
    <h2>{{ vote.id }} 번째 발표</h2>
    <h3>최상위 입찰가 : {{ vote.price }}</h3>
    <p v-if="vote.teams.length">입찰 팀 목록 : 
      <span v-for="team in vote.teams" :key="team">
        {{ team }} | 
      </span>
    </p>
    <p v-else>현재 입찰 팀 없음</p>
    <BidForm 
      :vote="vote"
    />
    <hr>
  </div>
</template>

<script setup>
  import { computed } from 'vue'
  import BidForm from './BidForm.vue'
  import { useAccountStore } from '@/stores/accounts';
  const props = defineProps({
    vote: Object
  })
  const accountStore = useAccountStore()
  const isLastBidTeam = computed(() => {
    return props.vote.last_bid_team === accountStore.userInfo.id
  })
</script>

<style scoped>
.last-bid-team {
  background-color: rgb(255, 223, 211);
}
</style>