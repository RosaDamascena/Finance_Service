import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { ko } from 'date-fns/locale'

const router = useRouter()

// export const useAuthStore = defineStore('auth', () => {
//   name: 'App',
//   components: {
//       Datepicker,
//   },
//   setup() {
//       const picked = ref(new Date())
//       const locale = reactive(ko)
//       const inputFormat = ref('yyyy-MM-dd')

//       return {
//           picked,
//           locale,
//           inputFormat,
//       }
//   }
// })