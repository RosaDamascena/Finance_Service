<template>
  <div class="bottom">
    <div class="container container-custom">
      <div class="row d-flex justify-content-between">
        <div class="col-3">
           <SideBarView />
        </div>
        <div class="col-8">
          <MainPageView />
        </div>
      </div>
      <!-- <iframe src="http://free.timeanddate.com/clock/i94e0l4y/n5096/tlkr47/fn6/fs17/fcffd28f/tc83a2ff/pct/ftb/blcfff/brcfff/btcfff/bbcfff/pa16/tt0/tm1/th2/tb4" frameborder="0" width="243" height="78" allowtransparency="true"></iframe> -->
      
      <!-- <RouterView /> -->
      <hr>
    </div>

  </div>
</template>

<script setup>
  import SideBarView from '@/views/Main/SideBarView.vue'
  import MainPageView from '@/views/Main/MainPageView.vue'
  import UnderBarView from '@/views/Main/UnderBarView.vue'
</script>

<style scoped>
.bottom{
    margin-bottom: 30%;
    margin-top: 2rem;
}

.container-custom {
  max-width: 1500px;
}

</style>