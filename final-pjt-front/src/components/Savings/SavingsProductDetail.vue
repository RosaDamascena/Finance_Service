<!-- SavingsProductDetail.vue -->
<template>
    <div class="container mt-5">
        <h1 class="mb-4">적금 상세 정보</h1>
        <div class="card mb-4 p-4 shadow">
            <h4 class="mb-4">No. {{ store.detailSP.id }}</h4>
            <p>금융 상품 코드 : {{ store.detailSP.fin_prdt_cd }}</p>
            <p>상품명 : {{ store.detailSP.fin_prdt_nm }}</p>
            <p>은행 : {{ store.detailSP.kor_co_nm }}</p>  
            <button @click="goBank(store.detailSP.kor_co_nm)" class="btn btn-primary">홈페이지</button>
        </div>
        <div class="card mb-4 p-4 shadow">
            <h4>상세 정보</h4>
            <hr>
            <h5>만기 후 이자율</h5>
            <p v-for="(line, index) in mtrtIntLines" :key="index">{{ line }}</p>
        </div>
        <div class="card mb-3">
            <div class="card-body">
                <div ref="scrollArea" style="max-height: 400px; overflow-y: auto;">
                <ul class="list-group">
                    <li 
                    v-for="savingsComment in store.savingsComments"
                    :key="savingsComment.id"
                    class="list-group-item d-flex justify-content-between align-items-center border-bottom"
                    >
                    <div class="d-flex align-items-center">
                        <span class="badge bg-primary me-2">{{ savingsComment.user }}</span>
                        <span class="text-break">{{ savingsComment.content }}</span>
                    </div>
                    <button v-if="savingsComment.user === authStore.userdata.userid" @click = "deleteSavingsComment(savingsComment.id)" class="btn btn-sm btn-danger">삭제</button>
                    </li>
                </ul>
                </div>
                <form @submit.prevent="submitComment" class="d-flex align-items-center mt-3">
                <div class="flex-grow-1 me-2">
                    <input v-model="comment" type="text" placeholder="댓글을 입력하세요" class="form-control" />
                </div>
                <div>
                    <input type="submit" value="제출" class="btn btn-secondary">
                </div>
                </form>
            </div>
        </div>
        <div>
            <button @click="goBack" class="btn btn-dark">뒤로가기</button>
        </div>
    </div>
</template>


<script setup>
    import { ref, onMounted , computed} from 'vue'
    import { useRoute, useRouter } from 'vue-router'
    import { FinanceProductsStore } from '@/stores/bank.js'
    import { useAuthStore } from '@/stores/auth.js'
    
    const router = useRouter()
    const route = useRoute()
    const id = ref(route.params.id)
    const store = FinanceProductsStore()
    const authStore = useAuthStore()
    const comment = ref('')

    onMounted(() => {
        store.savingsProductsDetail(id.value)
        store.getSavingsComments(id.value)
    })

    const mtrtIntLines = computed(() => {
        if (store.detailSP && store.detailSP.mtrt_int) {
            return store.detailSP.mtrt_int.split('\n')
        }
        return []
    })

    const goBack = () => {
        router.go(-1)
    }

    const goBank = (bankName) => {
        const link = store.searchBankLink(bankName)
        if (link) {
            window.open(link, '_blank')
        }
    }

    //댓글
    const submitComment = async () => {
        const payload = {
            comment: comment.value,
        }
        await store.createSavingsComment(payload, id.value)
        comment.value = ''
        await store.getSavingsComments(id.value)
    }

    const deleteSavingsComment = async (commentId) => {
        await store.deleteSavingsComment(id.value, commentId)
        await store.getSavingsComments(id.value)
    }
</script>

<style scoped>

</style>