<template>
  <div 
    :class="{'last-bid-team': isLastBidTeam}"
    class="bid-card"
  >
    <h2>{{ vote.id }} 번째 발표</h2>
    <h3>최상위 입찰가 : {{ vote.price }}</h3>
    <p>입찰 팀 목록 : </p>
    <div 
      v-if="vote.teams.length"
      class="bid-list"
    >
      <ul>
        <li 
          v-for="(item, idx) in vote.teams" :key="item.team"
          :class="{first: !idx}"
        >
          {{ item.team }} 팀 | 입찰가 : {{ item.payment }}
        </li>
      </ul>
    </div>
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
template {
  width: 300px;
}

.bid-card {
  margin: 20px;
  border-radius: 10px; /* Rounded corners for a softer look */
  border: 2px solid steelblue; /* Border to highlight the section */
  padding: 20px; /* Adding padding for better spacing */

}
.last-bid-team {
  background-color: #ffe0b2; /* Soft orange background */
  border: 2px solid #ffab91; /* Border to highlight the section */

}

.bid-list {
  height: 200px;
  max-height: 200px;
  overflow-y: auto;
  background-color: rgb(255, 255, 255);
  border-radius: 5px;
  border: 2px solid salmon;
  margin-bottom: 10px;
}

.bid-list::-webkit-scrollbar {
  width: 3px;
}
.bid-list::-webkit-scrollbar-thumb {
  background-color: #2f3542;
  border-radius: 10px;
  height: 5px;
  background-clip: padding-box;
  border: 2px solid black;
}
.bid-list::-webkit-scrollbar-track {
  background-color: grey;
  border-radius: 10px;
  box-shadow: inset 0px 0px 5px white;
}

h2 {
  font-size: 1.5em;
  margin-bottom: 10px;
}

h3 {
  font-size: 1.2em;
  margin-bottom: 20px;
  color: #d32f2f; /* Dark red color for contrast */
}

ul {
  list-style-type: none; /* Removing default list styling */
  padding: 0; /* Removing default padding */
}

li {
  padding: 10px;
  margin-bottom: 5px;
  border-bottom: 1px solid #e0e0e0; /* Light grey border for separation */
}


li.first {
  font-weight: bold;
  color: #388e3c; /* Green color to highlight the first item */
}

p {
  font-size: 1em;
  color: #616161; /* Grey color for secondary text */
}

hr {
  border: none;
  border-top: 1px solid #e0e0e0; /* Light grey border for a subtle divider */
  margin: 20px 0;
}
</style>