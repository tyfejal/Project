<template>
  <section
    class="flex flex-col w-10/12 px-4 mx-auto my-16 text-center select-none max-w-7xl sm:px-6 lg:px-8 gap-y-2"
  >
    <p>내게 딱 맞는 금융상품, 찾기 어렵게 느껴지셨나요?</p>
    <h2 class="text-2xl font-bold hahmlet">
      모두의금융이 쉽게, 그리고 정확하게 도와드릴게요!
    </h2>
    <div class="flex justify-between gap-5 mt-5">
      <div
        v-for="item in items"
        :key="item.index"
        class="flex flex-col items-center text-center gap-y-3"
      >
        <img
          :src="getIconPath(item.index)"
          :alt="'인트로 섹션 이미지' + item.index"
          class="w-[130px]"
        />
        <h4 class="font-medium">{{ item.title }}</h4>
        <p class="px-4 font-thin break-words text-balance">
          {{ item.description }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
const items = [
  {
    index: 1,
    title: '다양한 서비스 제공',
    description:
      '금/은 시세, 영상 검색, 환율 계산, 나에게 가까운 은행지점 찾기까지 다양한 서비스를 모두 챙겼습니다.',
  },
  {
    index: 2,
    title: '나에게 꼭 맞는 금융 추천',
    description:
      '몇 가지 질문에 답하면, 똑똑한 알고리즘이 내 상황에 딱 맞는 금융상품을 추천해줘요. 처음 접하는 분도, 익숙한 분도 모두 쉽게 활용할 수 있어요.',
  },
  {
    index: 3,
    title: '광고 없는 깔끔한 추천',
    description:
      '광고나 협찬 없이, 오직 믿을 수 있는 데이터로만 금융상품을 추천해요. 편향 없는 정보를 원한다면 모두의금융이 정답입니다.',
  },
];

const getIconPath = index => {
  return `images/icons/desc-section${index}-icon.png`;
};
</script>
