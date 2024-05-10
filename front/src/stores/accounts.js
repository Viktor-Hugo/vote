import { defineStore } from "pinia"
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const router = useRouter()
  const isAuthenticated = ref(false)
  const userInfo = ref({
    token: null
  })
  const login = function ({username, password}) {
    console.log(username, password)
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      },
    })
    .then(res => {
        console.log(res)
        userInfo.value.token = res.data.key
        isAuthenticated.value = true
        getUserInfo()
        router.push({name:'main'})
      })
    .catch(err => window.alert(err))
  }

  const getUserInfo = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/accounts/userinfo/',
      headers: {
        Authorization: `Token ${userInfo.value.token}`
      }
    }) 
      .then(res => {
        userInfo.value = {...res.data, ...userInfo.value}
      })
      .catch(err => console.log(err))
  }

  const balance = computed(() => {
    return userInfo.value.score
  })
  return { isAuthenticated, login, userInfo, balance }
},  { persist: true })