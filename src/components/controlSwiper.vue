<template lang="pug">
div.arrow_wrapper
    img(src="../assets/images-booking/arrow-left.svg" @click="swiper.slidePrev()")
    img(src="../assets/images-booking/arrow-right.svg" @click="swiper.slideNext()")
</template>

<script setup>
import { useSwiper } from 'swiper/vue';

const swiper = useSwiper();
</script>

<style>
.arrow_wrapper{
  display: flex;
  justify-content: end;
  gap: 10px;
  margin-top: 22px;
}
</style>