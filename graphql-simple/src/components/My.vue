<template>
  <div id="test" :style="{ fontSize: fsize + 'em' }">
    <b>{{title}}</b>
    <ul>
      <li v-for="string in strings">{{string}}</li>
    </ul>
  </div>

</template>

<script>
  export default {
//    props: {
//      strings: Array,
//    },
    props: {'title': String, 'fsize': String},
    template: "#test",
    data() {
      return {
        strings: ["One", "Two", "Three", "Vasia"],
      }
      },
//    created: function () {
//      this.strings = ['1', '2', '3']
//    }
  }
</script>
