<!-- <template>
    <div>

    </div>
</template>

<script setup>

const today = new Date()
const dday = new Date()
const timeGap = dday.getTime() - today.getTime()

</script>

<style scoped>

</style> -->
<template>
    <div class="container">
        <div style="text-align:center;">
        <p style="margin:3%"> D-DAY</p>
        <!-- <p style="font-size: 5.4vw; margin:0%"> D-DAY</p> -->
        
        </div>
    </div> 
    <!-- <h2> {{ userI.saving_target_period }} </h2> -->
    <!-- <input type="text" class="datepicker" readonly="true" autofocus /> -->
    <!-- <input class="datepicker" /> -->
    <div>
        <h4> {{ dateString }} 에서 
        <input type ='text' class=datepicker /> {{ goalDate }} 까지 </h4>
        <h1 style="margin:0%"> {{ dday }}일 남았습니다! </h1>
    </div>
</template>
  
<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useAuthStore } from '@/stores/auth.js'
import Datepicker from 'vue3-datepicker'
// import { format, compareAsc} from 'date-fns'
import { RouterLink, useRouter } from 'vue-router'
// import dayjs from 'dayjs'



// $.datepicker.setDefaults({
//     dateFormat: 'yy-mm-dd',
//     prevText: '이전 달',
//     nextText: '다음 달',
//     monthNames: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
//     monthNamesShort: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
//     dayNames: ['일', '월', '화', '수', '목', '금', '토'],
//     dayNamesShort: ['일', '월', '화', '수', '목', '금', '토'],
//     dayNamesMin: ['일', '월', '화', '수', '목', '금', '토'],
//     showMonthAfterYear: true,
//     yearSuffix: '년'
// });
const goalDate = ref(null)

$(function () {
    $('.datepicker').datepicker({
        showOn: "both",
        buttonImage:  "/assets/button.png",
        buttonImageOnly: true,
        dateFormat: 'yy-mm-dd',
        prevText: '이전 달',
        nextText: '다음 달',
        monthNames: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
        monthNamesShort: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
        dayNames: ['일', '월', '화', '수', '목', '금', '토'],
        dayNamesShort: ['일', '월', '화', '수', '목', '금', '토'],
        dayNamesMin: ['일', '월', '화', '수', '목', '금', '토'],
        showMonthAfterYear: true,
        yearSuffix: '년',
        onSelect: function(dateText, dateString) {
            goalDate.value = dateText;
            updateDday()}
    });
})

const today = new Date();

const year = today.getFullYear();
const month = ('0' + (today.getMonth() + 1)).slice(-2);
const day = ('0' + today.getDate()).slice(-2);

const dateString = year + '-' + month  + '-' + day;

console.log(goalDate);
console.log(dateString);

const dday = ref()

const updateDday = () => {
    if (goalDate.value) {
        const date1 = new Date(goalDate.value);
        const date2 = new Date(dateString);

        const diffTime = date1.getTime() - date2.getTime()
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

        dday.value = diffDays;}
        else {
            dday.value = 0;
        }
    }

// const target_period = parseInt(goalDate.value)

//  현재 날짜 구하는 함수 
// function getToday() {
//     const today = new Date();
//     // 월은 0부터 시작하므로 실제 월에는 1을 더해줍니다.
//     const year = today.getFullYear();
//     const month = today.getMonth() + 1;
//     const day = today.getDate();
//     return `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`;
// }




// // 디데이 계산하는 함수 
// function calculateDday(selectedDate) {
//     const today = new Date(getToday());
//     const selected = new Date(selectedDate);
//     const timeDiff = selected.getTime() - today.getTime(); // 선택한 날짜와 현재 날짜와의 시간 차이 (밀리초 단위)

//     const dayDiff = Math.floor(timeDiff / (1000 * 60 * 60 * 24)); // 밀리초를 날짜로 변환

//     return dayDiff;
// }

// const getDateDiff = (d1, d2) => {
//   const date1 = new Date(d1);
//   const date2 = new Date(d2);
  
//   const diffDate = date1.getTime() - date2.getTime();
  
//   return Math.abs(diffDate / (1000 * 60 * 60 * 24)); // 밀리세컨 * 초 * 분 * 시 = 일
// }


// daypicker에서 선택한 날짜
// const selectedDate = ref(null);

// watch(selectedDate, (newSelectedDate) => {
//     if (newSelectedDate !== null) {
//         const dDay = calculateDday(newSelectedDate);
//         console.log(`D-Day: ${dDay}`);
//     }
// });
// watchEffec
// var daySpinnerView = datePickerView.findViewById < View > (Resources.getSystem().getIdentifier("day", "id", "android"))
// var monthSpinnerView = datePickerView.findViewById < View > (Resources.getSystem().getIdentifier("month", "id", "android"))
// var yearSpinnerView = datePickerView.findViewById < View > (Resources.getSystem().getIdentifier("year", "id", "android"))

// var dayEditText = daySpinnerView.findViewById(Resources.getSystem().getIdentifier("numberpicker_input", "id", "android")
// function getDate( element ) {
//     var date;
//     var dateFormat = "yy-mm-dd";
//     try {
//       date = $.datepicker.parseDate( dateFormat, element.value );
//     } catch( error ) {
//       date = null;
//     }
//     return date;
//  }
// const goalDate = getDate()
// console.log(goalDate)

// targetTime = "2022-12-25-13:30:00";
// document.write("<span id=countSpan></span>");
// targetCount = targetTime.split("-")[1] + "-" + targetTime.split("-")[2] + "-" + targetTime.split("-")[0] + "-" + targetTime.split("-")[3];
// function countInterval() {
//     countTime = new Date(targetCount) - new Date();
//     countDay = Math.floor(countTime / (1000 * 60 * 60 * 24)) < 1 ? "" : Math.floor(countTime / (1000 * 60 * 60 * 24)) + "<span>일</span> ";
//     countHour = ("0" + Math.floor(countTime % (1000 * 60 * 60 * 24) / (1000 * 60 * 60))).slice(-2) + ":";
//     countMinute = ("0" + Math.floor(countTime % (1000 * 60 * 60) / (1000 * 60))).slice(-2) + ":";
//     countSecond = ("0" + Math.floor(countTime % (1000 * 60) / 1000)).slice(-2);
//     if (countTime < 1) {
//         countSpan.innerHTML = "이벤트 종료";
//         clearInterval(countMode);
//     }
//     else countSpan.innerHTML = countDay + countHour + countMinute + countSecond;   
// }
// countInterval();
// countMode = setInterval(countInterval, 1000);


// const router = useRouter()
// const store = useAuthStore()

// const userI = store.userdata


</script>
  
<style scoped>

.ui-datepicker{ font-size: 10px; width: 50px; }
.ui-datepicker select.ui-datepicker-month{ width:30px; font-size: 11px; }

/* .ui-widget-header { border: 0px solid #dddddd; background: #fff; } 

.ui-datepicker-calendar>thead>tr>th { font-size: 14px !important; } 

.ui-datepicker .ui-datepicker-header { position: relative; padding: 10px 0; } 

.ui-state-default,
.ui-widget-content .ui-state-default,
.ui-widget-header .ui-state-default,
.ui-button,
html .ui-button.ui-state-disabled:hover,
html .ui-button.ui-state-disabled:active { border: 0px solid #c5c5c5; background-color: transparent; font-weight: normal; color: #454545; text-align: center; } 

.ui-datepicker .ui-datepicker-title { margin: 0 0em; line-height: 16px; text-align: center; font-size: 14px; padding: 0px; font-weight: bold; } 

.ui-datepicker { display: none; background-color: #fff; border-radius: 4px; margin-top: 10px; margin-left: 0px; margin-right: 0px; padding: 20px; padding-bottom: 10px; width: 300px; box-shadow: 10px 10px 40px rgba(0, 0, 0, 0.1); } 

.ui-widget.ui-widget-content { border: 1px solid #eee; } 

#datepicker:focus>.ui-datepicker { display: block; } 

.ui-datepicker-prev,
.ui-datepicker-next { cursor: pointer; } 

.ui-datepicker-next { float: right; } 

.ui-state-disabled { cursor: auto; color: hsla(0, 0%, 80%, 1); } 

.ui-datepicker-title { text-align: center; padding: 10px; font-weight: 100; font-size: 20px; } 

.ui-datepicker-calendar { width: 100%; } 

.ui-datepicker-calendar>thead>tr>th { padding: 5px; font-size: 20px; font-weight: 400; } 

.ui-datepicker-calendar>tbody>tr>td>a { color: #000; font-size: 12px !important; font-weight: bold !important; text-decoration: none;}

.ui-datepicker-calendar>tbody>tr>.ui-state-disabled:hover { cursor: auto; background-color: #fff; } 

.ui-datepicker-calendar>tbody>tr>td { border-radius: 100%; width: 44px; height: 30px; cursor: pointer; padding: 5px; font-weight: 100; text-align: center; font-size: 12px; } 

.ui-datepicker-calendar>tbody>tr>td:hover { background-color: transparent; opacity: 0.6; } 

.ui-state-hover,
.ui-widget-content .ui-state-hover,
.ui-widget-header .ui-state-hover,
.ui-state-focus,
.ui-widget-content .ui-state-focus,
.ui-widget-header .ui-state-focus,
.ui-button:hover,
.ui-button:focus { border: 0px solid #cccccc; background-color: transparent; font-weight: normal; color: #2b2b2b; } 

.ui-widget-header .ui-icon { background-image: url('/assets/btns.png'); } 

.ui-icon-circle-triangle-e { background-position: -20px 0px; background-size: 36px; } 

.ui-icon-circle-triangle-w { background-position: -0px -0px; background-size: 36px; } 

.ui-datepicker-calendar>tbody>tr>td:first-child a { color: red !important; } 

.ui-datepicker-calendar>tbody>tr>td:last-child a { color: #0099ff !important; } 

.ui-datepicker-calendar>thead>tr>th:first-child { color: red !important; } 

.ui-datepicker-calendar>thead>tr>th:last-child { color: #0099ff !important; } 

.ui-state-highlight,
.ui-widget-content .ui-state-highlight,
.ui-widget-header .ui-state-highlight { border: 0px; background: #f1f1f1; border-radius: 50%; padding-top: 10px; padding-bottom: 10px; } 

.inp { padding: 10px 10px; background-color: #f1f1f1; border-radius: 4px; border: 0px; } 

.inp:focus { outline: none; background-color: #eee; }  */


</style>
  