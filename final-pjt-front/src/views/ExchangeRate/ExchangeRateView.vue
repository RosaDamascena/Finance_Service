<template>
    <div class="card">
      <div class="card-header">
        <h4 class="mb-0">환율계산기</h4>
      </div>
      <div class="card-body">
        <div class="row mb-3">
          <div class="col">
            <label for="source-input" class="form-label">FROM</label>
            <select class="form-select" v-if="isToKr" id="source-input" v-model="from">
                    <option value="AED">아랍에미리트 디르함</option>
                    <option value="AUD">호주 달러</option>
                    <option value="BHD">바레인 디나르</option>
                    <option value="BND">브루나이 달러</option>
                    <option value="CAD">캐나다 달러</option>
                    <option value="CHF">스위스 프랑</option>
                    <option value="CNH">중국 위안화</option>
                    <option value="DKK">덴마크 크로네</option>
                    <option value="EUR">유럽연합 유로</option>
                    <option value="GBP">영국 파운드</option>
                    <option value="HKD">홍콩 달러</option>
                    <option value="IDR(100)">인도네시아 루피아</option>
                    <option value="JPY(100)">일본 엔</option>
                    <option value="KRW">한국 원</option>
                    <option value="KWD">쿠웨이트 디나르</option>
                    <option value="MYR">말레이시아 링깃</option>
                    <option value="NOK">노르웨이 크로네</option>
                    <option value="NZD">뉴질랜드 달러</option>
                    <option value="SAR">사우디 리얄</option>
                    <option value="SEK">스웨덴 크로나</option>
                    <option value="SGD">싱가포르 달러</option>
                    <option value="THB">태국 달러</option>
                    <option value="USD">미국 달러</option>
            </select>
            <span v-else>한국 원</span>
            <input type="number" class="form-control mt-2" v-model="fromValue" id="source-input-value">
          </div>
          <div class="col">
            <label for="source-output" class="form-label">TO</label>
            <select class="form-select" v-if="isFromKr" id="source-output" v-model="to">
                    <option value="AED">아랍에미리트 디르함</option>
                    <option value="AUD">호주 달러</option>
                    <option value="BHD">바레인 디나르</option>
                    <option value="BND">브루나이 달러</option>
                    <option value="CAD">캐나다 달러</option>
                    <option value="CHF">스위스 프랑</option>
                    <option value="CNH">중국 위안화</option>
                    <option value="DKK">덴마크 크로네</option>
                    <option value="EUR">유럽연합 유로</option>
                    <option value="GBP">영국 파운드</option>
                    <option value="HKD">홍콩 달러</option>
                    <option value="IDR(100)">인도네시아 루피아</option>
                    <option value="JPY(100)">일본 엔</option>
                    <option value="KRW">한국 원</option>
                    <option value="KWD">쿠웨이트 디나르</option>
                    <option value="MYR">말레이시아 링깃</option>
                    <option value="NOK">노르웨이 크로네</option>
                    <option value="NZD">뉴질랜드 달러</option>
                    <option value="SAR">사우디 리얄</option>
                    <option value="SEK">스웨덴 크로나</option>
                    <option value="SGD">싱가포르 달러</option>
                    <option value="THB">태국 달러</option>
                    <option value="USD">미국 달러</option>
            </select>
            <span v-else>한국 원</span>
          </div>
        </div>
        <button class="btn btn-primary" @click="calculate">환율 계산하기</button>
        <p class="mt-3">
          <span>{{ fromValue }} <strong>{{ from.includes('(100)') ? from.slice(0,3) : from }}</strong></span>
          <span> = </span>
          <span>{{ toValue }} <strong>{{ to.includes('(100)') ? to.slice(0,3) : to }}</strong></span>
        </p>
      </div>
    </div>
  </template>
  
  <!-- ... -->
  

<script setup>
import { ref, computed, watch } from 'vue'
import axios from 'axios'
import { useAuthStore } from '@/stores/auth'

const store = useAuthStore()
const baseURL = `${store.URL}/api/v1/exchange_rate/get/`
// URL 형태 :  http://127.0.0.1:8000/api/v1/exchange_rate/get/?searchDate=2023-10-29&from=CHF&to=CAD
const currentDate = new Date()
const searchDate = ref(currentDate.toISOString().slice(0,10))
const from = ref('')
const fromValue = ref()
const to = ref('')
const toValue = ref()
const rate = ref()
const mod = ref(1)

const isFromKr = computed(() => {
    if (from.value === 'KRW' | from.value === '') {
        return true
    } else {
        to.value = 'KRW'
        return false
    }
})

const isToKr = computed(() => {
    if (to.value === 'KRW' | to.value === '') {
        return true
    } else {
        from.value = 'KRW'
        return false
    }
})

watch(from, (newVal, oldVal) => {
    // console.log(newVal)
    fromValue.value = ''
    toValue.value = ''
    if (['IDR(100)', 'JPY(100)'].includes(newVal)) {
        mod.value = 100
    } else {
        mod.value = 1
    }
})

watch(to, (newVal, oldVal) => {
    // console.log(newVal)
    fromValue.value = ''
    toValue.value = ''
    if (['IDR(100)', 'JPY(100)'].includes(newVal)) {
        mod.value = 100
    } else {
        mod.value = 1
    }
})

watch(fromValue, (newVal, oldVal) => {
    toValue.value = ''
})

const calculate = function() {
    const URL = `${baseURL}?searchDate=${searchDate.value}&from=${from.value}&to=${to.value}`
    console.log(URL)
    axios({
        method: 'get',
        url: URL
        })
        .then((response) => {
            console.log(response)
            const data = response.data
            const idx = data.findIndex((item) => { 
                if (to.value === 'KRW') {
                    return item.cur_unit === from.value
                } else {
                    return item.cur_unit === to.value
                }
            })
            rate.value = parseFloat(data[idx].deal_bas_r.replace(',',''))

            console.log('rate', rate.value)
            console.log('mod', mod.value)
            if (to.value === 'KRW') {
                toValue.value = ((fromValue.value * rate.value) / mod.value).toFixed(2)
            } else {
                toValue.value = ((fromValue.value / rate.value) * mod.value).toFixed(2)
            }

        })
        .catch((error) => {
            console.log(error)
        })
    
}
</script>

<style scoped>

</style>