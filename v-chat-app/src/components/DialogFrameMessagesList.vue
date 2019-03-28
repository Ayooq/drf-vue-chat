<template>
  <ul class="messages-list">
    <li v-for="message in messages" :key="message.id">
      <div>{{ message.text }}</div>
      <div>
        <b>{{ message.sender.username }}</b>
      </div>
      <div>
        <i>{{ message.dispatch_date }}</i>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
  name: "MessagesList",
  props: {
    updateDialog: Boolean
  },
  data() {
    return {
      messages: ""
    };
  },
  computed: {
    roomId() {
      return this.$store.state.roomId;
    }
  },
  watch: {
    updateDialog: "reRenderList"
  },
  created() {
    this.showMessages();
  },
  methods: {
    showMessages() {
      const params = {
        room: this.roomId
      };
      const options = {
        method: "GET",
        url: "api/v1/chat/dialogs/",
        params,
        paramsSerializer(params) {
          return this.$qs.stringify(params, { arrayFormat: "repeat" });
        }
      };

      this.$http(options)
        .then(response => {
          this.messages = response.data.data.messages;
          console.log(this.messages);
          this.$emit("up-to-date");
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

    reRenderList() {
      if (this.updateDialog) {
        this.showMessages();
      }
    }
  }
};
</script>

<style>
</style>
