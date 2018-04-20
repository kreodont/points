<template>
  <ul>
    <li v-for="string in strings">{{string}}</li>
  </ul>
  <!--<div>{{strings}}</div>-->

</template>

<script>
  export default {
//    props: {
//      strings: Array,
//    },
    data() {return {strings: ["One", "Two", "Three"]}},
//    created: function () {
//      this.strings = ['1', '2', '3']
//    }
  }
</script>
