<!-- SavingsProductsView.vue -->
<template>
    <div class="container">
        <h1>적금 전체 조회</h1>
    </div>
    <hr>
    <div>
        <div class="container">
        <h4 class="mb-3">검색 조건을 입력하세요</h4>
        <hr>
        <form @submit.prevent="onClickFilter">
            <div class="row">
                <div class="col-md-2">
                    <div class="form-group">
                        <label for="bank">은행</label>
                        <select name="bank" id="bank" v-model="bank" class="form-control">
                            <option value="전체 은행">전체 은행</option>
                            <option :value="bk" v-for="bk in bankList">{{ bk }}</option>
                        </select>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="form-group">
                        <label for="interest_type">저축 금리 유형</label>
                        <select name="interest_type" id="interest_type" v-model="interest_type" class="form-control">
                            <option value="전체 금리 유형">전체 금리 유형</option>
                            <option>단리</option>
                            <option>복리</option>
                        </select>
                    </div>
                </div>
                <!-- <div class="col-md-2">
                    <div class="form-group">
                        <label for="term">예치 기간</label>
                        <select name="term" id="term" v-model="term" class="form-control">
                            <option value="전체 기간">전체 기간</option>
                            <option>6</option>
                            <option>12</option>
                            <option>24</option>
                            <option>36</option>
                        </select>
                    </div>
                </div> -->
                <!-- <div class="col-md-3">
                    <div class="form-group">
                        <label for="acc_type">적립 유형</label>
                        <select name="acc_type" id="acc_type" v-model="acc_type" class="form-control">
                            <option value="적립 유형">적립 유형</option>
                            <option>자유적립식 </option>
                            <option>정액정립식</option>
                        </select>
                    </div>
                </div> -->
                <div class="col-md-1 mt-4 d-flex justify-content-center">
                    <button type="submit" class="btn btn-primary">검색</button>
                </div>
            </div>
        </form>
    </div>
    </div>
    <hr>
    <div>
        <button @click="goBack" class="btn btn-dark mb-5">뒤로가기</button>
    </div>
    <hr>
    <body>
        <div>
            <div v-if="result.length > 0">
                <SavingsProductsAll
                    v-for="savingsProduct in result"
                    :key="savingsProduct.id"
                    :savingsProduct="savingsProduct"
                />
            </div>
            <div v-else>
                <p class="text-center">조건에 맞는 결과가 없습니다.</p>
            </div>
        </div>
    </body>
</template>

<script setup>
import SavingsProductsAll from '@/components/Savings/SavingsProducts.vue'
import { ref, onMounted } from 'vue'
import { FinanceProductsStore } from '@/stores/bank.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = FinanceProductsStore()

onMounted(() => {
    store.savingsProducts()
})

const bankList = ['SC제일은행', '경남은행', '광주은행', '국민은행',
    '기업은행', '농협은행', '대구은행', '부산은행', '수협은행', '신한은행',
    '외환은행', '우리은행', '전북은행', '제주은행', '하나은행', '한국산업은행', 
    '한국시티은행']

const bank = ref('전체 은행')
const interest_type = ref('전체 금리 유형')

// 은행, 유형 같이 필터링
const bankTypeFilter = function (bank, interest_type) {
    const result = []
    for (const product of store.savingsProductsList) {
        const saving_list = []
        if (product.kor_co_nm === bank) {
            if (product.intr_rate_type_nm === interest_type) {
                saving_list.push(product)
            }
        }
        if (saving_list.length != 0) {
            result.append(saving_list)
        }
    }
    return result
}

const result = ref([])
const onClickFilter = function () {
if (bank.value === '전체 은행' && interest_type.value === '전체 금리 유형') {
    // 전체 조회
    result.value = store.savingsProductsList
} else if (bank.value !== '전체 은행' && interest_type.value === '전체 금리 유형') {
    // 은행만 필터링
    result.value = store.savingsProductsList.filter((item) => {
        if (item.kor_co_nm === bank.value) {
            return item
        }
    })
} else if (bank.value === '전체 은행' && interest_type.value!== '전체 금리 유형') {
    // 금리 유형만 필터링
    result.value = store.savingsProductsList.filter((item) => {
        if (item.intr_rate_type_nm === interest_type.value) {
            return item
        }
    })
} else {
    // 은행과 유형
    result.value = bankTypeFilter(bank.value, interest_type.value)
}
console.log(result.value)
}

const goBack = () => {
    router.go(-1)
}

</script>

<style scoped>

</style>