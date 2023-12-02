<template>
  <div class="container mt-5">
    <div class="withdrawal-container d-flex justify-content-center align-items-center align-items-center">
      <div class="card rounded p-3" style="width: 40rem;">
        <div class="card-body text-center">
          <h5 class="card-title">회원탈퇴</h5>
          <form>
            <div class="mb-3 mx-3">
              <label for="password1" class="form-label">현재 비밀번호</label>
              <input type="password" id="password1" v-model="password1" class="form-control">
            </div>
            <div class="mb-3 mx-3">
              <label for="password2" class="form-label">현재 비밀번호 확인</label>
              <input type="password" id="password2" v-model="password2" class="form-control">
            </div>
            <button type="button" @click='deleteAccount' class="btn btn-warning w-100">확인</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
  

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const store = useAuthStore()
const password1 = ref('')
const password2 = ref('')

const deleteAccount = function () {
  if (password1.value === password2.value) {
    const confirmed = confirm("정말로 회원탈퇴를 진행하시겠습니까?") // 확인 창 표시
    if (confirmed) {
    const payload = {
      password1: password1.value
      }
      store.byebye(payload)
    }
  }
  else {
    console.error(error)
    alert('비밀번호가 일치하지 않습니다.')
  }
}
</script>

<style scoped>

</style>