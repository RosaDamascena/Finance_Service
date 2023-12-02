import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/Main/MainView.vue'
// User
import SignUpView from '@/views/User/SignUpView.vue'
import LoginView from '@/views/User/LogInView.vue'
import ProfileView from '@/views/User/ProfileView.vue'
import ProfileUpdateView from '@/views/User/ProfileUpdateView.vue'

// Bank
import FinanceProductsView from '@/views/Bank/FinanceProductsView.vue'
import DepositProductsView from '@/views/Bank/DepositProductsView.vue'
import SavingsProductsView from '@/views/Bank/SavingsProductsView.vue'
import ProductsRecommendationView from '@/views/Bank/ProductsRocommendationView.vue'
import DepositProductDetail from '@/components/Deposit/DepositProductDetail.vue'
import SavingsProductDetail from '@/components/Savings/SavingsProductDetail.vue'
import ByebyeView from '@/views/User/ByebyeView.vue'


// Exchange
import ExchangeRateView from '@/views/ExchangeRate/ExchangeRateView.vue'


// Map
import findBank from '@/components/Map/findBank.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Main',
      component: MainView,
    },
    {
      path: '/finance_products',
      name: 'financeProducts',
      component: FinanceProductsView,
    },

    // accounts
    {
      path: '/signup/',
      name: 'SignUp',
      component: SignUpView,
    },
    {
      path: "/login/",
      name: "LogIn",
      component: LoginView,
    },

    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
    },

    {
      path: "/profile/update/:username",
      name: "ProfileUpdateView",
      component: ProfileUpdateView,
    },

    {
      path: "/bybyeuser/",
      name: "Byebye",
      component: ByebyeView,
    },

    // 금융 상품 전체 조회 페이지 
    {
      path: '/finance_products/deposit_products',
      name: 'depositProducts',
      component: DepositProductsView,
    },
    {
      path: '/finance_products/savings_products',
      name: 'savingsProducts',
      component: SavingsProductsView,
    },
    // 상품 추천 페이지
    {
      path: '/finance_products/products_recommendation',
      name: 'productsRecommendation',
      component: ProductsRecommendationView,
    },

    // 금융 상품 상세 페이지
    {
      path: '/deposit_product/:id',
      name: 'depositDetail',
      component: DepositProductDetail,
    },
    {
      path: '/savings_product/:id',
      name: 'savingsDetail',
      component: SavingsProductDetail,
    },
    {
      path: '/exchange_rate/',
      name: 'exchangeRate',
      component: ExchangeRateView,
    },
    {
      path: '/find_Bank/',
      name: 'findBank',
      component: findBank,
    },

    
  ]
})


export default router