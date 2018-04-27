<template>
  <div id="test" :style="{ fontSize: fsize + 'em' }">
    <p><b>{{title}}</b></p>
    <table v-if="columns">
      <thead>
      <tr>
        <th v-for="key in columns"> {{key | capitalize}}</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="entry in filteredData">
        <td v-for="key in columns">
          {{entry[key]}}
        </td>
      </tr>
      </tbody>
    </table>
  </div>

</template>

<script>
  export default {
//    props: {
//      strings: Array,
//    },
    props: {'title': String, 'fsize': String, 'data': Array, 'columns': Array, 'filterKey': String},
    template: "#test",
    data() {
      return {}
      },

    filters: {
      capitalize: function (str) {
        if (str !== undefined) {
          return str.charAt(0).toUpperCase() + str.slice(1)
        }
        return ""
      }
    },
    computed: {
      filteredData: function () {
        let filterKey = this.filterKey && this.filterKey.toLowerCase();
        let data = this.data;
        if (filterKey) {
          data = data.filter(function (row) {
            return Object.keys(row).some(function (key) {
              return String(row[key]).toLowerCase().indexOf(filterKey) > -1
            })
          })
        }
        return data
      }
    },
//    created: function () {
//      this.strings = ['1', '2', '3']
//    }
  }
</script>

<style>
  body {
    font-family: Helvetica Neue, Arial, sans-serif;
    font-size: 14px;
    color: #444;
  }
  p {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 20px;
    font-size: 24px;
  }

  table {
    border: 2px solid #42b983;
    border-radius: 3px;
    background-color: #fff;
  }

  th {
    background-color: #42b983;
    color: rgba(255,255,255,0.66);
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  td {
    background-color: #f9f9f9;
  }

  th, td {
    min-width: 120px;
    padding: 10px 20px;
  }

  /*th.active {*/
    /*color: #fff;*/
  /*}*/

  /*th.active .arrow {*/
    /*opacity: 1;*/
  /*}*/

  /*.arrow {*/
    /*display: inline-block;*/
    /*vertical-align: middle;*/
    /*width: 0;*/
    /*height: 0;*/
    /*margin-left: 5px;*/
    /*opacity: 0.66;*/
  /*}*/

  /*.arrow.asc {*/
    /*border-left: 4px solid transparent;*/
    /*border-right: 4px solid transparent;*/
    /*border-bottom: 4px solid #fff;*/
  /*}*/

  /*.arrow.dsc {*/
    /*border-left: 4px solid transparent;*/
    /*border-right: 4px solid transparent;*/
    /*border-top: 4px solid #fff;*/
  /*}*/

</style>
