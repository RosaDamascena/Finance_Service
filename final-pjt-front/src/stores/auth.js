// stores/auth.js
import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()
  const user = ref(null)
  const token = ref(null)
  const isAuthenticated = ref(false)
  const URL = 'http://127.0.0.1:8000'
  const userdata = ref(null)
  const likeDeposit = ref(false)
  const likeSavings = ref(false)
  
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    console.log(payload)
    const username = payload.username
    const email = payload.email
    const nickname = payload.nickname
    const password1 = payload.password1
    const password2 = payload.password2
    const address = payload.address
    const gender = payload.gender
    const birthday = payload.birthday
    const interest = payload.interest
    const married_period = payload.married_period
    const saving_target_period = payload.saving_target_period
    const main_bank = payload.main_bank
    
    const couple_nickname = payload.couple_nickname
    const couple_birthday = payload.couple_birthday
    // // 구조 분해할당
    // const { username, password1, password2, email, nickname,
    //    address, gender, birthday, interest, married_period,
    //    saving_target_period, main_bank } = payload

    console.log( username,
      password1,
      password2,
      email,
      nickname,
      address,
      gender,
      birthday,
      interest,
      married_period,
      saving_target_period,
      main_bank,
      couple_nickname,
      couple_birthday,)
    axios({
      method: 'post',
      url: `${URL}/dj-rest-auth/signup/`,
      data: {
        username,
        password1,
        password2,
        email,
        nickname,
        address,
        gender,
        birthday,
        interest,
        married_period,
        saving_target_period,
        main_bank,
        couple_nickname,
        couple_birthday,
      }
    })
      .then((res) => {
        // token.value = res.data.key
        // isAuthenticated.value = true
        console.log('회원가입 완료')
        // user.value = res.data
        router.push({ name: 'Main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${URL}/dj-rest-auth/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 완료')
        token.value = res.data.key
        user.value = username
        // router.go(-1)
        router.push({ name: 'Main' })
        console.log(token.value, user.value)
      })
      .catch((err) => {
        console.log(err)
        window.alert('아이디 혹은 비밀번호가 틀렸습니다')
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${URL}/dj-rest-auth/logout/`
    })
      .then((res) => {
        console.log('로그아웃 완료')
        token.value = null
        console.log(token.value, user.value)
        user.value = null
        router.push({ name: 'Main' })
        localStorage.removeItem('likedProducts')
        // console.log(token, userId)
      })
      .catch((err) => {
        console.log(err)
        window.alert('로그아웃되지 않았습니다.')
      })
  }


  // 유저정보 반환해서 profile 만들기
  const userInfo = function () {
    axios({
      method: 'get',
      url: `${URL}/accounts/userinfo/${user.value}`,
      headers: {
        Authorization: `Token ${token.value}`
      }
      // data: {
      //   username,
      //   email,
      //   nickname,
      //   birthday,
      //   interest,
      //   married_period,
      //   main_bank,
      //   couple_nickname,
      //   couple_birthday,
      // }
    })
      .then((res) => {
        // console.log(res.data)
        userdata.value = {
          userid : res.data.id,
          username : res.data.username,
          password1 : res.data.password1,
          password2 : res.data.password2,
          email : res.data.email,
          nickname : res.data.nickname,
          address: res.data.address,
          gender : res.data.gender,
          birthday : res.data.birthday,
          interest : res.data.interest,
          married_period : res.data.married_period,
          saving_target_period : res.data.saving_target_period,
          main_bank: res.data.main_bank,
          couple_nickname : res.data.couple_nickname,
          couple_birthday : res.data.couple_birthday,
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const dpLike = async (depositProductId) => {
    try {
      const response = await axios({
        method: 'post',
        url: `${URL}/api/v1/deposit_products/${depositProductId}/like/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
      });
      
      return response.data
    } catch (error) {
      console.log(error)
    }
  }

  const count_dp = ref(0)
  const dpLikeCount = async (depositProductId) => {
    try {
      const response = await axios({
        method: 'get',
        url: `${URL}/api/v1/deposit_products/${depositProductId}/like/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
      });
      
      return response.data
    } catch (error) {
      console.log(error)
    }
  }

  const spLike = async (savingsProductId) => {
    try {
      const response = await axios({
        method: 'post',
        url: `${URL}/api/v1/savings_products/${savingsProductId}/like/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
      });
      
      return response.data
    } catch (error) {
      console.log(error)
    }
  }

  const count_sp = ref(0)
  const spLikeCount = async (savingsProductId) => {
    try {
      const response = await axios({
        method: 'get',
        url: `${URL}/api/v1/savings_products/${savingsProductId}/like/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
      });
      
      return response.data
    } catch (error) {
      console.log(error)
    }
  }

  // const count_sp = ref(0)
  // const spLikeCount = function (savingsProductId) {
  //   axios({
  //     method: 'get',
  //     url: `${URL}/api/v1/savings_products/${savingsProductId}/like/`
  //   })
  //     .then((res) => {
  //       count_dp.value = res.data.count
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }

  // const spLike = (savingsProductId) => {
  //   axios({
  //       method: 'post',
  //       url: `${URL}/api/v1/savings_products/${savingsProductId}/like/`,
  //       headers: {
  //           Authorization: `Token ${store.token.value}`
  //       },
  //   })
  //     .then(res => {
  //       likeSavings.value = res.data,
  //       console.log(likeSavings.value)
  //   })
  //     .catch(error => console.log(error))
  // }

  const byebye = function (payload) {
    const { password1 } = payload
    axios ({
      method: 'post',
      url: `${URL}/accounts/byebyeuser/`,
      data: {
        password1
      },
      headers: {
        Authorization: `Token ${token.value}`
      }})
      .then((res) => {
        console.log('Account deleted successfully')
        logOut()
        router.push({ name: 'Main' })
        window.alert('그동안 fortunetree와 함께 해주셔서 감사합니다.')
      })
      .catch((err) => {
        console.error('Account deletion failed:', err)
        window.alert('비밀번호가 틀렸습니다.')
      })
  }

  return { URL, signUp, logIn, token, logIn, logOut, user, userInfo, isLogin, userdata, isAuthenticated, likeDeposit, likeSavings, spLike, dpLike, count_dp, count_sp, spLikeCount, dpLikeCount, byebye }
}, { persist: true })