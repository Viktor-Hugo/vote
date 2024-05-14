<template>
  <div class="login-container">
    <form @submit.prevent="useAccountStore().login(user)" class="login-form">
      <label for="username">사용자 이름</label>
      <input type="text" name="username" id="username" v-model="user.username" placeholder="사용자 이름">
      
      <label for="password">비밀번호</label>
      <input type="password" name="password" id="password" v-model="user.password" placeholder="비밀번호">
      
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
  import { useAccountStore } from '@/stores/accounts';
  import { ref } from 'vue'
  const user = ref({
    username: '',
    password: '',
  })
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Full height of the viewport */
  background-color: #ffe0b2; /* Soft orange background */
}

.login-form {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
  width: 300px; /* Fixed width for the form */
  display: flex;
  flex-direction: column;
  gap: 15px; /* Gap between form elements */
}

.login-form label {
  font-size: 1em;
  color: #616161; /* Grey color for text */
}

.login-form input[type="text"],
.login-form input[type="password"] {
  padding: 10px;
  border: 1px solid #e0e0e0; /* Light grey border */
  border-radius: 5px; /* Rounded corners */
  font-size: 1em;
}

.login-form input[type="submit"] {
  background-color: #ffab91; /* Matching the border color of the last-bid-team class */
  color: #fff;
  border: none;
  border-radius: 5px; /* Rounded corners */
  padding: 10px;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.3s ease; /* Smooth transition */
}

.login-form input[type="submit"]:hover {
  background-color: #ff7043; /* Darker orange on hover */
}
</style>
