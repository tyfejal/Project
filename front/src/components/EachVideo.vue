<template>
  <div>
    <!-- 영상카드 클릭시 상세페이지로 이동 -->
    <div class="video-card card text-bg-light border-secondary" v-on:click="moveToDetail">
      <!-- 썸네일 이미지 클릭시 상세페이지로 이동 -->
      <img class="card-img-top" v-bind:src="thumbnailSrc" v-on:click="moveToDetail" alt="video" />
      <div class="card-body">
        <!-- 영상제목 보이기 -->
        <p class="card-text">{{ title }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

// SearchVideoList (부모) 컴포넌트로 부터 받은 props 객체 정의
const props = defineProps({
  video: {
    description: String,
    publishTime: String,
    thumbnails: {
      default: {
        height: Number,
        width: Number,
        url: String,
      },
      high: Object,
      medium: Object,
    },
    title: String,
    videoId: String,
  },
})

// props를 반응형으로 
const video = ref(props.video)

// 중간 해상도 썸네일 URL 추출
const thumbnailSrc = computed(() => {
  return video.value.thumbnails.medium.url;
})

// 영상 제목 추출
const title = computed(() => {
  return video.value.title;
})

// 라우터 인스턴스 생성해서 카드 클릭시 상세페이지로 이동 (router.push)
const router = useRouter()

const moveToDetail = () => {
  router.push(`/videos/${video.value.videoId}`);
}

</script>


<style scoped>
.video-card {
  width: 300px;
  height: 300px;
}

.card-text {
  font-size: 1.2rem;
  font-weight: bolder;
}
</style>