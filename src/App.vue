<template>
  <div id="app">
    <div class="wrapper">
      <div id="svg-browser">
        <p>SVG files</p>
        <div class="image-browser">
          <div class="image-container" v-for="svg in svgs" :key="svg">
            <img :alt="svg" :src="svg" />
          </div>
        </div>
      </div>

      <div id="png-browser">
        <p>PNG files</p>
        <div class="image-browser">
          <div class="image-container" v-for="png in pngs" :key="png">
            <img :alt="png" :src="png">
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
function importAll(r) {
  return r.keys().map(r);
}

const svgFiles = importAll(require.context('./assets/img/svg', true, /\.svg$/));
const pngFiles = importAll(require.context('./assets/img/png', true, /\.png$/));
const gifFiles = importAll(require.context('./assets/img/gif', true, /\.gif$/));

export default {
  name: 'app',
  data() {
    return {
      pngs: pngFiles,
      svgs: svgFiles,
      gifs: gifFiles,
    };
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
  background: #607B99;
}

.wrapper {
  padding: 40px;
}

.image-browser {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.image-container {
  width: 120px;
  height: 120px;
  padding: 10px;
  margin-right: 10px;
  margin-bottom: 10px;
  border: 1px solid blue;
}

img {
  max-width: 100%;
  max-height: 100%;
}
</style>
