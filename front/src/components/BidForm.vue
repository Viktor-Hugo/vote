<template>
  <div class="bid-container">
    <form @submit.prevent="useVoteStore().bid({ vote, payment })" class="bid-form">
      <input type="number" name="payment" id="payment" :placeholder="vote.price + 10" v-model="payment">
      <input type="submit" value="입찰">
    </form>
    <form 
      @submit.prevent="useVoteStore().bidCancle({ vote })"
      v-show="
        (
          vote.last_bid_team != useAccountStore().userInfo.id
          &&
          vote.teams.some(item => item.team === useAccountStore().userInfo.id)
        )
      "
      class="cancel-form"
    >
      <input type="submit" value="입찰 취소">
    </form>
  </div>
</template>

<script setup>
  import { useVoteStore } from '@/stores/vote';
  import { useAccountStore } from '@/stores/accounts';
  import { ref, watch } from 'vue';
  
  const props = defineProps({
    vote: Object
  });
  
  const payment = ref(props.vote.price + 10);
  
  watch(() => props.vote.price, (newVal) => {
    payment.value = newVal + 10;
  });
</script>

<style scoped>
.bid-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px; /* Gap between forms */
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
  margin: 20px 0; /* Margin to separate from other content */
}

.bid-form, .cancel-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px; /* Gap between form elements */
  width: 100%;
}

.bid-form input[type="number"],
.cancel-form input[type="submit"],
.bid-form input[type="submit"] {
  padding: 10px;
  border: 1px solid #e0e0e0; /* Light grey border */
  border-radius: 5px; /* Rounded corners */
  font-size: 1em;
  width: 100%; /* Full width input fields */
  box-sizing: border-box; /* Ensure padding and border are included in the width */
}

.bid-form input[type="submit"] {
  background-color: #93ff9a; /* Matching the border color of the last-bid-team class */
  color: black;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease; /* Smooth transition */
  border: 5px solid #93ff9a ; /* Darker orange on hover */

}

.bid-form input[type="submit"]:hover {
  border: 5px solid #93ff9a ; /* Darker orange on hover */
  background-color: rgb(233, 255, 226);
}

.cancel-form input[type="submit"] {
  background-color: #ff7043; /* Matching the border color of the last-bid-team class */
  color: #fff;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease; /* Smooth transition */
  border: 5px solid #ff7043 ; /* Darker orange on hover */

}

.cancel-form input[type="submit"]:hover {
  border: 5px solid #ff7043 ; /* Darker orange on hover */
  background-color: rgb(255, 236, 226);
  color: black;
}

</style>
