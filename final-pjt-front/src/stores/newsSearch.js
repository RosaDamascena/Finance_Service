import { defineStore } from 'pinia';
import axios from 'axios';

export const useArticleStore = defineStore('financeProducts', () => {
  const API_URL = 'http://127.0.0.1:8000/api/v1'; // 백엔드 API URL

  const fetchArticles = async (query) => {
    try {
      const response = await axios.get(`${API_URL}/news/search_news/?query=${query}`);
      if (response.status === 200) {
        // 기사 데이터를 반환합니다.
        return response.data;
      } else {
        throw new Error('Failed to fetch articles');
      }
    } catch (error) {
      console.error('Error fetching articles:', error);
      throw error;
    }
  }

  return { fetchArticles, };
}, { persist: true });



// export const useArticleStore = defineStore('articles', {
//   state: () => ({
//     articles: [],
//     API_URL: 'https://openapi.naver.com/v1/search/news',
//     client_id: 'zuupf4b56FrdfO8TVHfO', // 네이버 API 클라이언트 ID 입력
//     client_secret: 'sulBZ4u2ZD', // 네이버 API 클라이언트 시크릿 입력
//   }),

//   actions: {
//     async fetchArticles(query) {
//       try {
//         const encText = encodeURIComponent(query)
//         const headers = {
//           'X-Naver-Client-Id': this.client_id,
//           'X-Naver-Client-Secret': this.client_secret,
//         }
//         const response = await axios.get(`${this.API_URL}?query=${encText}`, {
//           headers: headers,
//         })
//         if (response.status === 200) {
//           this.articles = response.data.items || [] // 응답이 'items' 배열을 포함하는 것으로 가정합니다
//         } else {
//           console.error('기사를 가져오는데 실패했습니다:', response.status)
//         }
//       } catch (error) {
//         console.error('기사를 가져오는 도중 오류가 발생했습니다:', error)
//       }
//     },
//   },
// })

