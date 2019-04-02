<template>
  <div id="app">
    <div class="wrapper">
      <image-catalog></image-catalog>
    </div>
  </div>
</template>

<script>
import ImageCatalog from './components/imageCatalog/ImageCatalog.vue';

export default {
  name: 'app',
  components: {
    ImageCatalog,
  },
};
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #E3FFAA;
}

.wrapper {
  padding: 40px;
}
</style>
