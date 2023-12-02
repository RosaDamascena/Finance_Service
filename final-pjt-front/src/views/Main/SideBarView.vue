<template>
    <div class="container mt-4">
      <img style="width: 16rem; padding-bottom: 2rem ;" src="/assets/fortuntree.png" alt="">
      <div class="card mb-4" v-if="store.isLogin == false">
        <div class="card-body">
          <h5 class="card-title">비로그인 상태입니다</h5>
          <div class="d-flex justify-content-between">
            <RouterLink class="btn btn-primary" :to="{ name: 'SignUp' }">회원가입</RouterLink>
            <RouterLink class="btn btn-secondary" :to="{ name: 'LogIn' }">Login</RouterLink>
          </div>
        </div>
      </div>
      
      <div class="card mb-4" v-else>
        <div class="card-body">
          <h5 class="card-title">{{ store.username }}</h5>
          <div class="d-flex justify-content-between">
            <RouterLink class="btn btn-primary" :to="{ name: 'profile' }">📑프로필</RouterLink>
            <button class="btn btn-danger" @click="store.logOut">로그아웃</button>
          </div>
        </div>
      </div>
  
      <div class="card mb-4">
        <div class="card-body">
          <div class="d-flex flex-column justify-content-center">
            <div class="text-center">{{ currentDate }}</div>
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <iframe src="http://free.timeanddate.com/clock/i94e14xp/n594/szw160/szh160/hoc99f/hbw0/cf100/hgr0/fan2/fas20/facfff/fdi86/mqc009/mqs2/mql3/mqw4/mqd70/mhc83a2ff/mhs4/mhl3/mhw4/mhd70/mmv0/hhc06f/hhs3/hms3/hsc009" frameborder="0" width="160" height="160"></iframe>
            </div>
          </div>
        </div>
      </div>
  
      <div class="card mb-4">
        <div class="card-body">
          <ExchangeRateView />
        </div>
      </div>
  
      <div class="card mb-4">
        <div class="card-body">
          <rateCalculator />
        </div>
      </div>
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'
import ExchangeRateView from '@/views/ExchangeRate/ExchangeRateView.vue'
import Dday from '@/components/Profile/Dday.vue'
import rateCalculator from '@/components/MainPageView/rateCalculator.vue'
import { ref, onMounted } from 'vue';

const currentDate = ref('');

onMounted(() => {
  const date = new Date();
  currentDate.value = `${date.getFullYear()}년 ${date.getMonth() + 1}월 ${date.getDate()}일`;
});


const store = useAuthStore()
</script>

<style scoped>
nav {
  background-color: #a0b4f1;
  position: fixed;
  height: 6rem;
  padding-left: 1.3rem;
  top: 90%;
  left: 0;
  /* 항상 젤 위에 위치하게 하기 위해서 z-index */
  z-index: 1000;
  width: 100%;

}

</style>