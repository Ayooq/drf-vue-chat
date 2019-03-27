<template>
  <div class="auth">
    <img alt="Vue logo" src="../assets/logo.png">
    <LoginForm/>
  </div>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "Auth",
  components: {
    LoginForm
  }
};
</script>
