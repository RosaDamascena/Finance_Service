<template>
    <div class="container">
        <h1> 회원가입 </h1>
        <form @submit.prevent="signUp">
            <label for="username"> 아이디(닉네임) : </label>
            <input type="text" id="username" v-model.trim="username" placeholder="아이디로 사용됩니다">
            <button type="button" class="btn btn-secondary btn-sm col-3" @click="checkUserID">중복체크</button>
            <p :class="{ 'text-danger': !isPassCheckId, primary: isPassCheckId }">{{ checkMsg }}</p>
            <hr>
            <div class="essentials"> 성별 :
                <select v-model="gender">
                    <option disabled value="">다음 중 하나를 선택하세요</option>
                    <option>남성</option>
                    <option>여성</option>
                </select>
            </div>
            <hr>
 
            <div class="essentials">
                <label for="password1"> 비밀번호 : </label>
                <input type="password" id="password1" v-model.trim="password1" autocomplete="on" placeholder="비밀번호를 입력하세요">
                8글자 이상(특수문자,영어포함) 
            </div>
            <div class="essentials">
                <label for="password2"> 비밀번호 확인 : </label>
                <input type="password" id="password2" v-model.trim="password2" autocomplete="on" placeholder="비밀번호를 확인하세요">
                <div v-if="password1 !== password2 && password2 !== null" class="text-danger">
                     {{ warning }}
                </div>
            </div>


            <hr>
            <div class="essentials">
                <label for="email"> 이메일 : </label>
                <input type="text" id="email" v-model.trim="email" placeholder="email@email.com">
            </div>
            <hr>
            <div>
                <div>
                    <label for="nickname" class="essentials"> 성함 : </label>
                    <input type="text" id="nickname" v-model.trim="nickname" placeholder="성함">
                </div>
                <div>
                    <label for="couple_nickname"> 배우자 닉네임 : </label>
                    <input type="text" id="couple_nickname" v-model.trim="couple_nickname" placeholder="(필수 입력칸은 아닙니다)"><i
                        class="fas fa-star" style="color: #e3c7ff;"></i> 필수입력 항목이 아닙니다
                </div>
            </div>
            <hr>
            <div class="essentials">
                <label for="address"> 거주지가 어디신가요? : </label>
                <input type="text" id="address" v-model.trim="address" placeholder=" ex) 부산">
            </div>
            <hr>
            <div>
                <label for="birthday"> 생년월일 : </label>
                <input style="width: 350px" type="text" id="birthday" v-model.number="birthday"
                    placeholder="19970106 과 같은 형식으로 적어주세요(-없이)">
            </div>
            <div>
                <label for="couple_birthday"> 배우자 생년월일 : </label>
                <input style="width: 350px" type="text" id="couple_birthday" v-model.number="couple_birthday"
                    placeholder="위와 같은 형식으로 적어주세요(필수 입력칸은 아닙니다)"><i class="fas fa-star" style="color: #e3c7ff;"></i> 필수입력
                항목이 아닙니다
            </div>
            <hr>
            <div class="essentials"> 관심사
                <select v-model="interest">
                    <option disabled value="">다음 중 하나를 선택하세요</option>
                    <option>내집마련</option>
                    <option>재태크</option>
                    <option>신혼여행</option>
                    <option>출산</option>
                </select>
            </div>
            <hr>
            <div>
                <label for="married_period"> 결혼한지 얼마나 되셨나요? : </label>
                <input type="text" id="married_period" v-model.number="married_period">
                <span> (개월)</span>
            </div>
            <hr>
            <div>
                <label for="saving_target_period" class="essentials"> 목표 달성할 기간 : </label>
                <input type="text" id="saving_target_period" v-model.number="saving_target_period">
                <span> (개월)</span>
            </div>
            <hr>
            <div> 주거래은행
                <select v-model="main_bank">
                    <option disabled value="">다음 중 하나를 선택하세요</option>
                    <option>우리은행</option>
                    <option>한국스탠다드차타드은행</option>
                    <option>대구은행</option>
                    <option>부산은행</option>
                    <option>광주은행</option>
                    <option>제주은행</option>
                    <option>전북은행</option>
                    <option>경남은행</option>
                    <option>중소기업은행</option>
                    <option>한국산업은행</option>
                    <option>국민은행</option>
                    <option>신한은행</option>
                    <option>농협</option>
                    <option>하나은행</option>
                    <option>수협은행</option>
                    <option>카카오뱅크</option>
                    <option>주식회사 케이뱅크</option>
                    <option>토스뱅크 주식회사</option>
                    <option>기타</option>
                </select>
            </div>
            <hr>
            <input type="submit" value="회원가입 완료하기">
        </form>
    </div>
    <div class="bottom">
    </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth.js'
import { ref } from 'vue'
import axios from 'axios'

const store = useAuthStore()
const warning = ref('비밀번호가 일치하지 않습니다.')

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const email = ref('')
const nickname = ref('')
const address = ref('')
const gender = ref('')
const birthday = ref('')
const interest = ref('')
const married_period = ref('')
const saving_target_period = ref('')
const main_bank = ref('')
const couple_nickname = ref('')
const couple_birthday = ref('')


const showWarning = ref(false);
const handlePasswordInput = () => {
    showWarning.value = false; // 입력 시 warning 숨기기
};

const signUp = function () {
    const payload = {
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
        couple_birthday: couple_birthday.value,
    }
    store.signUp(payload)
}

const checkMsg = ref('')
const isPassCheckId = ref(false)
const checkUserID = function () {
    if (!username.value) {
        checkMsg.value = "아이디를 입력하세요."
        isPassCheckId.value = false
    } else {
        axios({
            method: 'post',
            url: `${store.URL}/accounts/checkUserID/`,
            data: {
                username: username.value
            }
        })
            .then((res) => {
                if (res.data.isExist) {
                    isPassCheckId.value = false
                    checkMsg.value = "이미 존재하는 아이디입니다"
                } else {
                    isPassCheckId.value = true
                    checkMsg.value = "사용할 수 있는 아이디입니다"
                }
            })
            .catch((err) => {
                console.log(err)
            })
    }
}

</script>

<style scoped>
.essentialss {
    color: rgb(223, 69, 69);
    font-weight: bold;
}

.centered {
    margin-top: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    /* 화면 전체 높이에 해당하는 수치 */
    flex-direction: column;
    /* Flexbox의 방향을 수직(column)으로 설정 */
}

h1 {
    margin: 0%;
}

h4 {
    margin: 2%;
}

/* .bottom {
    margin-bottom: 20%;
} */
</style>