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
  </div>
</template>

<script>
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

const svgFiles = importAll(require.context('../../assets/img/organized-new', true, /\.svg$/));

export default {
  name: 'new-image-catalog',
  components: {
    SvgContainer,
  },
  data() {
    return {
      svgArray: svgFiles,
    };
  },
  computed: {
    svgs() {
      return [...new Set(this.svgArray)];
    },
  },
};
</script>

<style>
</style>
