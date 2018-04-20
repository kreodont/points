<template>
  <ul>
    <li v-for="string in strings">{{string}}</li>
  </ul>
</template>

<script>
  export default {
    props: {
      strings: Array,
    },
    data() {return {}},
//    created: function () {
//      this.strings = ['1', '2', '3']
//    }
  }
</script>
