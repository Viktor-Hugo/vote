import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from './accounts'
import axios from 'axios'

export const useVoteStore = defineStore('vote', () => {
  const accountsStore = useAccountStore()
  const votes = ref([])
  const getVoteInfo = function () {
    axios({
      method: 'get',
      url: 'https://vote-tqrw.onrender.com//api/v1/',
      headers: {
        Authorization: `Token ${accountsStore.userInfo.token}`
      }
    })
      .then(res => {
        votes.value = res.data
      })
      .catch(err => console.log(err))
  }

  const bid = function ({vote, payment}) {
    axios({
      method: 'post',
      url: `https://vote-tqrw.onrender.com//api/v1/bid/${vote.id}/`,
      headers: {
        Authorization: `Token ${accountsStore.userInfo.token}`,
      },
      data: {
        payment
      }
    })
      .then(res => {
        console.log(res.data)
        votes.value.forEach(v => {
          if (v.id === vote.id) {
            v.price = res.data.order.price
            v.teams = res.data.order.teams
          }
        })
        accountsStore.userInfo.score = res.data.balance

      })
      .catch(err => console.log(err))
  }
  return { getVoteInfo, bid, votes }
})
