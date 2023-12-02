<template>
  <div class="container">
    <!-- <button @click="toggleCalculator" class="btn btn-primary mb-3">{{ isOpen ? '계산기 닫기' : '계산기 열기' }}</button> -->
    <!-- <div v-if="isOpen" class="card"> -->
      <div class="card-body">
        <h3 class="card-title">간편 예적금 계산기</h3>
        <div class="mb-3">
          <label for="type" class="form-label">저축 방식</label>
          <select id="type" v-model="type" class="form-select">
            <option disabled value="">유형을 선택해 주세요</option>
            <option>예금</option>
            <option>적금</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="inputmoney" class="form-label">예치 금액</label>
          <input type="number" id="inputmoney" v-model="inputmoney" :min="0" class="form-control">원
        </div>
        <div class="mb-3">
          <label for="intr_rate_type" class="form-label">이자 방식</label>
          <select id="intr_rate_type" v-model="intr_rate_type" class="form-select">
            <option disabled value="">유형을 선택해 주세요</option>
            <option>단리</option>
            <option>복리</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="save_trm" class="form-label">예금 기간</label>
          <input type="number" id="save_trm" v-model="save_trm" :min="0" class="form-control">(개월)
        </div>
        <div class="mb-3">
          <label for="intr_rate" class="form-label">연이자율</label>
          <input type="number" id="intr_rate" v-model="intr_rate" :min="0" class="form-control">(%)
        </div>
        <div class="mb-3">
          <button @click.prevent="calculator()" class="btn btn-success">계산</button>
        </div>
        <div>
          <p>원금 합계 : {{ calinput.toLocaleString('ko-KR') }}(원)</p>
          <p>세전이자: {{ beforintr.toLocaleString('ko-KR') }}(원)</p>
          <p>이자과세: -{{ taxintr.toLocaleString('ko-KR') }}(원)</p>
          <p>세후 수령액: {{ mymoney.toLocaleString('ko-KR') }}(원)</p>
        </div>
      </div>
    </div>
  <!-- </div> -->
</template>

<script setup>
  import { ref } from 'vue'
  
  const isOpen = ref(false)
  const type = ref('')  //예,적금 형식
  const inputmoney = ref('')  // 예치 금액
  const intr_rate_type = ref('')  // 예치 유형
  const save_trm = ref('')  // 예금 기간
  const intr_rate = ref('')  // 기본금리
  const calinput = ref('')  // 원금 총액
  const beforintr = ref('')  // 세전 이율
  const taxintr = ref('')  // 과세 금액
  const mymoney = ref('')  // 예상 금액
  
  const calculator = function () {
    if (type.value === "예금") {
      if (intr_rate_type.value === "단리") {
        calinput.value = inputmoney.value * (save_trm.value / 12)
        beforintr.value = (calinput.value * (intr_rate.value / 100))
        taxintr.value = (beforintr.value * 0.154)
        mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
      }
      else {
        calinput.value = inputmoney.value * (save_trm.value / 12)
        beforintr.value = (inputmoney.value * ((1+(intr_rate.value/1200))**save_trm.value) - inputmoney.value)
        taxintr.value = (beforintr.value * 0.154)
        mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
      }
    } else { // 적금
      if (intr_rate_type.value === "단리") {
        calinput.value = inputmoney.value * save_trm.value
        beforintr.value = (inputmoney.value * (intr_rate.value / 1200) * (Math.round(((save_trm.value + 1) * save_trm.value) / 2)))
        taxintr.value = (beforintr.value * 0.154)
        mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
      }
      else {
        calinput.value = inputmoney.value * save_trm.value
        beforintr.value = ((inputmoney.value*((1+intr_rate.value/1200)**(save_trm.value+1))) - (inputmoney.value*(1+intr_rate.value/1200))) / (1+intr_rate.value/1200)
        taxintr.value = (beforintr.value * 0.154)               
        mymoney.value = Math.round(calinput.value + beforintr.value - taxintr.value)
      }
    }
  }
  
  const toggleCalculator = function () {
    isOpen.value = !isOpen.value
  }
  
</script>
  
<style scoped>
.card {
  max-width: 500px;
  margin: auto;
}
</style>