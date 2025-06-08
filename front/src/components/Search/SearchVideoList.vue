<template>
  <div class="video-list-wrapper">
    <ul class="video-list-ul">
      <li
        class="video-list-li"
        v-for="video in videoList"
        :key="video.videoId"
      >
      <EachVideo :video="video" />
      </li>
    </ul>
  </div>
</template>

<script setup>
import EachVideo from "@/components/EachVideo.vue";

const props = defineProps({
  videoList: Array
})

</script>

<style scoped>
.video-list-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  padding: 1rem;
}

.video-list-ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 0;
  margin: 0;
  gap: 20px;
  list-style: none;
}

.video-list-li {
  flex: 0 0 auto;
}
</style>
