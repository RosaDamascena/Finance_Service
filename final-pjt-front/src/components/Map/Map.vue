<template>
  <div id="map"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios'


const lat = 37.54 
const lon = 126.98

const mapKey = import.meta.env.VITE_KAKAOMAP_API_KEY
const restAPIKey = import.meta.env.VITE_KAKAOMAP_REST_API_KEY

let map = null;

const initMap = (lat = 37.54, lon = 126.98) => {
    const container = document.getElementById('map');
    const options = {
        center: new kakao.maps.LatLng(lat, lon),
        level: 8,
    };

    // 지도 객체를 등록합니다.
    // 지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
    map = new kakao.maps.Map(container, options);
};

// Map.vue가 마운트 될 때, initMap() 함수 실행되도록
onMounted(async () => {
    if (window.kakao && window.kakao.maps) {
        initMap();
    } else {
        const script = document.createElement('script');
        /* global kakao */
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${mapKey}&libraries=services`;
        document.head.appendChild(script);
        script.onload = () => kakao.maps.load(initMap);
    }
});

var markers = []

const markBank = function (bankName) {
    console.log(bankName, '을 찾으려고 하는 중')

    // map의 확대, 축소 레벨을 8로 고정
    map.setLevel(8)

    // 현재 지도에 표시된 마커가 있으면, 모두 제거함
    if (markers.length > 0) {
        markers.forEach((item) => {
            item.setMap(null)
        })
    }

    // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
    var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

    // 장소 검색 객체를 생성합니다
    var ps = new kakao.maps.services.Places();

    // 키워드로 장소를 검색합니다
    ps.keywordSearch(bankName, placesSearchCB);

    // 키워드 검색 완료 시 호출되는 콜백함수 입니다
    function placesSearchCB(data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {

            for (var i = 0; i < data.length; i++) {
                displayMarker(data[i]);
            }

        }
        // console.log(markers)
    }

    // 지도에 마커를 표시하는 함수입니다
    function displayMarker(place) {

        // 마커를 생성하고 지도에 표시합니다
        var marker = new kakao.maps.Marker({
            map,
            position: new kakao.maps.LatLng(place.y, place.x)
        });
        markers.push(marker)

        // 마커에 클릭이벤트를 등록합니다
        kakao.maps.event.addListener(marker, 'mouseover', function () {
            // 마커에 마우스를 올리면 장소명 인포윈도우에 표출됩니다
            infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
            infowindow.open(map, marker);
        });
        kakao.maps.event.addListener(marker, 'mouseout', function () {
            // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
            infowindow.close(map, marker);
        });
        // 클릭하면 정보가 뜨도록 (추가해야함)
        kakao.maps.event.addListener(marker, 'click', function () {
            // 마커를 클릭하면 장소명이 해당 장소 확대
            const pos = marker.getPosition()
            map.setLevel(3)
            map.panTo(pos)
        });

    }

}

// 현위치 버튼을 누르면, 지도 중심이 현위치로 이동하도록
const setCenter = function (lat, lon) {
    const moveLatLon = new kakao.maps.LatLng(lat, lon);
    map.setLevel(6)
    // console.log('Map에서', moveLatLon)
    // console.log('Map에서', map)
    // 지도 중심을 이동 시킵니다
    map.setCenter(moveLatLon)

}

// address 넘겨주면, 위경도 검색하고 지도의 중심을 옮기는 함수
const moveSelectedLocation = function (address) {
    // console.log(restAPIKey)
    axios({
        method: 'get',
        url: "https://dapi.kakao.com/v2/local/search/address.json",
        params: {
            'analyze_type': 'similar',
            'page': 1,
            'size': 3,
            'query': address
        },
        headers: { 'Authorization': `KakaoAK ${restAPIKey}` }
    })
        .then((res) => {
            // console.log(res.data.documents[0].address)
            const lat = res.data.documents[0].address.y
            const lon = res.data.documents[0].address.x
            setCenter(lat, lon)

        })
        .catch((err) => {
            console.log(err)
        })

}

defineExpose({
    setCenter, moveSelectedLocation, markBank
})
</script>


<style scoped>
#map {
    margin-top: 20%;
    width: 45rem;
    height: 45rem;
    border-radius: 10px;
    margin: 0 auto;
}
</style>
