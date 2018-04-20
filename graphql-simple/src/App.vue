<template>
  <div id="app">
    <my strings=[1, 2, 4]/>
    <!--<Table/>-->
  </div>
</template>

<script>
import my from './components/My.vue'
import grid from './components/Table.vue'

export default {
  name: 'App',
  components: {
    my
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
