<template>
  <div class="image-container">
    <img :src="path" :alt="alt" :title="title"/>
  </div>
</template>

<script>
export default {
  name: 'image-container',
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
.image-container {
  width: 120px;
  min-height: 120px;
  padding: 10px;
  margin-right: 10px;
  margin-bottom: 10px;
  border: 1px solid blue;
}

img {
  display: block;
}

#png-browser img {
  max-width: 120px;
  max-height: 120px;
}

#svg-browser img {
  width: 120px;
  height: 120px;
}
</style>
