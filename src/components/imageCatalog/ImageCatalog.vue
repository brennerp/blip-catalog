<template>
  <div class="image-catalog">
    <div id="svg-browser">
      <p>SVG files</p>
      <div id="svg-browser" class="image-browser">
        <svg-container
          v-for="(svg, index) in svgs"
          v-once
          :key="index"
          :path="svg"/>
      </div>
    </div>

    <div id="png-browser">
      <p>PNG files</p>
      <div id="png-browser" class="image-browser">
        <image-container
          v-once
          v-for="(png, index) in pngs"
          :key="index"
          :path="png"/>
      </div>
    </div>

  </div>
</template>

<script>
import ImageContainer from './ImageContainer.vue';
import SvgContainer from './SvgContainer.vue';

function importAll(r) {
  return r.keys().map(r);
}

const importSvgs = require.context('../../assets/img/organized', true, /\.svg$/);
console.log(importSvgs.keys());

const svgFiles = importAll(importSvgs);
const pngFiles = importAll(require.context('../../assets/img/png', true, /\.png$/));


// const gifFiles = importAll(require.context('../../assets/img/gif', true, /\.gif$/));

export default {
  name: 'image-catalog',
  components: {
    ImageContainer,
    SvgContainer,
  },
  data() {
    return {
      pngArray: pngFiles,
      svgArray: svgFiles,
      // gifs: gifFiles,
    };
  },
  computed: {
    svgs() {
      return [...new Set(this.svgArray)];
    },
    pngs() {
      return this.pngArray;
    },
  },
};
</script>

<style>
.image-browser {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
