<!-- DepositProducts.vue -->
<template>
    <div class="card">
        <div class="card-body p-5">
            <h5 class="card-title">{{ depositProduct.fin_prdt_nm }}</h5>
            <p class="card-text">은행명 : {{ depositProduct.kor_co_nm }}</p>
            <p class="card-text">저축 금리 유형: {{ depositProduct.intr_rate_type_nm }}</p>
            <p class="card-text">금리 비교</p>
            <table class="table" border="1">
                <thead>
                    <tr class="table-primary">
                        <th scope="col">기간(개월)</th>
                        <th scope="col">6</th>
                        <th scope="col">12</th>
                        <th scope="col">24</th>
                        <th scope="col">36</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>저축 금리</td>
                        <td>{{ depositProduct.rates['6'].intr_rate }}</td>
                        <td>{{ depositProduct.rates['12'].intr_rate }}</td>
                        <td>{{ depositProduct.rates['24'].intr_rate }}</td>
                        <td>{{ depositProduct.rates['36'].intr_rate }}</td>
                    </tr>
                    <tr>
                        <td>최대 우대 금리</td>
                        <td>{{ depositProduct.rates['6'].intr_rate2 }}</td>
                        <td>{{ depositProduct.rates['12'].intr_rate2 }}</td>
                        <td>{{ depositProduct.rates['24'].intr_rate2 }}</td>
                        <td>{{ depositProduct.rates['36'].intr_rate2 }}</td>
                    </tr>
                </tbody>    
            </table>
            <button class="btn btn-primary" @click="goToDetail(depositProduct)">상품 상세 보기</button>
        </div>
        <div class="card-footer">
            <div @click="toggleLike(depositProduct.fin_prdt_cd)">
                <i v-if="likedResult || isLikedLocally(depositProduct.fin_prdt_cd)" class="fas fa-star" style="color: #f4d81f;"></i>
                <i v-else class="far fa-star"></i>
            </div>
            <div>
                <p>좋아요 수 : {{ count }}</p>
            </div>
        </div>
    </div>
    <br>
</template>


<script setup>
import { useRouter } from 'vue-router'
import { watchEffect, computed, ref } from 'vue'
import { FinanceProductsStore } from '@/stores/bank.js'
import { useAuthStore } from '@/stores/auth.js'

const router = useRouter() 
const store = FinanceProductsStore()
const authStore = useAuthStore()
const likedResult = ref(false)
const count = ref(0)

const props = defineProps({
    depositProduct: Object,
 })

const goToDetail = (product) => {
    router.push({
        name: 'depositDetail',
        params: {
            id: product.fin_prdt_cd,
            intr_rate: product.intr_rate,
            intr_rate2: product.intr_rate2,
            intr_rate_type_nm: product.intr_rate_type_nm,
        }
    })
}

const toggleLike = async (productId) => {
    const res = await authStore.dpLike(productId)
    likedResult.value = res

    const count_dp = await authStore.dpLikeCount(productId)
    count.value = count_dp.count

    // 로컬 스토리지에 좋아요 상태 저장
    saveLikedLocally(productId, res)
    saveLikedCountLocally(productId, count_dp)
}

const saveLikedCountLocally = (productId, count) => {
    // 로컬 스토리지에 좋아요 수를 저장
    const likedCount = JSON.parse(localStorage.getItem('likedCount')) || {}
    likedCount[productId] = count.count
    localStorage.setItem('likedCount', JSON.stringify(likedCount))
}

const getLikedCountLocally = (productId) => {
    // 로컬 스토리지에서 좋아요 수를 가져옴
    const likedCount = JSON.parse(localStorage.getItem('likedCount')) || {}
    return likedCount[productId] || 0
}

const isLikedLocally = (productId) => {
    // 로컬 스토리지에서 좋아요 상태를 가져옴
    const likedProducts = JSON.parse(localStorage.getItem('likedProducts')) || []
    return likedProducts.includes(productId)
}

const saveLikedLocally = (productId, isLiked) => {
    // 로컬 스토리지에 좋아요 상태를 저장
    let likedProducts = JSON.parse(localStorage.getItem('likedProducts')) || []
    if (isLiked) {
        likedProducts.push(productId)
    } else {
        likedProducts = likedProducts.filter(id => id !== productId)
    }
    localStorage.setItem('likedProducts', JSON.stringify(likedProducts))
}

// 페이지 로드 시 로컬 스토리지에서 좋아요 상태를 가져와서 초기화
watchEffect(() => {
    const likedProducts = JSON.parse(localStorage.getItem('likedProducts')) || []
    likedResult.value = likedProducts.includes(props.depositProduct.fin_prdt_cd)
    count.value = getLikedCountLocally(props.depositProduct.fin_prdt_cd)
})

</script>

<style scoped>

</style>

