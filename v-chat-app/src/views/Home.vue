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
      localStorage.removeItem("auth_token");
      this.$store.commit("eraseToken");
      this.$store.dispatch("deauthorize");
      this.$router.push("/auth");
    },
    showDialog() {
      this.isVisible = true;
    }
  }
};
</script>
