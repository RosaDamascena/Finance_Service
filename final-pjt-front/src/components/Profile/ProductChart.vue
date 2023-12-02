<template>
    <div>
        <!-- <h3>찜한 상품 리스트와 상품기간별 최저, 최고금리차트</h3> -->
    </div>
    <div>
  <Bar :data="data" :options="options" />
      
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { FinanceProductsStore } from '@/stores/bank.js'
// http://127.0.0.1:8000/api/v1/deposit_products/
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)


const store = FinanceProductsStore()
const chartdata1 = ref([])


const loadedCharData = computed(() => {
    return chartdata1.value
})

async() => {
    await store.depositProducts()
    chartdata1.value = store.depositProductsList.intr_rate
    console.log(chartdata1.value)
}



const data = {
  labels: [
    '6개월',
    '12개월',
    '24개월',
    '36개월',
    ],
  datasets: [
    {
      label: '저축금리',
      backgroundColor: '#FFE3BB',
    //   data: [chartdata1['6개월'], chartdata1['12개월'], chartdata1['24개월'], chartdata1['36개월']],
      data: [3, 5, 1, 4],  
    },
    {
      label: '최고우대금리',
      backgroundColor: '#B4BDFF',
      data: [3, 8, 5, 4],    

    }
  ],
};

const options = {
  type: 'bar',
  data: data,
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  },
};
</script>

<style scoped>

</style>