<template>
    <div>
      <h3>개인 맞춤 상품 추천</h3>
    </div>
    <!-- <div
    v-for="product in result" 
    :key="product.id"
    >
    <p>{{ product.fin_prdt_nm }}</p>
    </div> -->
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useAuthStore } from '@/stores/auth.js'
  import { FinanceProductsStore } from '@/stores/bank.js'

//   const store = FinanceProductsStore()
//   const authStore = useAuthStore()
//   const my_bank = ref(authStore.userdata.main_bank)

//   onMounted(() => {
//     authStore.userInfo()
//     store.savingsProducts()
//     store.depositProducts()
//     onClickFilter()
//   })


//   const bankSPFilter = function (my_bank) {
//     const result = []
//     for (const product of store.savingsProductsList) {
//         const saving_list = []
//         if (product.kor_co_nm === my_bank) {
//           saving_list.append(product)
//         }
//         if (saving_list.length != 0) {
//           result.append(saving_list)
//         }
//     }
//     return result
// }

// const bankDPFilter = function (my_bank) {
//     const result = []
//     for (const product of store.depositProductsList) {
//         const saving_list = []
//         if (product.kor_co_nm === bank) {
//           saving_list.append(product)
//         }
//         if (saving_list.length != 0) {
//             result.append(saving_list)
//         }
//     }
//     return result
// }

// const result1 = ref([])
// const result2 = ref([])
// const result = ref([])
// const onClickFilter = function () {
//   result1.value = bankSPFilter(my_bank.value)
//   result2.value = bankDPFilter(my_bank.value)
//   result.append(result1.value)
//   result.append(result2.value)

//   return result
// }


</script> 

<style scoped>

</style>