<template>
  <div id="app" v-if="hydrated">
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: () => ({ hydrated: false }),
  async mounted() {
    await this.$apollo.provider.defaultClient.hydrated();
    this.hydrated = true;
  }
}
</script>
