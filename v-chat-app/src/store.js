import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isAuthorized: false,
    token: "",
    roomId: null
  },
  mutations: {
    alterAuthStatus(state) {
      state.isAuthorized = !state.isAuthorized;
    },

    setToken(state) {
      state.token = "Token " + localStorage.getItem("auth_token");
    },
    eraseToken(state) {
      state.token = "";
    },

    provideRoomId(state, payload) {
      state.roomId = payload;
    }
  },
  actions: {
    authSuccess({ commit }) {
      commit("alterAuthStatus");
    },
    deauthorize({ commit }) {
      commit("alterAuthStatus");
    }
  }
});
