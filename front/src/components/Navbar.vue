<template>
  <nav
    v-if="
      $route.name !== 'product-detail' &&
      $route.name !== 'login' &&
      $route.name !== 'error' &&
      $route.name !== 'signup'
    "
    class="sticky top-0 z-40 w-full bg-white shadow-sm"
  >
    <div class="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex items-center flex-shrink-0 mb-1">
          <RouterLink :to="{ name: 'home' }">
            <img src="@/assets/wholeicon/pagelogo.png" alt="모두의금융 로고" class="homelogo" />
          </RouterLink>
        </div>
        <div
          class="hidden text-sm select-none md:flex md:items-center md:space-x-6"
        >
          <RouterLink
            :to="{ name: 'deposit' }"
            class="text-gray-600 hover:text-black"
            >예적금 금리 비교</RouterLink
          >
          <RouterLink
            :to="{ name: 'exchange' }"
            class="text-gray-600 hover:text-black"
            >환율 계산기</RouterLink
          >
          <RouterLink
            :to="{ name: 'metal' }"
            class="text-gray-600 hover:text-black"
            >금/은 시세</RouterLink
          >
          <RouterLink
            :to="{ name: 'map' }"
            class="text-gray-600 hover:text-black"
            >은행 지점찾기</RouterLink
          >
          <RouterLink
            :to="{ name: 'recommend' }"
            class="text-gray-600 hover:text-black"
            >상품 추천 서비스</RouterLink
          >
          <RouterLink
            :to="{ name: 'board' }"
            class="text-gray-600 hover:text-black"
            >커뮤니티</RouterLink
          >
          <RouterLink
            :to="{ name: 'InterestSearch' }"
            class="text-gray-600 hover:text-black"
            >영상검색</RouterLink
          >
          <div v-if="isLogin" class="relative">
            <button
              @click="toggleProfileMenu"
              class="text-gray-600 hover:text-black"
            >
              <Profile />
            </button>
            <div
              v-if="isProfileMenuOpen"
              class="absolute z-50 py-2 mt-2 text-sm bg-white border rounded shadow-xl -right-2 w-28"
            >
              <RouterLink
                :to="{ name: 'profile', params: { tab: 'basicInfo' } }"
                class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
                @click="toggleProfileMenu"
              >
                프로필
              </RouterLink>
              <RouterLink
                v-if="!userStore.isLogin"
                :to="{ name: 'login' }"
                class="block w-full px-4 py-2 text-left text-gray-700 hover:bg-gray-100"
                >Login</RouterLink
              >
              <button
                v-if="userStore.isLogin"
                @click="logOut"
                class="block w-full px-4 py-2 text-left text-gray-700 hover:bg-gray-100"
              >
                로그아웃
              </button>
            </div>
          </div>
        </div>
        <div class="flex items-center md:hidden">
          <button @click="toggleMenu" class="text-gray-600 hover:text-black">
            <Menu />
          </button>
        </div>
      </div>
    </div>
    <div v-if="isMenuOpen">
      <div
        class="fixed inset-0 z-40 transition-opacity duration-500 bg-black bg-opacity-70"
        @click="toggleMenu"
      ></div>
      <div
        class="fixed top-0 right-0 z-50 w-64 h-full transition-transform duration-500 transform bg-white shadow-lg"
        :class="{
          'translate-x-full': !isMenuOpen,
          'translate-x-0': isMenuOpen,
        }"
      >
        <div class="px-2 pt-2 pb-3 space-y-1 select-none text-md sm:px-3">
          <div class="flex justify-between">
            <RouterLink
              v-if="isLogin"
              :to="{ name: 'profile', params: { tab: 'basicInfo' } }"
              class="block px-3 py-2 text-sm text-gray-700 hover:font-bold"
              @click="toggleMenu"
            >
              마이 페이지
            </RouterLink>
            <RouterLink
              v-if="!userStore.isLogin"
              :to="{ name: 'login' }"
              class="px-3 text-gray-700 hover:font-bold"
              >Login</RouterLink
            >
            <button
              v-if="userStore.isLogin"
              @click="logOut"
              class="px-3 text-gray-700 hover:font-bold"
            >
              Log out
            </button>
          </div>
          <RouterLink
            :to="{ name: 'deposit' }"
            class="block px-3 py-2 text-gray-700 hover:bg-slate-100"
            @click="toggleMenu"
            >예적금 금리 비교</RouterLink
          >
          <RouterLink
            :to="{ name: 'exchange' }"
            class="block px-3 py-2 text-gray-700 hover:bg-slate-100"
            @click="toggleMenu"
            >환율 계산기</RouterLink
          >
          <RouterLink
            :to="{ name: 'map' }"
            class="block px-3 py-2 text-gray-700 hover:bg-slate-100"
            @click="toggleMenu"
            >은행 지점찾기</RouterLink
          >
          <RouterLink
            :to="{ name: 'recommend' }"
            class="block px-3 py-2 text-gray-700 hover:bg-slate-100"
            @click="toggleMenu"
            >상품 추천 서비스</RouterLink
          >
          <RouterLink
            :to="{ name: 'board' }"
            class="block px-3 py-2 text-gray-700 hover:bg-slate-100"
            @click="toggleMenu"
            >커뮤니티</RouterLink
          >
          <button
            @click="openDeleteModal"
            class="px-3 text-xs text-gray-200 hover:underline"
          >
            회원탈퇴를 하시겠습니까?
          </button>
        </div>
      </div>
      <CustomModal
        v-model="isDeleteModalOpen"
        @confirm="handleDeleteConfirm"
        @cancel="handleDeleteCancel"
        :modalTitle="'회원탈퇴를 하시겠습니까?'"
        :confirmText="'확인'"
        :cancelText="'취소'"
        >확인을 누르면 계정에 대한 모든 정보가 삭제됩니다.</CustomModal
      >
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/user';
import Menu from 'vue-material-design-icons/Menu.vue';
import Profile from 'vue-material-design-icons/AccountCircle.vue';
import CustomModal from '@/components/Modal.vue';

const userStore = useUserStore();
const isLogin = userStore.isLogin;

const isMenuOpen = ref(false);
const isProfileMenuOpen = ref(false);
const isDeleteModalOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const toggleProfileMenu = () => {
  isProfileMenuOpen.value = !isProfileMenuOpen.value;
};

const logOut = () => {
  userStore.logOut();
  isProfileMenuOpen.value = false;
};

const deleteAccount = () => {
  userStore.deleteAccount();
};

const openDeleteModal = () => {
  isDeleteModalOpen.value = true;
};

const handleDeleteConfirm = () => {
  deleteAccount();
  isDeleteModalOpen.value = false;
};

const handleDeleteCancel = () => {
  isDeleteModalOpen.value = false;
};
</script>

<style>
  .homelogo {
    width: 216px;
    height: 45px;
  }
</style>