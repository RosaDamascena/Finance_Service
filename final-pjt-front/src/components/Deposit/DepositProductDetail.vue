<!-- DepositproductDetail.vue -->
<template>
    <div class="container mt-5">
        <h1 class="mb-4">정기예금 상세 정보</h1>
        <div class="card mb-4 p-4 shadow">
            <h4 class="mb-4">No. {{ store.detailDP.id }}</h4>
            <p>금융 상품 코드 : {{ store.detailDP.fin_prdt_cd }}</p>
            <p>상품명 : {{ store.detailDP.fin_prdt_nm }}</p>
            <p>은행 : {{ store.detailDP.kor_co_nm }}</p>  
            <button @click="goBank(store.detailDP.kor_co_nm)" class="btn btn-primary">홈페이지 바로가기</button>
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
                    v-for="(depositComment, index) in store.depositComments"
                    :key="depositComment.id"
                    class="list-group-item d-flex justify-content-between align-items-center border-bottom"
                    >
                    <div class="d-flex align-items-center">
                        <span class="badge bg-primary me-2">{{ depositComment.user.nickname }}</span>
                        <span class="text-break">{{ depositComment.content }}</span>
                    </div>
                    <button v-if="depositComment.user.nickname === authStore.userdata.nickname" @click = "deleteDepositComment(depositComment.id)" class="btn btn-sm btn-danger">삭제</button>
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
            <button @click="goBack" class="btn btn-dark mb-5">뒤로가기</button>
        </div>
    </div>
</template>

<script setup>
        
    import { ref, onMounted , computed , watch} from 'vue'
    import { useRoute, useRouter } from 'vue-router'
    import { FinanceProductsStore } from '@/stores/bank.js'
    import { useAuthStore } from '@/stores/auth.js'
    
    const router = useRouter()
    const route = useRoute()
    const id = ref(route.params.id)
    const store = FinanceProductsStore()
    const authStore = useAuthStore()
    // const articleId = ref(store.detailDP.id)
    const comment = ref('')
    const intr_rate = ref({})
    const intr_rate2 = ref({})
    console.log(id.value)
    console.log(route.params.intr_rate)

    onMounted(async () => {
        await store.depositProductsDetail(id.value)
        await store.getDepositComments(id.value)

        // intr_rate.value = JSON.parse(route.params.intr_rate)
        // intr_rate2.value = JSON.parse(route.params.intr_rate2)
        console.log(intr_rate.value)
    })

    const mtrtIntLines = computed(() => {
        if (store.detailDP && store.detailDP.mtrt_int) {
            return store.detailDP.mtrt_int.split('\n')
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
        await store.createDepositComment(payload, id.value)
        comment.value = ''
        await store.getDepositComments(id.value)
    }

    const deleteDepositComment = async (commentId) => {
        await store.deleteDepositComment(id.value, commentId)
        await store.getDepositComments(id.value)
    }
    

    // const getDepositComments = async () => {
    //     try {
    //         await store.getDepositComments(id.value)
    //         console.log(store.depositComments)
    //     } catch (error) {
    //         console.error(error)
    //     }
    // }

</script>

<style scoped>

</style>