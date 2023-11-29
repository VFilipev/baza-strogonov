<template lang="pug">
div
    .container 
        .row.d-flex.justify-content-between.align-items-center(style="padding-top:63px")
            .col-4.house_name {{ house.name }}
            btn.btn_close.d-flex(@click="$emit('modalClose')")        
        .row 
            .col-6
                .row
                    .col-12
                        .house__image(:style="{ backgroundImage: `url(${house.main_photo})` }")
                .row(style="margin-top:40px")
                    .swiper__wrapper(style="position: relative")                  
                        swiper(slidesPerView="2" :spaceBetween="40" @slideChange="showSliderIcon = false")
                            swiper-slide(v-for="card in house.galery")
                                .photogalery__card 
                                    .photogalery__image(:style="{ backgroundImage: `url(${card.photo})`}")
                                    .photogalery__name {{ card.name }}                            
                        img.slider_icon(v-if="showSliderIcon" src="../assets/images/slider-icon.svg")
            .col-6
                .row(style="margin-bottom:64px")                          
                    .col-12
                        .house__name_description Стоимость                            
                        .row_cost(v-for="cost in house.cost")                            
                            .house__text_description {{ cost.name }}
                            .house__text_description {{ cost.cost }}                            
                .row(style="margin-bottom:31px") 
                    .col-6
                        .house__name_description Описание 
                        .house__text_description {{ house.description }} 
                    .col-6 
                        .house__name_description Доступность
                        .house__text_description
                            p(v-for="availability in house.availability") {{ availability }}
                .row(style="padding-bottom: 63px")
                    .col-6 
                        .house__name_description Удобства  
                        .house__text_description {{ house.conveniences }} 
                    .col-6 
                        .house__name_description Включено в проживание
                        .house__text_description {{ house.include }}
</template>

<script>
import { ref } from "vue"

import { Swiper, SwiperSlide } from 'swiper/vue';

export default {
    name: "house-detail",
    props: ["house"],
    components: {
        Swiper,
        SwiperSlide,
    },
    setup() {
        let showSliderIcon = ref(true)
        return {
            showSliderIcon
        }
    }
}
</script>

<style scoped>
.house__text_description{
    color: black;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300;
    line-height: 20.33px; 
    max-width: 483px;   
}
.house__name_description{
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
    margin-bottom: 10px;
}
.slider_icon {
    position: absolute;
    bottom: -31px;
    right: 0;
    z-index: 100;
    animation: hand-swipe 2s infinite ease;
}

@keyframes hand-swipe {
    50% {
        transform: rotate(-80deg);
    }

    100% {
        transform: rotate(0deg);
    }
}

.photogalery__name {
    color: #032D28;
    font-size: 11px;
    font-family: 'Lato';
    font-weight: 400;
    display: flex;
    justify-content: center;
    padding: 19px 0px;
}

.photogalery__image {
    border-radius: 30px;
    width: 291px;
    height: 204px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}

.photogalery__card {
    background-color: #fff;
    border-radius: 30px;
}

.swiper {
    position: relative;
}

.house__image {
    border-radius: 30px;
    width: 621px;
    height: 354px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}

.btn_close {
    background-image: url('src/assets/images/btn-close.svg');
    background-repeat: no-repeat;
    background-position: center;
    height: 40px;
    width: 40px;

    &:hover {
        cursor: pointer;
        background-image: url('src/assets/images/btn-close-active.svg');
    }
}

.house_name {
    color: #003C30;
    font-size: 47px;
    font-family: 'Apoc Normal';
    font-weight: 300;
}</style>