import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '../router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      // console.log(res);
      // console.log(res.data);
      articles.value = res.data
    })
    .catch(err => console.log(err))
  }


  const signup = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    // const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    }).then(res => {
      console.log('회원가입이 완료되었습니다.');
      console.log(res)
      const password = password1
      logIn({ username, password })
    }).catch(err => console.error(err.response.data))
  }

  const token = ref(null)

  const logIn = function (payload) {
    const { username, password } = payload
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data:{
        username, password
      }
    }) .then(res => {
      console.log('로그인이 완료되었습니다');
      console.log(res.data);
      token.value = res.data.key
      router.push({ name:'ArticleView'})
    }) .catch(err => console.log(err.response.data))
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


  return { articles, API_URL, getArticles, signup, logIn, token, isLogin }
}, { persist: true })
