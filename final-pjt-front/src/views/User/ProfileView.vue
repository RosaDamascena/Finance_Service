<template>
  <div class="bottom">
      <div class="container">
          <div class="row d-flex justify-content-between">
              <div class="col-4">
                  <div class="card">
                      <div class="card-body">
                          <Dday />
                      </div>
                  </div>
                  <div class="card mt-3">
                      <div class="card-body">
                          <PersonalInfo />
                      </div>
                  </div>
              </div>
              <div class="col-8">
                  <Goal />
                  <ProductChart />
              </div>
          </div>
      </div>
  </div>
</template>


<script setup>
import PersonalInfo from '@/components/Profile/PersonalInfo.vue';
import ProductChart from '@/components/Profile/ProductChart.vue';
import Goal from '@/components/Profile/Goal.vue';
import Dday from '@/components/Profile/Dday.vue';
</script>

<style scoped></style>