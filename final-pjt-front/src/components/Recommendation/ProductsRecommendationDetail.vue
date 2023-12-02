<template>
    <div>
        <h3>찜한 정기 예금 상품</h3>
        <div class="list-group">
            <a href="#" class="list-group-item list-group-item-action" v-for="(product, index) in store.likedDP" :key="index">
                {{ product.fin_prdt_nm }}
            </a>
        </div>
        <div style="height: 20px;">
        </div>
        <h3>찜한 적금 상품</h3>
        <div class="list-group mb-3">
            <a href="#" class="list-group-item list-group-item-action" v-for="(product, index) in store.likedSP" :key="index">
                {{ product.fin_prdt_nm }}
            </a>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted } from "vue"
    import { useRouter } from "vue-router"
    import { useAuthStore } from "@/stores/auth.js"
    import { FinanceProductsStore } from "@/stores/bank.js"

    const router = useRouter()
    const authStore = useAuthStore()
    const store = FinanceProductsStore()
    
    onMounted(() => {
        store.likedDepositProducts()
        store.likedSavingsProducts()
        console.log(store.likedDP.value)
        console.log(store.likedSP.value)
    })
</script>

<style scoped>

</style>
