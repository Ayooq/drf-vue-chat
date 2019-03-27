<template>
  <ul class="rooms-list">
    <li
      v-for="room in rooms"
      :key="room.id"
      class="rooms-list__item"
      @click.stop.prevent="selectRoom(room.id)"
    >
      <h3 class="title">{{ room.creator.username }}</h3>
      <ul class="list">
        <li
          v-for="person in room.participants"
          :key="person.id"
          class="list__item"
        >{{ person.username }}</li>
      </ul>
    </li>
  </ul>
</template>

<script>
export default {
  name: "RoomsList",
  data() {
    return {
      rooms: undefined
    };
  },
  created() {
    this.getRooms();
  },
  methods: {
    getRooms() {
      this.$http
        .get("api/v1/chat/rooms/")
        .then(response => {
          this.rooms = response.data.data.rooms;
        })
        .catch(error => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
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

    selectRoom(roomId) {
      this.$store.commit("provideRoomId", roomId);
      this.$emit("room-selected");
    }
  }
};
</script>

<style scoped>
.rooms-list,
.list {
  list-style-type: none;
  padding: 0;
}
.rooms-list__item {
  cursor: pointer;
}
.rooms-list__item,
.list__item {
  display: inline-block;
  margin: 0 10px;
}
.title {
  margin: 20px 0 0;
}
</style>
