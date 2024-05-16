import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from './accounts'
import axios from 'axios'

export const useVoteStore = defineStore('vote', () => {
  const API_URL = import.meta.env.VITE_API_URL
  const accountsStore = useAccountStore()
  const votes = ref([])

  const getVoteInfo = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/`,
      headers: {
        Authorization: `Token ${accountsStore.userInfo.token}`
      }
    })
      .then(res => {
        votes.value = res.data
      })
      .catch(err => {
        window.alert(err.data)
      })
  }

  const bid = function ({vote, payment}) {
    if (window.confirm(
        `${vote.id} 번째 발표를 \n${payment} 포인트로 입찰 합니까?
        \n 현재 ${vote.last_bid_team === accountsStore.userInfo.id ? '당신' : vote.last_bid_team}팀이 최상위 입찰자 입니다.
        `)) 
      {
      
      if (accountsStore.userInfo.score < payment) {
        window.alert(
          `보유 금액 부족 \n보유 금액 : ${accountsStore.userInfo.score} \n입찰 시도 금액 : ${payment}
          `)
      } else if (payment <= vote.price) {
        window.alert(
          `구매 가능 금액 미달 \n최소 금액 : ${vote.price} \n입찰 시도 금액 : ${payment}
          `)
      } else {
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/bid/${vote.id}/`,
          headers: {
            Authorization: `Token ${accountsStore.userInfo.token}`,
          },
          data: {
            payment
          }
        })
          .then(res => {
            votes.value.forEach(v => {
              if (v.id === vote.id) {
                v.last_bid_team = res.data.order.last_bid_team
                v.price = res.data.order.price
                v.teams = res.data.order.teams
              }
            })
            accountsStore.userInfo.score = res.data.balance
    
          })
          .catch(err => {
            if (err.response.status === 406) {
              window.alert('마감 되었습니다.')
            } else if (err.response.status === 400) {
              const {data, balance, price} = err.response.data
              if (data === '구매 가능 금액 미달') {
                window.alert(`${data} \n최소 금액 : ${price}`)
              } else {
                window.alert(`${data} \n보유 금액 : ${balance}`)
              }
            }
          })
      }
    }
  }

  const bidCancle = function ({vote}) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/bid/${vote.id}/cancle/`,
      headers: {
        Authorization: `Token ${accountsStore.userInfo.token}`,
      },
    })
      .then(res => {
        const { balance, refundAmount, lastBidPayment } = res.data
        accountsStore.userInfo.score = res.data.balance
        window.alert(`반환 포인트 : ${refundAmount} \n현재 보유금 : ${balance}`)
        getVoteInfo()
      })
      .catch(err => {
        if ( err.response.status === 403 ) {
          window.alert(`최상위 입찰자는 입찰 취소가 불가능 합니다.`)
        } else if (err.response.status === 406) {
          window.alert('마감 되었습니다.')
        } else {
          window.alert('권한 없음.')
        }
      })
  }
  return { getVoteInfo, bid, bidCancle, votes }
})
