import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { defineStore } from 'pinia';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

export const useRecommendStore = defineStore(
  'recommend',
  () => {
    const recommendedProducts = ref([]);
    const userStore = useUserStore();
    const router = useRouter();

    const fetchRecommendedProducts = function () {
      axios({
        url: 'http://127.0.0.1:8000/products/recommend-products/',
        method: 'get',
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then(res => {
          recommendedProducts.value = res.data.sort((a, b) => b.r - a.r);
          router.push({ name: 'recommend-list' });
        })
        .catch(err => {
          if (err.message === 'Request failed with status code 500') {
            alert('상품 추천에 필요한 회원 정보가 없습니다.');
            router.push({ name: 'profile', params: { tab: 'moreInfo' } });
          }
        });
    };
    return { recommendedProducts, fetchRecommendedProducts };
  },
  { persist: true },
);
