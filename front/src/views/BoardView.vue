<template>
  <div
    class="container relative flex flex-col items-center w-4/5 mx-auto overflow-hidden rounded-[80px] shadow-md bg-slate-100"
  >
    <img
      class="object-cover w-full overflow-hidden grayscale-[5%] h-48 blur-[1px]"
      src="@/assets/images/board.png"
      alt="게시판 페이지 헤더 이미지"
    />
    <h1
      class="absolute text-5xl font-bold tracking-widest text-center text-white top-24"
    >
      <span class="hidden text-black sm:inline-block">커뮤니티 게시판</span>
    </h1>
    <div class="flex flex-col w-3/5 my-3">
      <button
        class="flex items-center self-end px-4 my-2 btn-active w-min"
        @click="handleClickCreate"
      >
        Create
      </button>
      <BoardArticleList
        v-if="boardStore.articles"
        :articles="boardStore.articles"
      />
    </div>
  </div>
</template>

<script setup>
import BoardArticleList from '@/components/BoardArticleList.vue';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useBoardStore } from '@/stores/board';

const boardStore = useBoardStore();
const router = useRouter();

onMounted(() => {
  boardStore.fetchArticles();
});

const handleClickCreate = () => {
  router.push({ name: 'create-article' });
};
</script>
