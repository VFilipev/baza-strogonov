<template lang="pug">
div
  //- Transition(name="fade" mode="out-in")
  RouterView
  <notifications />
</template>

<script>
import { RouterView } from 'vue-router'
export default {
  name:'app',
  setup(){
  return {
    RouterView
  }
  }
  
}
</script>



<style scoped>

.fade-enter-from,
.fade-leave-to{
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active{
  transition: opacity .5s ease-out;;
}
</style>
