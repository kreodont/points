<template>
  <!-- demo root element -->
  <div id="demo">
    <My :title="title" :data="gridData" :columns="gridColumns"></My>
  </div>

</template>

<script>
  import My from './components/My.vue'

  export default {
    name: 'App',
    components: {
      My
    },
    data: function () {
      return {
        title: 'From component',
        searchQuery: '',
        gridColumns: ['Имя', 'Время', 'Описание', 'Баллы'],
        gridData: []
        // { "Имя": 'Chuck Norris', 'Описание': 'Карл у Клары украл кораллы. Кораллы, Карл!' },]

      }
    },
    created() {
      this.$http.post('https://o4qvvrybeney3a2ilgryjkgd2q.appsync-api.us-east-1.amazonaws.com/graphql', ).then(response => {}, error => {console.log(error)})
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
