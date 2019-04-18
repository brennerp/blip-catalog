<template>
  <div class="image-catalog">
    <div id="svg-browser">
      <p>SVG files</p>
      <div id="svg-browser" class="image-browser">
        <svg-container
          v-for="(svg, index) in svgs"
          v-once
          :key="index"
          :originalPath="svg.originalPath"
          :path="svg.path"/>
      </div>
    </div>

    <div id="png-browser">
      <p>PNG files</p>
      <div id="png-browser" class="image-browser">
        <image-container
          v-once
          v-for="(png, index) in pngs"
          :key="index"
          :originalPath="png.originalPath"
          :path="png.path"/>
      </div>
    </div>

  </div>
</template>

<script>
import ImageContainer from './ImageContainer.vue';
import SvgContainer from './SvgContainer.vue';

function importAll(files) {
  const keys = files.keys();
  const pathMap = keys.map(files);
  return keys.map(
    (key, index) => {
      const path = pathMap[index];
      return {
        originalPath: key,
        path,
      };
    },
  );
}

const importSvgs = require.context('../../assets/img/organized', true, /\.svg$/);
console.log(importSvgs.keys());

const test = importAll(importSvgs);
console.log(test);

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
.image-container {
  position: relative;
  width: 120px;
  min-height: 120px;
  padding: 15px;
  margin-right: 10px;
  margin-bottom: 10px;
  border: 2px solid #0cc8cc;
  border-radius: 10px;
}

.image-container figcaption {
  position: absolute;
  left: 0;
  bottom: 0;
  display: block;
  width: 100%;
  text-align: center;
  background-color: #0cc8cc;
  font-size: 14px;
}

.image-browser {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
