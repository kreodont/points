<template>
  <!-- demo root element -->
  <div id="app">
    <My title="Some" fsize=0.8></My>
    <My title="Another"></My>
    <My></My>
  </div>

</template>

<script>
//import grid from './components/Grid.vue'

import My from './components/My.vue'


export default {
  name: 'App',
  components: {
    My
  }
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
