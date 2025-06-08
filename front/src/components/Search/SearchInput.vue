<template>
  <div>
    <div class="input-group">
      <!-- 검색창에서 엔터누르든 찾기 버튼 누르든 똑같은 함수 호출해서 기능 똑같게 구현 -->
      <input
       type="text"
       class="form-control"
       placeholder="검색어를 입력하세요."
       v-model="userInput"
       @keyup.enter = "getSearchData"
      >
      <button class="btn btn-success" type="button" @click="getSearchData">
        찾기
      </button>
    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue"

  const userInput = ref("")

  const emit = defineEmits(["getVideos"])

  const getSearchData = function() {
    if (userInput.value.trim() !== "") {
      emit('getVideos', userInput.value)
    }
    
  }
</script>

<style scoped>
  .input-group {
  max-width: 600px;
  margin: 0 auto;
}

</style>