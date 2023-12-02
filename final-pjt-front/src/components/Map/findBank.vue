<template>
    <div class="container">
        <h1 class="text-center mb-4">근처 은행 검색</h1>
        <div class="row">
            <div class="col-lg-4">
                <div class="card">
                    <div class="card-body">
                        <div class="search-box m-3 d-flex flex-column justify-content-between align-items-start g-3">
                            <div class="row g-3">
                                <button @click="currentLocation" class="btn btn-primary col-12 mb-3">현위치</button>
                            </div>
                            <hr>
                            <div class="row g-3">
                                <select name="province" id="province" v-model="province" class="form-control col-12 mb-3">  
                                    <option value="" selected disabled hidden>=== 시/도 선택 ===</option>
                                    <option :value="pr" v-for="pr in provinceInput">{{ pr }}</option>
                                </select>
                                <select name="country" id="country" v-model="country" class="form-control col-12 mb-3">
                                    <option value="" selected disabled hidden>=== 구/군 선택 ===</option>
                                    <option :value="ct" v-for="ct in countryInput[prIdx]">{{ ct }}</option>
                                </select>
                                <button @click="selectedLocation(address)" class="btn btn-primary col-12">선택한 지역으로 이동</button>
                            </div>
                            <hr>
                            <div class="row g-3 mt-1">
                                <select name="bank" id="bank" v-model="bank" class="form-control col-12 mb-2">
                                    <option value="" selected disabled hidden>은행 선택</option>
                                    <option :value="bk" v-for="bk in bankList">{{ bk }}</option>
                                </select>
                                <button @click="searchBank(bank)" class="btn btn-primary col-12">은행 검색</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-8">
                <Map ref="mapRef" />
            </div>
        </div>
    </div>
</template>



<!-- <template>
    <div class="container text-center">
        <h1 class="mb-4">근처 은행 검색</h1>
        <div class="search-box mb-5 row d-flex flex-column flex-lg-row justify-content-between align-items-center g-3">
            <button @click="currentLocation" class="btn btn-primary col-sm-5 col-lg-1">현위치</button>
            <div class="row col-lg-7 g-3">
                <select name="province" id="province" v-model="province" class="form-control col-sm-6 col-lg-4">  
                    <option value="" selected disabled hidden>=== 시/도 선택 ===</option>
                    <option :value="pr" v-for="pr in provinceInput">{{ pr }}</option>
                </select>
                <select name="country" id="country" v-model="country" class="form-control col-sm-6 col-lg-4">
                    <option value="" selected disabled hidden>=== 구/군 선택 ===</option>
                    <option :value="ct" v-for="ct in countryInput[prIdx]">{{ ct }}</option>
                </select>
                <button @click="selectedLocation(address)" class="btn btn-success col-lg-4">선택한 지역으로 이동</button>
            </div>
            <div class="row col-lg-3 g-3">
                <select name="bank" id="bank" v-model="bank" class="form-control col-sm-8 col-lg-6">
                    <option value="" selected disabled hidden>은행 선택</option>
                    <option :value="bk" v-for="bk in bankList">{{ bk }}</option>
                </select>
                <button @click="searchBank(bank)" class="btn btn-warning col-sm-4 col-lg-6">은행 검색</button>
            </div>
        </div>
        <Map ref="mapRef" />
    </div>
</template> -->


<script setup>
import Map from '@/components/Map/Map.vue'
import { ref, watch, computed } from 'vue'

const provinceInput = ['서울특별시', '부산광역시', '대구광역시', '인천광역시',
'광주광역시', '대전광역시', '울산광역시', '세종특별자치시',
'경기도', '충청북도', '충청남도', '전라북도', '전라남도',
'경상북도', '경상남도', '제주특별자치도', '강원특별자치도']

const countryInput = {
    0: ['강남구','강동구','강북구','강서구','관악구','광진구','구로구',
    '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구',
    '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구',
    '은평구', '종로구', '중구', '중랑구'],
    1: ['강서구','금정구','기장군','남구','동구','동래구','부산진구','북구','사상구',
    '사하구','서구','수영구','연제구','영도구','중구','해운대구'],
    2: ['군위군','남구','달서구','달성군','동구','북구','서구','수성구','중구'],
    3: ['강화군','계양구','남동구','동구','미추홀구','부평구','서구','연수구','옹진군','중구'],
    4: ['광산구','남구','동구','북구','서구'],
    5: ['대덕구','동구','서구','유성구','중구'],
    6: ['남구','동구','북구','울주군','중구'],
    7: [''],
    8: ['가평군','고양시 덕양구','고양시 일산동구','고양시 일산서구','과천시','광명시','광주시','구리시','군포시','김포시','남양주시','동두천시','부천시','성남시 분당구','성남시 수정구','성남시 중원구','수원시 권선구','수원시 영통구','수원시 장안구','수원시 팔달구','시흥시','안산시 단원구','안산시 상록구','안성시','안양시 동안구','안양시 만안구','양주시','양평군','여주시','연천군','오산시','용인시 기흥구','용인시 수지구','용인시 처인구','의왕시','의정부시','이천시','파주시','평택시','포천시','하남시','화성시'],
    9: ['괴산군','단양군','보은군','영동군','옥천군','음성군','제천시','증평군','진천군','청주시 상당구','청주시 서원구','청주시 청원구','청주시 흥덕구','충주시'],
    10: ['계롱시','공주시','금산군','논산시','당진시','보령시','부여군','서산시','서천군','아산시','예산군','천안시 동남구','천안시 서북구','청양군','태안군','홍성군'],
    11: ['고창군','군산시','김제시','남원시','무주군','부안군','순창군','완주군','익산시','임실군','장수군','전주시 덕진구','전주시 완산구','정읍시','진안군'],
    12: ['강진군','고흥군','곡성군','광양시','구례군','나주시','단양군','목포시','무안군','보성군','순천시','신안군','여수시','영광군','영암군','완도군','장성군','장흥군','진도군','함평군','해남군','화순군'],
    13: ['경산시','경주시','고령군','구미시','김천시','문경시','봉화군','상주시','성주군','안동시','영덕군','영양군','영주시','영천시','예천군','울릉군','울진군','의성군','청도군','청송군','칠곡군','포항시 남구','포항시 북구'],
    14: ['거제시','거창군','고성군','김해시','남해군','밀양시','사천시','산청군','양산시','의령군','진주시','창녕군','창원시 마산합포구','창원시 마산회원구','창원시 성산구','창원시 의창구','창원시 진해구','통영시','하동군','함안군','함양군','합천군'],
    15: ['서귀포시','제주시'],
    16: ['강릉시','고성군','동해시','삼척시','속초시','양구군','양양군','영월군','원주시','인제군','정선군','철원군','춘천시','태백시','평창군','홍천군','화천군','횡성군']
}

const bankList = ['SC제일은행', '경남은행', '광주은행', '국민은행',
    '기업은행', '농협은행', '대구은행', '부산은행', '수협은행', '신한은행',
    '외환은행', '우리은행', '전북은행', '제주은행', '하나은행', '한국산업은행', 
    '한국시티은행']

const province = ref('')
const country = ref('')
const pointInfo = ref(null)
const bank = ref('')

const prIdx = computed(() => {
    // console.log(province.value)
    return provinceInput.findIndex((item) => item === province.value)
})

const address = computed(() => {
    console.log('주소:', province.value + ' ' + country.value)
    return province.value + ' ' + country.value
})

const mapRef = ref(null)

const currentLocation = function () {
    if ("geolocation" in navigator) {
        /* 위치정보 사용 가능 */
        navigator.geolocation.getCurrentPosition((position) => {
            const lat = position.coords.latitude
            const lon = position.coords.longitude
            // console.log(lat, lon, mapRef.value.setCenter)
            mapRef.value.setCenter(lat, lon)
        })
    } else {
        /* 위치정보 사용 불가능 */
        window.alert("위치 정보 사용이 불가능합니다.")
    }

}

const selectedLocation = function (address) {
    // 주소로 위경도 검색 후 지도 중심 이동
    mapRef.value.moveSelectedLocation(address)
    console.log('지도 중심 이동')
}

const searchBank = function (bank) {
    console.log(bank)
    mapRef.value.markBank(bank)
    console.log('선택한 은행 지도에서 마크 표시')
}

</script>


<style scoped>
/* .search-box {
    padding-left: 7rem;
    padding-right: 7rem;
} */
</style>


