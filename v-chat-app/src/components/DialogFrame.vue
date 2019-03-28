<template>
  <div class="dialog-frame">
    <DialogFrameMessagesList :update-dialog="updateDialog" @up-to-date="updateDialog = false"/>
    <DialogFrameReplyForm @message-submitted="updateDialog = true"/>
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
      updateDialog: false
    };
  }
};
</script>

<style>
</style>
