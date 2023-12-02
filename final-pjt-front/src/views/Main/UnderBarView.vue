<template>
  <nav>
    <div v-if="store.isLogin == false" class="container text-center">
      <div class="row">
      <div class="col-4">
        <h3 class="col">안녕하세요 반갑습니다 🙂 </h3>
      </div>
      <div class="col-8">
        <RouterLink class="col-2" :to="{ name: 'Main' }"> <button>⛪Home </button></RouterLink> 
        <RouterLink class="col-1" :to="{ name: 'SignUp' }"> <button>회원가입</button></RouterLink>
        <!-- <RouterLink class="col" :to="{ name: 'LogIn' }"> <button>Login</button></RouterLink>  -->
        <RouterLink class="col" :to="{ name: 'financeProducts' }"> <button>💰FinanceProducts</button></RouterLink> 
        <RouterLink class="col" :to="{ name: 'findBank' }"><button>은행 찾기</button></RouterLink> 
        <div>
        </div>
      </div>
      </div>
    </div>
    
    <div v-else class="container text-center">
      <div class="row">
        <div class="col-3">
          <h3>안녕하세요 {{ store.userdata.username }} 님</h3>
        </div>
        <div class="col-9">
          <RouterLink class="col-2" style="margin-left: 5px; margin-right: 5px" :to="{ name: 'Main' }"> <button>⛪Home</button> </RouterLink> 
          
          <RouterLink class="col" :to="{ name: 'financeProducts' }"> <button>💰FinanceProducts</button></RouterLink>
          
          <RouterLink class="col-1" :to="{ name: 'findBank' }"><button>은행 찾기</button></RouterLink> 
          
          <RouterLink class="col-2" style="margin-left: 5px; margin-right: 5px;" :to="{ name: 'profile' }"><button>📑프로필</button>  </RouterLink> 
          
          <button class="col-1.5" @click="store.logOut" style="margin-left: 5px; margin-right: 5px"> 로그아웃 </button> 
          
          <!-- <RouterLink class="col-1" style="margin-left: 5px; margin-right: 5px"  :to="{ name: 'Byebye' }"> <button>회원탈퇴</button> </RouterLink>  -->
          <div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<!-- <template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">🙂</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item" v-if="store.isLogin == false">
            <RouterLink class="nav-link hover-effect" :to="{ name: 'Main' }">⛪Home</RouterLink>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'SignUp' }">회원가입</RouterLink>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'LogIn' }">Login</RouterLink>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'financeProducts' }">💰FinanceProducts</RouterLink>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'findBank' }">은행 찾기</RouterLink>
          </li>
          <li class="nav-item" v-else>
            <span class="navbar-text mr-3">안녕하세요 {{ store.userdata.username }} 님</span>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'profile' }">📑프로필</RouterLink>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'Main' }">⛪Home</RouterLink>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'financeProducts' }">💰FinanceProducts</RouterLink>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'findBank' }">은행 찾기</RouterLink>
            <button class="btn btn-outline-secondary mx-2 hover-effect" @click="store.logOut">로그아웃</button>
            <RouterLink class="nav-link hover-effect" :to="{ name: 'Byebye' }">회원탈퇴</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template> -->


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'
import ByebyeView from '@/views/User/ByebyeView.vue'
// import ExchangeRateView from './views/ExchangeRate/ExchangeRateView.vue'
// import findBank from '@/components/Map/findBank.vue'

const store = useAuthStore()

const user = store.userInfo.value
console.log(user)

</script>

<style scoped>
* {
  background-color: #83A2FF;
  padding-top: 5px;
}

.hover-effect {
  transition: all 0.3s ease;
}

.hover-effect:hover {
  text-decoration: underline;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
</style>