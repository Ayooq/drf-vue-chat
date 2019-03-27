<template>
  <form class="reply-form" @submit.stop.prevent="sendReply">
    <textarea
      id="reply"
      v-model="replyText"
      name="reply"
      cols="30"
      rows="10"
      placeholder="Введите текст сообщения."
      required
    ></textarea>
    <button type="submit">Отправить</button>
  </form>
</template>

<script>
export default {
  name: "ReplyForm",
  data() {
    return {
      replyText: ""
    };
  },
  computed: {
    roomId() {
      return this.$store.state.roomId;
    }
  },
  methods: {
    sendReply() {
      const data = {
        room: this.roomId,
        text: this.replyText
      };
      const options = {
        method: "POST",
        url: "api/v1/chat/dialogs/",
        data: this.$qs.stringify(data, { arrayFormat: "repeat" })
      };

      this.$http(options)
        .then(response => {
          this.$emit("message-submitted", response.data.data.messages);
          console.log(response.data.data.messages);
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
    }
  }
};
</script>

<style>
</style>
