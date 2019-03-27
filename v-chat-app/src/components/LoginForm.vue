<template>
  <form class="login-form" @submit.prevent.stop="authUser">
    <input v-model.trim="username" type="text" placeholder="Имя аккаунта" autofocus>
    <input v-model="password" type="password" placeholder="Пароль">
    <button type="submit">Войти</button>
  </form>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    authUser() {
      const data = {
        username: this.username,
        password: this.password
      };
      const options = {
        method: "POST",
        url: "auth/token/create/",
        data: this.$qs.stringify(data, { arrayFormat: "repeat" })
      };

      this.$http(options)
        .then(response => {
          alert("Добро пожаловать!");
          const AUTH_TOKEN = response.data.data.attributes.auth_token;
          localStorage.setItem("auth_token", AUTH_TOKEN);
          this.$store.commit("setToken");
          this.$store.dispatch("authSuccess");
          this.goBackOrRedirectToHome();
        })
        .catch(error => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            if (error.response.status === 400) {
              alert("Введённые данные некорректны!");
            } else {
              console.log(error.response.data);
              console.log(error.response.status);
              console.log(error.response.headers);
            }
          } else if (error.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(error.request);
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log("Error", error.message);
          }

          console.log(error.config);
        });
    },

    goBackOrRedirectToHome() {
      window.history > 1 ? this.$router.go(-1) : this.$router.push("/");
    }
  }
};
</script>

<style>
</style>
