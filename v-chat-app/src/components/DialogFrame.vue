<template>
  <div class="dialog-frame">
    <DialogFrameMessagesList :updated-dialog="dialog"/>
    <DialogFrameReplyForm @message-submitted="updateDialog"/>
  </div>
</template>

<script>
import DialogFrameMessagesList from "@/components/DialogFrameMessagesList.vue";
import DialogFrameReplyForm from "@/components/DialogFrameReplyForm.vue";

export default {
  name: "DialogFrame",
  components: {
    DialogFrameMessagesList,
    DialogFrameReplyForm
  },
  data() {
    return {
      dialog: undefined
    };
  },
  methods: {
    updateDialog(content) {
      this.dialog = content;
    }
  }
};
</script>

<style>
</style>
