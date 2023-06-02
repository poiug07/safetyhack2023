<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
import Footer from './components/Footer.vue';
export default {
    name: "App",
    components: { Footer }
}
</script>

