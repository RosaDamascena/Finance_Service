<template>
  <div >
      <!-- <div>
          <p> D-DAY</p>
          <datepicker
              v-model="selected"
              :locale="locale"
              :upperLimit="to"
              :lowerLimit="from"
              :clearable="true"
          />
      </div> -->


      <div v-if="userdata?.couple_nickname" class="align" >
          <div>
              <!-- <div v-if="userdata?.birthday"> -->
                  <!-- <img class="img1" src="@/assets/6.png" alt="프로필이미지"> -->
                  <img class="img1" :src="`/assets/${selfimage}.png`" alt="프로필이미지">
              <!-- </div> -->
              <p>{{ userdata?.nickname }}</p>
              <p>{{ userdata?.birthday }}</p>
          </div>
          <!-- <p>{{ us }}</p> -->
          <div>
              <p> 💙</p>
          </div>
          <div>
              <img class="img2" :src="`/assets/${coupleimage}.png`" alt="프로필이미지">
              <p>{{ userdata?.couple_nickname }}</p>
              <p>{{ userdata?.couple_birthday }}</p>
              <!-- <p>{{ imagecompute }}</p> -->
          </div>
      </div>
      <div v-else="userdata?.couple_birthday" class="align" >
          <div>
              <!-- <div v-if="userdata?.birthday"> -->
                  <!-- <img class="img1" src="@/assets/6.png" alt="프로필이미지"> -->
                  <img class="img1" :src="`/assets/${selfimage}.png`" alt="프로필이미지">
              <!-- </div> -->
              <p>{{ userdata?.nickname }}</p>
              <p>{{ userdata?.birthday }}</p>
          </div>
          <!-- <p>{{ us }}</p> -->
          <div>
              <p> 💙</p>
          </div>
          <div>
              <img class="img2" :src="`/assets/${coupleimage}.png`" alt="프로필이미지">
              <p>{{ userdata?.couple_nickname }}</p>
              <p>{{ userdata?.couple_birthday }}</p>
              <!-- <p>{{ imagecompute }}</p> -->
          </div>
      </div>
      <div v-else class="align">
          <div>
              <img class="img1"  :src="`/assets/${selfimage}.png`" alt="프로필이미지">
              <hr>
              <p> 성함 : {{ userdata?.username }}</p>
              <p> 이메일 : {{ userdata?.email }}</p>
              <p> 닉네임 : {{ userdata?.nickname }}</p>
              <p> 생년월일 : {{ userdata?.birthday }}</p>
              <p> 관심사 : {{ userdata?.interest }}</p>
              <p> 결혼기간 : {{ userdata?.married_period }}개월</p>
              <p> 주거래은행 : {{ userdata?.main_bank }}</p>
          </div>
      </div>
      <hr>
          <button @click="goupdate(userdata?.username)">프로필수정</button>
      <hr>
  </div >

</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth.js'
// import Datepicker from 'vue3-datepicker'
import { format, compareAsc} from 'date-fns'
import {RouterLink, useRouter} from 'vue-router'
import dayjs from 'dayjs'



const router = useRouter()
const store = useAuthStore()
const userdata = ref(null)

const selfimage = ref([])
const coupleimage = ref([])
// const imagecompute = computed(() => {
//   if (userdata.value && userdata.value.birthday) {
//     return parseInt(userdata.value.birthday.slice(0, 4)) % 12;
//   }
//   return 0; // 기본값으로 설정할 값
// });

// const imagesource = computed(() => {
//   return '@/assets/' + imagecompute.value + '.png';
// });

const goupdate = function(username){
  router.push({name:'ProfileUpdateView', params:{username:username}})
}

onMounted(() => {
  store.userInfo()
  userdata.value = store.userdata

  // 본인 12간지 프로필 사진
  selfimage.value = parseInt(userdata.value.birthday.slice(0,4)) % 12
  console.log(selfimage.value) // 5

  // 배우자 12간지 프로필 사진
  if(userdata?.value?.couple_nickname){
  coupleimage.value = parseInt(userdata?.value.couple_birthday.slice(0,4)) % 12
  console.log(coupleimage.value)
  }
 


  // console.log(typeof userdata.value.birthday) // string
  // console.log(parseInt(userdata.value.birthday.slice(0,4))%12) // number
  // 목표 날짜와 현재 날짜 받아서 디데이 계산하기 
  // format(new Date())

  // console.log(userdata.value.birthday)

  // 12간지 프로필 이미지생성하기 
  // const imagecompute = ref(0)

  // // const birthnumber = userdata.value.birthday.slice(0,3)
  // // console.log(birthnumber)
  // const imagecompute = computed(() => parseInt(userdata.birthday.slice(0,3)) % 12)
  // console.log(imagecompute.value)
  // const imagecompute = computed(() => userdata.value.birthday.slice(0,4) % 12)
  

  // const imagecompute = computed(() => parseInt(userdata?.birthday.slice(0, 3)) % 12);
  // console.log(imagecompute)
  // const imagesource = '@/assets/' + imagecompute + '.png'
  // console.log(imagesource)
})



</script>

<style scoped>

.align {
  display: flex;
  justify-content: center; /* 수평 가운데 정렬 */
  align-items: center; /* 수직 가운데 정렬 */
  flex-direction: row; /* 요소들을 가로로 나열합니다. */
  text-align: center; 
}
.d-day_p {
  font-size: 80px;
}

.img1 {
  width: 80px;
  border-radius: 60%;
  background-color: bisque;
  border: 2px solid;
}

.img2 {
  width: 80px;
  border-radius: 60%;
  background-color: rgb(175, 197, 238);
  border: 2px solid;
}
</style>
