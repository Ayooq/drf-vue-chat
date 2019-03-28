<template>
  <div class="home">
    <button @click.stop.prevent="logoutUser">Выйти</button>
    <RoomsList @room-selected="showDialog"/>
    <DialogFrame v-if="isVisible"/>
  </div>
</template>

<script>
import RoomsList from "@/components/RoomsList.vue";
import DialogFrame from "@/components/DialogFrame.vue";

export default {
  name: "Home",
  components: {
    RoomsList,
    DialogFrame
  },
  data() {
    return {
      isVisible: false
    };
  },
  methods: {
    logoutUser() {
      sessionStorage.removeItem("auth_token");
      this.setAuthState();
      this.$router.push("/auth");
    },
    setAuthState() {
      this.$store.commit("eraseToken");
      this.$store.commit("alterAuthStatus");
    },
    showDialog() {
      this.isVisible = true;
    }
  }
};
</script>
