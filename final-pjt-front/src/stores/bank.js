// stores/bank.js
import axios from "axios"
import { ref } from "vue"
import { defineStore } from "pinia"
import { useAuthStore } from "@/stores/auth.js"



export const FinanceProductsStore = defineStore('financeProducts', () => {
    const store = useAuthStore()
    const depositProductsList = ref([])
    const savingsProductsList = ref([])
    const detailDP = ref([])
    const detailSP = ref([])
    // const likeDeposit = ref([])
    // const likeSavings = ref([])
    const API_URL = "http://127.0.0.1:8000/api/v1"

    const depositProducts = () => {
        axios({
            method: 'get',
            url: `${API_URL}/deposit_products/`,
        })
        .then(res => depositProductsList.value = res.data)
        .catch(err => console.log(err))
    }

    const depositProductsDetail = (id) => {
        axios ({
            method: 'get',
            url: `${API_URL}/deposit_products/${id}/`,
        })
        .then(res => detailDP.value = res.data)
        .catch(err => console.log(err))
    }

    const savingsProducts = () => {
        axios({
            method: 'get',
            url: `${API_URL}/savings_products/`,
        })
        .then(res => savingsProductsList.value = res.data)
        .catch(err => console.log(err))
    }

    const savingsProductsDetail = (id) => {
        axios ({
            method: 'get',
            url: `${API_URL}/savings_products/${id}/`,
        })
        .then(res => detailSP.value = res.data)
        .catch(err => console.log(err))
    }

    const bankLink = ref([
        {
            "bank_name": "신한은행",
            "bank_url": "https://bank.shinhan.com/index.jsp#020105020000",
        },
        {
            "bank_name": "우리은행",
            "bank_url": "https://spot.wooribank.com/pot/Dream?withyou=PODEP0001",
        },
        {
            "bank_name": "대구은행",
            "bank_url": "https://www.dgb.co.kr/com_ebz_fpm_sub_main.jsp",
        },
        {
            "bank_name": "광주은행",
            "bank_url": "https://www.kjbank.com/ib20/mnu/FPMDPTR030000",
        },
        {
            "bank_name": "제주은행",
            "bank_url": "https://www.e-jejubank.com/HomeFinanceMallDeposit.do",
        },
        {
            "bank_name": "한국스탠다드차타드은행",
            "bank_url": "https://www.standardchartered.co.kr/np/kr/pl/se/SavingList.jsp?ptfrm=HIN.KOR.INTRO.mega.korPerA1_1&id=list1",
        },
        {
            "bank_name": "부산은행",
            "bank_url": "https://www.busanbank.co.kr/ib20/mnu/FPM00001",
        },
        {
            "bank_name": "전북은행",
            "bank_url": "https://www.jbbank.co.kr/",
        },
        {
            "bank_name": "경남은행",
            "bank_url": "https://www.knbank.co.kr/ib20/mnu/BHPFIS000000000",
        },
        {
            "bank_name": "중소기업은행",
            "bank_url": "https://mybank.ibk.co.kr/uib/jsp/index.jsp",
        },
        {
            "bank_name": "한국산업은행",
            "bank_url": "https://banking.kdb.co.kr/bp/index.jsp",
        },
        {
            "bank_name": "국민은행",
            "bank_url": "https://obank.kbstar.com/quics?page=C030037&QSL=F&_ga=2.196160940.1629055220.1700470410-794371171.1700030088#loading",
        },
        {
            "bank_name": "농협은행주식회사",
            "bank_url": "https://smartmarket.nonghyup.com/servlet/SFMN0001R.view",
        },
        {
            "bank_name": "하나은행",
            "bank_url": "https://www.kebhana.com/cont/mall/index.jsp",
        },
        {
            "bank_name": "수협은행",
            "bank_url": "https://www.suhyup-bank.com/",
        },
        {
            "bank_name": "주식회사 케이뱅크",
            "bank_url": "https://www.kbanknow.com/ib20/mnu/FPMDPT130000",
        },
        {
            "bank_name": "주식회사 카카오뱅크",
            "bank_url": "https://www.kakaobank.com/products/withdrawal",
        },
        {
            "bank_name": "토스뱅크 주식회사",
            "bank_url": "https://www.tossbank.com/product-service/savings/time-deposit",
        },
    ])

    const searchBankLink = (bankname) => {
        const bank = bankLink.value.filter(bank => bank.bank_name.includes(bankname))
        return bank.length > 0 ? bank[0].bank_url : ''
    }

    // 상품 하나에 대한 모든 댓글 전체 조회
    const depositComments = ref([])

    const getDepositComments = function (id, articleId) {
        axios({
            method:'get',
            url: `${API_URL}/deposit_products/${id}/comments/`,
            headers: {
                Authorization:`Token ${store.token}`,
            }
        })
            .then(res => depositComments.value = res.data)
            .catch(err => console.log(err))
        // console.log(depositComments.value)
        }
        

    const createDepositComment = function (payload, id) {
        axios({
          method: 'post',
          url: `${API_URL}/deposit_products/${id}/comments/`,
          headers:{ 
            Authorization: `Token ${store.token}`
          },
          data:{
            content : payload.comment,
          }

        })
          .then((res) => {
            depositComments.value.push(res.data)
          })
          .catch((err)=>{
            console.log(err)
          })
        // console.log(depositComments.value[0])
    }
    
    //댓글 삭제
    const deleteDepositComment = function(id, commentId){
        axios({
          method: 'delete',
          url:`${API_URL}/deposit_products/${id}/comments/${commentId}/`,
          headers: {
            Authorization:`Token ${store.token}`
            },
        })
        .then((res)=>{
          console.log(commentId, '----- delete -----')
        })
        .catch((err)=>{ 
          console.log(err)
        })
    }

    // 상품 하나에 대한 모든 댓글 전체 조회
    const savingsComments = ref([])

    const getSavingsComments = function (id, articleId) {
        axios({
            method:'get',
            url: `${API_URL}/savings_products/${id}/comments/`,
            headers: {
                Authorization:`Token ${store.token}`,
            }
        })
            .then(res => savingsComments.value = res.data)
            .catch(err => console.log(err))
        // console.log(depositComments.value)
        }
        

    const createSavingsComment = function (payload, id) {
        axios({
          method: 'post',
          url: `${API_URL}/savings_products/${id}/comments/`,
          headers:{ 
            Authorization: `Token ${store.token}`
          },
          data:{
            content : payload.comment,
          }

        })
          .then((res) => {
            savingsComments.value.push(res.data)
          })
          .catch((err)=>{
            console.log(err)
          })
        // console.log(depositComments.value[0])
    }
    
    //댓글 삭제
    const deleteSavingsComment = function(id, commentId){
        axios({
          method: 'delete',
          url:`${API_URL}/savings_products/${id}/comments/${commentId}/`,
          headers: {
            Authorization:`Token ${store.token}`
            },
        })
        .then((res)=>{
          console.log(commentId, '----- delete -----')
        })
        .catch((err)=>{ 
          console.log(err)
        })
    }

    const likedDP = ref([])
    const likedDepositProducts = function () {
        axios({
            method:'get',
            url: `${API_URL}/user/liked_deposit_products/`,
            headers: {
                Authorization:`Token ${store.token}`,
            }
        })
           .then(res => likedDP.value = res.data)
           .catch(err => console.log(err))
    }

    const likedSP = ref([])
    const likedSavingsProducts = function () {
        axios({
            method:'get',
            url: `${API_URL}/user/liked_savings_products/`,
            headers: {
                Authorization:`Token ${store.token}`,
            }
        })
          .then(res => likedSP.value = res.data)
          .catch(err => console.log(err))
    }

    return { 
        depositProductsList, depositProducts, detailDP, detailSP,
        depositProductsDetail, searchBankLink, bankLink, 
        savingsProductsList, savingsProducts, savingsProductsDetail, 
        createDepositComment, getDepositComments, deleteDepositComment, depositComments, 
        createSavingsComment, getSavingsComments, deleteSavingsComment, savingsComments,
        likedDP, likedDepositProducts, likedSP, likedSavingsProducts
    }

}, {persis:true})