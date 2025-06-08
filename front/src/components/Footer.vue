<template>
  <footer class="px-4 py-8 bg-gray-800">
    <div
      class="container flex flex-col items-center justify-between mx-auto md:flex-row"
    >
      <div class="mb-4 text-center md:text-left md:mb-0">
        <h3 class="mb-2 text-lg font-semibold text-white">모두의금융</h3>
        <p class="text-sm text-gray-400">
          광주광역시 광산구 하남산단 6번로 107
        </p>
        <p class="text-sm text-gray-400">mogum@service.app</p>
      </div>
      <div class="flex justify-center md:justify-start">
        <ul class="flex space-x-6">
          <li>
            <RouterLink
              :to="{ name: 'home' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >홈</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'deposit' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >예적금 금리 비교</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'exchange' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >환율 계산기</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'metal' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >금/은 시세</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'map' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >은행 지점찾기</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'recommend' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >상품 추천 서비스</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'board' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >커뮤니티</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'InterestSearch' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >영상검색</RouterLink
            >
          </li>
        </ul>
      </div>
    </div>
    <div class="pt-4 mt-8 border-t border-gray-700">
      <p class="text-sm text-center text-gray-400">
        &copy; 2025 모두의금융. All rights reserved.
      </p>
    </div>
  </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>
