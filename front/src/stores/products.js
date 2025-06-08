import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import api from '@/api/axios'; // 커스텀 axios 인스턴스

export const useProductStore = defineStore(
  'product',
  () => {
    const deposits = ref();
    const savings = ref();
    const annuities = ref();

    // Authorization 포함된 api 인스턴스를 사용
    const fetchDeposit = function () {
      api.get('products/deposit-list/')
        .then(res => {
          deposits.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };

    const fetchSaving = function () {
      api.get('products/saving-list/')
        .then(res => {
          savings.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };

    const fetchAnnuity = function () {
      api.get('products/annuity-list/')
        .then(res => {
          annuities.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };

    const bestDeposit = computed(() => {
      if (!deposits.value || deposits.value.length === 0) {
        return null;
      }

      return deposits.value
        .filter(
          deposit =>
            deposit.deposit_like_users && deposit.deposit_like_users.length > 0,
        )
        .reduce(
          (max, deposit) =>
            deposit.deposit_like_users.length > max.deposit_like_users.length
              ? deposit
              : max,
          { deposit_like_users: [] },
        );
    });

    const bestSaving = computed(() => {
      if (!savings.value || savings.value.length === 0) {
        return null;
      }

      return savings.value
        .filter(
          saving =>
            saving.saving_like_users && saving.saving_like_users.length > 0,
        )
        .reduce(
          (max, saving) =>
            saving.saving_like_users.length > max.saving_like_users.length
              ? saving
              : max,
          { saving_like_users: [] },
        );
    });

    const bestAnnuity = computed(() => {
      if (!annuities.value || annuities.value.length === 0) {
        return null;
      }

      return annuities.value
        .filter(
          annuity =>
            annuity.annuity_like_users && annuity.annuity_like_users.length > 0,
        )
        .reduce(
          (max, annuity) =>
            annuity.annuity_like_users.length > max.annuity_like_users.length
              ? annuity
              : max,
          { annuity_like_users: [] },
        );
    });

    return {
      deposits,
      savings,
      annuities,
      fetchDeposit,
      fetchAnnuity,
      fetchSaving,
      bestDeposit,
      bestAnnuity,
      bestSaving,
    };
  },
  { persist: true },
);
