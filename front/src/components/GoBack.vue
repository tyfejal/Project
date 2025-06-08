<template>
  <div>
    <!-- 홈 화면으로 돌아가는 라우터 링크 -->
    <RouterLink to="/" class="arrow-back-container">

      <!-- Google Material Icons 폰트 사용 -->
      <span class="arrow-back-icon material-symbols-outlined">
        arrow_back
      </span>

      <span class="arrow-back-text">뒤로가기</span>
    </RouterLink>
  </div>
</template>

<style scoped>

/* 링크 전체 영역을 수평 정렬 */
.arrow-back-container {
  display: flex;
  align-items: center;
  text-decoration-line: none;
  color: black;
  width: 100px;
  /* 줄바꿈 방지 */
  white-space: nowrap
}

/* 마우스 오버 할때 색상과 글꼴 강조하기 */
.arrow-back-container:hover {
  color: blue;
  font-weight: bold;
}
/* 뒤로가기 텍스트 크기 조절 */
.arrow-back-text {
  font-size: 1.2rem;
}
</style>