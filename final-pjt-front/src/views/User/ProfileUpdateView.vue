<template>
    <h2>{{username}}님의 정보수정 페이지 입니당</h2>
    <div class="page"></div>
    <div class="container">
      <div class="row d-flex justify-content-between">
        <div class="col-6">
            <hr>
          <div>
            <form @submit.prevent="submit(password1)">
                <input type="password" v-model="password1" autocomplete="new-password"> 💨
                <input type="submit" value='Password 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(email)">
                <input type="email" v-model="email"> 💨
                <input type="submit" value='이메일 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(nickname)">
                <input type="text" v-model="nickname"> 💨
                <input type="submit" value='닉네임 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(address)">
                <input type="text" v-model="address"> 💨
                <input type="submit" value='주소 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(gender)">
                <input type="text" v-model="gender"> 💨
                <input type="submit" value='성별 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(birthday)">
                <input type="text" v-model="birthday"> 💨
                <input type="submit" value='생년월일 수정'>
            </form>
        </div>
        </div>
        <div class="col-6">
                
        <hr>
        <div>
            <form @submit.prevent="submit(interest)">
                <input type="text" v-model="interest"> 💨
                <input type="submit" value='관심사 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(married_period)">
                <input type="number" v-model="married_period"> 💨
                <input type="submit" value='결혼기간 수정'>
            </form>
        </div>
 
        <hr>
        <div>
            <form @submit.prevent="submit(main_bank)">
                <input type="text" v-model="main_bank"> 💨
                <input type="submit" value='주거래은행 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(couple_nickname)">
                <input type="text" v-model="couple_nickname"> 💨
                <input type="submit" value='배우자 닉네임 수정'>
            </form>
        </div>
        <hr>
        <div>
            <form @submit.prevent="submit(couple_birthday)">
                <input type="text" v-model="couple_birthday"> 💨
                <input type="submit" value='배우자 생년월일 수정'>
            </form>
        </div>
        <hr>
        <button @click="goupdate" style="color: white; background-color:teal;"> 수정이 모두 완료되면 누르세요 </button>
    </div>
</div>
<div style="height: 8rem;"></div>
<RouterLink class="col-1" style="margin-left: 5px; margin-right: 5px"  :to="{ name: 'Byebye' }"> <button>회원탈퇴</button> </RouterLink> 
    </div>
    <div>
        <!-- <div>
            <form @submit.prevent="submit(username)">
                <input type="text" v-model="username"> 💨
                <input type="submit" value='ID 수정'>
            </form>
        </div> -->
        <hr>
    
  
        
    </div>
</template>


<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { RouterLink, RouterView } from 'vue-router'
import ProfileView from '@/views/User/ProfileView.vue'
const store = useAuthStore()
const router = useRouter()
const goupdate = function(){
        router.go(-1)
    }
    

const username = ref(store.userdata.username)
const password1 = ref(store.userdata.password1)
const password2 = ref(store.userdata.password2)
const email = ref(store.userdata.email)
const nickname = ref(store.userdata.nickname)
const address = ref(store.userdata.address)
const gender = ref(store.userdata.gender)
const birthday = ref(store.userdata.birthday)
const interest = ref(store.userdata.interest)
const married_period = ref(store.userdata.married_period)
const saving_target_period = ref(store.userdata.saving_target_period)
const main_bank = ref(store.userdata.main_bank)
const couple_nickname = ref(store.userdata.couple_nickname)
const couple_birthday = ref(store.userdata.couple_birthday)

const submit = function (username) {
    axios({
        method: 'put',
        url: `${store.URL}/accounts/updateinfo/${store.userdata.username}/`,
        headers: {
            Authorization: `Token ${store.token}`
        },
        data: { 
            username: username.value,
            password1: password1.value,
            password2: password2.value,
            email: email.value,
            nickname: nickname.value,
            address: address.value,
            gender: gender.value,
            birthday: birthday.value,
            interest: interest.value,
            married_period: married_period.value,
            saving_target_period: saving_target_period.value,
            main_bank: main_bank.value,
            couple_nickname: couple_nickname.value,
            couple_birthday: couple_birthday.value
         },

    })
        .then(res => {
            console.log(res.data)
            store.userdata = res.data
        })
        .catch(err => {
            console.log(err)
        })
}

</script>

<style scoped>
.page{
    padding-bottom: 1rem;
}
</style>