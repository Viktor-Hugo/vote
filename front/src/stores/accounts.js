import { defineStore } from "pinia"
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const API_URL = import.meta.env.VITE_API_URL
  const router = useRouter()
  const isAuthenticated = ref(false)
  const userInfo = ref({
    token: null
  })
  const login = function ({username, password}) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      },
    })
    .then(res => {
        userInfo.value.token = res.data.key
        isAuthenticated.value = true
        getUserInfo()
        router.push({name:'main'})
      })
    .catch(err => {window.alert(err.data)})
  }

  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/userinfo/`,
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
  return { isAuthenticated, login, getUserInfo, userInfo, balance }
},  { persist: true })