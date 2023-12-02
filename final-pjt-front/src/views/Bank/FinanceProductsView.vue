<template>
    <div class="mb-5 container">
        <h1>금융 상품 조회</h1>
    </div>
    <div class="d-flex justify-content-center">
        <div class="d-flex flex-wrap gap-3">
            <div
            v-for="(product, index) in products"
            :key="index"
            class="card text-center m-2"
            >
            <div class="card-body d-flex flex-column align-items-center justify-content-center">
                <img
                :src="product.imagePath"
                class="card-img-top"
                :alt="product.altText"
                >
                <h5 class="card-title mt-3">{{ product.title }}</h5>
                <button class="btn btn-primary mt-3" @click="goToProduct(product.routeName)">바로 가기</button>
            </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
  import { useRouter } from 'vue-router'
  import depositImage from '@/assets/bank/deposit.png'
  import savingsImage from '@/assets/bank/savings.png'
  import recommendImage from '@/assets/bank/recommend.png'
  
  const router = useRouter();
  
  const products = [
    {
      title: '정기예금',
      routeName: 'depositProducts',
      imagePath: depositImage,
      altText: '정기예금',
    },
    {
      title: '적금',
      routeName: 'savingsProducts',
      imagePath: savingsImage,
      altText: '적금',
    },
    {
      title: '추천 상품',
      routeName: 'productsRecommendation',
      imagePath: recommendImage,
      altText: '추천 상품',
    },
  ]
  
  const goToProduct = (routeName) => {
    router.push({ name: routeName })
  }
</script>
  
<style scoped>
  .card {
    width: 310px;
    height: 420px;
    cursor: pointer;
    transition: transform 0.3s ease-in-out;
    
  }

  .card_body {
    background-color: white !important;
  }
  
  .card:hover {
    transform: scale(1.05);
  }

  .card-title {
    margin-bottom: 0;
  }
  
  .card-img-top {
    width: 80%;
    height: 80%;
    object-fit: contain;
  }
  
  .btn-primary {
    margin-top: 10px;
  }
</style>
