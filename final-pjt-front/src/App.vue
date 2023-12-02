
<template>
  <div>
    <div class="container container-custom">
      <div class="row">

        <div class="col-3">
           <SideBarView />
        </div>
        <div class="col-8">
          <MainPageView />
        </div>
      </div>
      <!-- <iframe src="http://free.timeanddate.com/clock/i94e0l4y/n5096/tlkr47/fn6/fs17/fcffd28f/tc83a2ff/pct/ftb/blcfff/brcfff/btcfff/bbcfff/pa16/tt0/tm1/th2/tb4" frameborder="0" width="243" height="78" allowtransparency="true"></iframe> -->
      
      <header>
        <div>
          <nav>
            <UnderBarView />
          </nav>
        </div>
      </header>

      <!-- <MainView /> -->
      <RouterView />
      
    </div>

  </div>
  <footer class="footer bg-primary-subtle p-5 mt-5" style="height: 40rem;">
    <div class="contact-info">
      <div>
        <h3> 제작자 </h3>
        <hr>
        <p><i class="fas fa-people-carry" style="color: #092f71;"></i> 조혜원 </p>
        <p><i class="far fa-envelope-open"></i> Email : 01051910573@gmail.com</p>
        <p><i class="fas fa-mobile-alt"></i> Phone : 010-5191-0573</p>
      </div>
      <div>
       
        <hr>
        <p><i class="fas fa-people-carry" style="color: #092f71;"></i> 한성주 </p>
        <p><i class="far fa-envelope-open"></i> Email : hsj990604@gmail.com</p>
        <p><i class="fas fa-mobile-alt"></i> Phone : 010-5636-4852</p>
      </div>
      <hr>
      <hr>
      <hr>
        <!-- Add more contact information as needed -->
        <div class="copyright">
            <p>&copy; 2023 FortuneTree. All rights reserved.</p>
        </div>
    </div>

</footer>


</template>

<script setup>
import { RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'
import UnderBarView from '@/views/Main/UnderBarView.vue'

</script>

<style scoped>
nav {
  background-color: #83A2FF;
  position: fixed;
  height: 7rem;
  padding-left: 1.3rem;
  top: 90%;
  left: 0;
  /* 항상 젤 위에 위치하게 하기 위해서 z-index */
  z-index: 1000;
  width: 100%;
}

.container-custom {
  max-width: 1500px;
}
</style>
