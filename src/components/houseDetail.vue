<template lang="pug">
div
    .container 
        .row.d-flex.justify-content-between.align-items-center(style="padding-top:63px")
            .col-4.house_name {{ house.name }}
            button.btn_close.d-flex(@click="$emit('modalClose'),showSliderIcon = true")        
        .row 
            .col-6
                .row
                    .col-12
                        .house__image(:style="{ backgroundImage: `url(${house.img})` }")
                .row(style="margin-top:40px")
                    .swiper__wrapper(style="position: relative")                  
                        swiper(slidesPerView="2" :spaceBetween="40" @slideChange="showSliderIcon = false")
                            swiper-slide(v-for="card in house.photo_gallery_set")
                                .photogalery__card 
                                    .photogalery__image(:style="{ backgroundImage: `url(${card.img})`}")
                                    .photogalery__name {{ card.name }}                            
                        img.slider_icon(v-if="showSliderIcon" src="../assets/images/slider-icon.svg")
            .col-6
                .row(style="margin-bottom:64px")                          
                    .col-12
                        .house__name_description Стоимость                            
                        .row_cost(v-for="cost in house.price_set")                            
                            .house__text_description {{ cost.name }}
                            .house__text_description {{ formatNumber(cost.cost) + ' р.' }}
                        .row_cost(v-for="cost in house.special_price_set")                            
                            .house__text_description {{ cost.name }}
                            .house__text_description {{ formatNumber(cost.cost) + ' р.'}}
                .row(style="margin-bottom:31px") 
                    .col-6
                        .house__name_description Описание 
                        .house__text_description {{ house.description }} 
                    .col-6 
                        .house__name_description Доступность
                        .house__text_description
                            p(v-for="availability in house.availability_set") {{ availability.name }}
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
import { formatNumber } from './formatNumber'

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
            showSliderIcon,
            formatNumber
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
    width: 100%;
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

button.btn_close {
    background-image: url('src/assets/images/btn-close.svg');
    background-repeat: no-repeat;
    background-position: center;
    height: 40px;
    width: 40px;
    border: 0;
    background-color: transparent;
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