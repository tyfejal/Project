<template>
  <div>
    

    <div class="search-view">
      <GoBack />
      <h1>[금융]비디오 검색</h1>
      <SearchInput class="search-input" @get-videos="getVideos" />
      <div v-if="isLoading">
        <LoadingIcon />
      </div>
      <div v-else>
        <div v-if="videoList.length === 0">검색 결과가 없습니다.</div>
        <SearchVideoList  v-else :video-list="videoList" />
      </div>
    </div>
  </div>
  
  
</template>

<script setup>
  import SearchInput from "@/components/Search/SearchInput.vue"
  import SearchVideoList from "@/components/Search/SearchVideoList.vue"
  import GoBack from "@/components/GoBack.vue"
  import LoadingIcon from "@/components/LoadingIcon.vue"
  import Navbar from "@/components/Navbar.vue"
  import { ref } from "vue"
  import axios from "axios"
  import dayjs from "dayjs"

  const URL = "https://www.googleapis.com/youtube/v3";
  const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
  const videoList = ref([]);
  const word = ref("");
  const isLoading = ref(false);

  const getVideos = (userInput) => {
    word.value = userInput;
    isLoading.value = true;
    axios
      .get(`${URL}/search`, {
        params: {
          key: API_KEY,
          part: "snippet",
          type: "video",
          q: word.value,
          maxResults: 10,
        },
      })
      .then((response) => {
        const parsedVideoList = response.data.items.map((item) => {
          return {
            videoId: item.id.videoId,
            title: item.snippet.title,
            description: item.snippet.description,
            publishTime: dayjs(item.snippet.publishTime).format("YYYY-MM-DD"),
            thumbnails: item.snippet.thumbnails,
          };
        });
        videoList.value = parsedVideoList;
        isLoading.value = false;
      })
      .catch((error) => {
        console.log(error);
        isLoading.value = false
      });
  };
</script>

<style scopped>
  .content {
    margin-top: 2rem;
  }

  .search-input {
    margin-bottom: 20px;
  }

  .search-view {
    display: flex;
    flex-direction: column;
    padding-top: 56px;
    align-items: center;
    justify-content: center;
  }

  .search-input input {
    padding: 10px 15px;
  }
</style>