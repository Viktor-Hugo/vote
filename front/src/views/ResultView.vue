<template>
  <div class="result-component">
    <h2>발표 순서 낙찰 결과</h2>
    <ul class="result-list">
      <li v-for="result in results" :key="result.announcement_order">
        <strong>{{ result.announcement_order }}번째 발표:</strong> 팀 {{ result.winning_team }} 낙찰
      </li>
    </ul>
    <h3>남은 팀 포인트</h3>
    <ul class="team-list">
      <li v-for="team in remainTeams" :key="Object.keys(team)[0]">
        팀 {{ Object.keys(team)[0] }}: {{ Object.values(team)[0] }} 포인트
      </li>
    </ul>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useAccountStore } from '@/stores/accounts';
  import axios from 'axios'
  
  const API_URL = import.meta.env.VITE_API_URL
  const results = ref([])
  const remainTeams = ref([])
  onMounted(() => {
    axios({
      method: 'GET',
      url: `${API_URL}/api/v1/winner/`,
      headers: {
        Authorization: `Token ${useAccountStore().userInfo.token}`,
      },
    })
      .then(res => {
        results.value = res.data.data
        remainTeams.value = res.data.remain_teams
      })
      .catch(err => null)
  })
</script>

<style scoped>
.result-component {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  max-width: 600px;
  margin: auto;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.result-list,
.team-list {
  list-style: none;
  padding: 0;
}

.result-list li,
.team-list li {
  padding: 10px;
  background-color: #fff;
  margin-bottom: 10px;
  border-radius: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.result-list li strong {
  color: #333;
}

.team-list li {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
}

h2,
h3 {
  text-align: center;
  color: #333;
}

h3 {
  margin-top: 30px;
}
</style>
