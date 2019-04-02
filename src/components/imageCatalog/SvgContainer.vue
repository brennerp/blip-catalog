<template>
  <div class="svg-container">
    <img :src="path" :alt="alt" :title="title"/>
  </div>
</template>

<script>
export default {
  name: 'svg-container',
  props: {
    path: {
      type: String,
    },
    alt: {
      type: String,
      default: 'Image',
    },
    title: {
      type: String,
      default: 'Image',
    },
  },
  computed: {
    fileName() {
      const splitPath = this.path.split('/');
      const fileName = splitPath[splitPath.length - 1];
      return fileName;
    },
  },
};
</script>

<style>
.svg-container {
  width: 120px;
  padding: 10px;
  margin-right: 10px;
  margin-bottom: 10px;
  border: 1px solid blue;
}

svg {
  display: block;
  width: 120px;
  height: 120px;
}
</style>
