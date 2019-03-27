import Vue from "vue";
import axios from "axios";
import qs from "qs";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

// Добавление и настройка глобального метода для асинхронных запросов:
Vue.prototype.$http = axios;
Vue.prototype.$http.defaults.baseURL = "http://127.0.0.1:8000/";
Vue.prototype.$http.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";
// Метод для сериализации:
Vue.prototype.$qs = qs;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
