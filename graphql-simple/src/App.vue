<template>
  <!-- demo root element -->
  <div id="demo">
      <!--Поиск <input name="query" v-model="searchQuery">-->
    <My :title="title" :data="gridData" :columns="gridColumns"></My>
  </div>

</template>

<script>
  import My from './components/My.vue'
  import axios from 'axios'

  export default {
    name: 'App',
    components: {
      My
    },
    data: function () {
      return {
        gridColumns: ['Имя', 'Время', 'Описание', 'Баллы'],
        gridData: []

      }
    },
    created() {
      let config = {headers: {'Content-Type': 'application/graphql', 'x-api-key': 'da2-mb5oh5jfp5gcncvvcx5du5634m'}};
      let data = {query: "{allPoint{points{points_owner{printable_name, current_points}, details, number, creation_readable_date_time_moscow}}}"};
      axios.post('https://o4qvvrybeney3a2ilgryjkgd2q.appsync-api.us-east-1.amazonaws.com/graphql', data, config)
        .then(
          response => {
            let points = response['data']['data']['allPoint']['points'];
            for (let index in points) {
              if (points.hasOwnProperty(index)) {
                this.gridData.push({
                  'Имя': points[index]['points_owner']['printable_name'],
                  'Время': points[index]['creation_readable_date_time_moscow'],
                  'Описание': points[index]['details'],
                  'Баллы': points[index]['number']});
              }
            }
              },
          error => {console.log(error)})
    }
  }

</script>

<style scoped>
#demo {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  /*margin-top: 60px;*/
}
</style>
