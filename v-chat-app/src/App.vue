<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    isAuthorized() {
      return this.$store.state.isAuthorized;
    },
    token() {
      return this.$store.state.token;
    }
  },
  watch: {
    token() {
      this.$http.defaults.headers.common["Authorization"] = this.token;
      console.log(this.$http.defaults.headers.common["Authorization"]);
    }
  },
  created() {
    if (!this.isAuthorized) {
      this.$router.push("/auth");
    }
  }
};
</script>


<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
