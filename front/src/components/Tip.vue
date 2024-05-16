<template>
  <div class="modal-overlay" @click="$emit('toggle')">
    <div class="modal-content">
      <div class="modal-body">
        <p><strong>1. 입찰 최종 마감일 :</strong> 5월 29일 (수) 오후 2시 00분</p>
        <p><strong>2. 기본 룰 :</strong> <span class="highlight">마감</span> 시점 기준 <span class="highlight">최상위 입찰팀</span>이 해당 발표 순서를 <span class="highlight">낙찰</span> 받습니다.</p>
        <p><strong>3. 단, 한 개의 팀이 2개 이상의 발표 순서의 <span class="highlight">최상위 입찰팀</span>인 경우, 그 중, 입찰가가 높은 순서를 <span class="highlight">낙찰</span> 받습니다.</strong></p>
        <p> - ex)</p>
        <p> - 1팀이 2번 발표에 1000 포인트, 3번 발표에 2000 포인트로 입찰하여</p>
        <p> - 두 순서에 모두 <span class="highlight">최상위 입찰팀</span>인 경우, 1팀은 3번 발표를 <span class="highlight">낙찰</span> 받습니다.</p>
        <p> - 이때, 2번 발표는 <span class="highlight">최상위 입찰팀</span>이 사라지므로, 자연스레 2번째 <span class="highlight">입찰팀</span>이 <span class="highlight">낙찰</span> 받습니다.</p>
        <p> - 2번째 <span class="highlight">입찰팀</span> 역시 다른 발표를 <span class="highlight">낙찰</span>받게 된 경우는, 3번째 <span class="highlight">입찰팀</span>으로 이관됩니다.</p>
        <p> - 이하 동일</p>
        <p><strong>4. 만약, 하나도 <span class="highlight">낙찰</span>받지 못 한 경우, <span class="highlight">마감</span> 시점을 기준으로 하여 팀별 잔여 포인트순으로 우선권을 드립니다.</strong></p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  isActivate: Boolean
})
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  width: 90%;
  max-width: 600px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 1.2em;
  color: #d32f2f; /* Red color for close button */
}

.modal-body p {
  margin: 10px 0;
}

.modal-body strong {
  display: block;
  margin-bottom: 5px;
}

.highlight {
  font-weight: bold;
}

.highlight:nth-of-type(1) {
  color: #1976d2; /* Blue for 최상위 입찰팀 */
}

.highlight:nth-of-type(2) {
  color: #388e3c; /* Green for 낙찰 */
}

.highlight:nth-of-type(3) {
  color: #d32f2f; /* Red for 마감 */
}

.highlight:nth-of-type(4) {
  color: #fbc02d; /* Yellow for n번째 입찰팀 */
}
</style>
