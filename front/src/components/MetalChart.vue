<template>
  <div class="p-4">
    <select v-model="selectedMetal" @change="loadData" class="mb-4 border rounded p-2">
      <option value="gold">Gold</option>
      <option value="silver">Silver</option>
    </select>

    <!-- <Line :data="chartData" :options="chartOptions" /> -->
    <!-- 크기 조절 컨테이너 -->
    <div class="chart-container">
      <Line :key="chartKey" :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'
import { ref, onMounted } from 'vue'
import axios from 'axios'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const selectedMetal = ref('gold')

const chartData = ref({
  labels: [],
  datasets: [{
    label: 'Price (₩)',
    data: [],
    borderColor: '#f9c74f',
    backgroundColor: 'rgba(249, 199, 79, 0.3)',
    fill: true
  }]
})

const chartOptions = {
  responsive: true,
  scales: {
    y: {
      beginAtZero: false
    }
  }
}

async function loadData() {
  const isGold = selectedMetal.value === 'gold'

  const res = await axios.get(`/api/metal-price/${selectedMetal.value}/`)
  console.log('✅ 응답 결과:', res.data) 
  // chartData.value = {
  // labels: res.data.map(i => i.date),
  // datasets: [{
  //   label: selectedMetal.value === 'gold' ? 'Gold Price (₩)' : 'Silver Price (₩)',
  //   data: res.data.map(i => i.price),
  //   borderColor: '#f9c74f',
  //   backgroundColor: 'rgba(249, 199, 79, 0.3)',
  //   fill: true
  // }]
// }
  chartData.value = {
  labels: res.data.map(i => i.date),
  datasets: [{
    label: isGold ? 'Gold Price (₩)' : 'Silver Price (₩)',
    data: res.data.map(i => i.price),
    borderColor: isGold ? '#f9c74f' : '#aaa', // 골드는 금색, 은은 회은색
    backgroundColor: isGold
      ? 'rgba(249, 199, 79, 0.3)'
      : 'rgba(160, 160, 160, 0.3)',
    fill: true
  }]
}
}

onMounted(loadData)
</script>

<style scoped>
.chart-container {
  max-width: 1600px;
  max-height: 800px;
  margin: 0 auto;
}
</style>