<template>
    <div>
        <h1> LOGIN </h1>
        <form @submit.prevent="logIn">
            <div>
                <label for="username">아이디: </label>
                <input type="text" v-model.trim="username">
            </div>
            <div>
                <label for="password">비밀번호: </label>
                <input type="password" v-model.trim="password">
            </div>
            <input type="submit" value="로그인">
        </form>
    </div>
</template>


<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth.js'
const store = useAuthStore()

const username = ref(null)
const password = ref(null)


const logIn = function () {
    const payload = {
        username: username.value,
        password: password.value,
    }
    store.logIn(payload)
}
</script>

<style scoped></style>