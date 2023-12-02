<template>
    <div>
        <h3>경제 지수</h3>
        <ul>
            <li v-for="idx in index">
                <strong>{{ idx.name }}</strong>
                <p>{{ idx.value }}</p>
                <p>{{ idx.fluctuation.value }} // {{ idx.fluctuation.percent }}% </p>
            </li>
            <li v-if="kospi">
                <strong>{{ kospi.name }}</strong>
                <p>{{ kospi.value }}</p>
                <p>{{ kospi.fluctuation.value }} // {{ kospi.fluctuation.percent }}% </p>
            </li>
            <li v-else>
                <strong>코스피</strong>
                <p>코스피 정보를 받아오는 중입니다.</p>
            </li>
        </ul>
    </div>
</template>

<script setup>

const props = defineProps({
    index: Object,
    kospi: Object
})

</script>

<style scoped>

</style>