<template>
  <div>
    <!-- <h2></h2>
    <p v-if="rate"></p>
    <p v-else></p> -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const rate = ref(null)

// ✅ .env에서 불러온 API 키
const apiKey = import.meta.env.VITE_EXCHANGE_API_KEY;
console.log("API Key:", apiKey)

onMounted(async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/exchange-rate/api/v1/today/", {
      headers: {
        // 만약 API 키가 필요하다면 헤더에 추가
        Authorization: `Bearer ${apiKey}`
      }
    })
    rate.value = response.data.rate
  } catch (error) {
    console.error("API 호출 에러:", error)
  }
})
</script>
