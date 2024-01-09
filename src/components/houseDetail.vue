<template lang="pug">
div.focus-none(tabindex='-1' id="modal" @keyup.right="next" @keyup.left="prev" @keyup.esc="show = false")
    .container 
        .row.d-flex.justify-content-between.align-items-center.modal-header
            .col-6.col-sm-4.house_name {{ house.name }}
            button.btn_close.d-flex(@click="$emit('modalClose'),showSliderIcon = true")        
        .row.d-flex.d-sm-none.mb-4
            .col-12
                .house__name_description Стоимость     
                    template(v-if="house.price_set")          
                        .row_cost
                            .house__text_description Будни (пн-чт)
                            .house__text_description {{ formatNumber(house.price_set[1]) + ' р.' }}
                        .row_cost
                            .house__text_description Выходные (пт-сб-вс) и праздничные дни
                            .house__text_description {{ formatNumber(house.price_set[7]) + ' р.' }}
                    .row_cost(v-for="cost in house.special_price_set")
                        .house__text_description {{ cost.name }}
                        .house__text_description {{ formatNumber(cost.cost) + ' р.'}}
        .row 
            .col-12.col-sm-6
                .row
                    .col-12
                        .house__image(:style="{ backgroundImage: `url(${house.img})` }")
                .row.row_swiper
                    .swiper__wrapper(style="position: relative")                  
                        swiper(slidesPerView="2" :spaceBetween="spaceBetweenSlider" @slideChange="showSliderIcon = false")
                            swiper-slide(v-for="(card, index) in house.photo_gallery_set")
                                .photogalery__card 
                                    .photogalery__image(@click="selectPhoto(index)" :style="{ backgroundImage: `url(${card.img})`}")
                                    .photogalery__name {{ card.name }}                            
                        img.slider_icon(v-if="showSliderIcon" src="../assets/images/slider-icon.svg")
            .col-12.col-sm-6
                .row.d-none.d-sm-flex(style="margin-bottom:64px")
                    .col-12
                        .house__name_description Стоимость                            
                        .row_cost(v-for="cost in house.price_set")                            
                            .house__text_description {{ cost.name }}
                            .house__text_description {{ formatNumber(cost.cost) + ' р.' }}
                        .row_cost(v-for="cost in house.special_price_set")                            
                            .house__text_description {{ cost.name }}
                            .house__text_description {{ formatNumber(cost.cost) + ' р.'}}
                .row.mt-4.mt-sm-0.row_info 
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
    transition(name="modal")
        .modal-mask(v-if="show" aria-hidden="true")
           .modal-wrapper( ref="modal" @click="show=false"  role="dialog" aria-hidden="true")
                .modal-container-photo(@click.stop="" role="document")
                  .modal-body2-photo
                    svg(v-if='activIndex>0' @click="prev" width="36px" height="36px" class="next-btn" viewBox="0 0 24 24") 
                        path(d="M15.41 16.09l-4.58-4.59 4.58-4.59L14 5.5l-6 6 6 6z")
                    img(:src='activPhoto?.img' class="active-photo mx-auto d-block" )
                    svg(v-if='house.photo_gallery_set.length > activIndex+1' @click="next" width="36px" height="36px" class="next-btn" viewBox="0 0 24 24") <path d="M8.59 16.34l4.58-4.59-4.58-4.59L10 5.75l6 6-6 6z"></path>
</template>

<script>
import { ref, onMounted } from "vue";
import { formatNumber } from './formatNumber';
import { Swiper, SwiperSlide } from 'swiper/vue';


export default {
    name: "house-detail",
    props: ["house"],
    components: {
        Swiper,
        SwiperSlide,
    },
    setup(props) {
        let showSliderIcon = ref(true)       
        let spaceBetweenSlider = ref(40) 
        let activIndex = ref(-1)
        let activPhoto = ref({})
        let show = ref(false)
        const prev = () =>{
            if (activIndex.value > 0){
                activIndex.value -= 1
                activPhoto.value = props.house.photo_gallery_set[activIndex.value]
            }
            
        }
        const next = () =>{
            if (activIndex.value < props.house.photo_gallery_set.length - 1){
                activIndex.value+=1
                activPhoto.value = props.house.photo_gallery_set[activIndex.value]
            }            
        }
        const selectPhoto = (index) => {
            show.value = true
            let el = document.getElementById('modal')
            el.focus()
            activIndex.value = index
            activPhoto.value = props.house.photo_gallery_set[activIndex.value]
        }        
        onMounted(() => {
            if(window.innerWidth < 600 || /Mobi/i.test(navigator.userAgent)){
                spaceBetweenSlider.value = 20
            }
            console.log();
        })
        return {
            showSliderIcon,
            formatNumber,
            spaceBetweenSlider,
            selectPhoto,
            show,
            prev,
            next,
            activPhoto,
            activIndex
            
        }
    }
}
</script>

<style scoped>
.focus-none{
  outline: none;
  box-shadow: none;
}
.next-btn {
    background: #fff;
    border-radius: 20px;
    z-index: 999;
}
.active-photo{
    max-width:90%;
    max-height:100%
}
.modal-body2-photo
{
    height: calc(95vh );
    min-height: 600px;
    overflow-y: auto;
    overflow-x:hidden;
    padding:0px;
    align-items: center;
    display: flex;
}
.modal-container-photo{

    max-width:1000px;
    margin:15px auto;
}
.next-btn{
background: white;
border-radius: 20px;
z-index:10
}
.galery-title{
    margin-top:50px;
    margin-left:5px
}
.modal-mask{
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,.5);
    display: table;

}
.modal-wrapper {
    display: table-cell;
}
.row_cost {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.row_cost:not(:last-child) {
    border-bottom: 1px #005D4B solid;
    padding-bottom: 14px;
}

.row_cost:not(:first-child) {
    padding-top: 14px;
}
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
    &:hover{
        cursor: pointer;
    }
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
    width: 100%;
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
}
.modal-header{
    padding-top:63px;
}
.row_swiper{
    margin-top:40px;
}
.row_info{
    margin-bottom: 31px;
}
@media (max-width: 1200px) {
    .modal-header{
        padding-top: 0;
    }
}

@media (max-width: 1200px) {
.house_name{
    font-size: 25px;
}
.row_cost{
    display: flex;
    justify-content: space-between;    
    align-items: center;    
}
.row_cost:not(:last-child){
    border-bottom: 1px #005D4B solid;
    padding-bottom: 5px;
}
.row_cost:not(:first-child){
    padding-top: 5px;
}
.house__name_description{
    margin-bottom: 0px;
    font-size: 15px;
}
.modal-header{
    position: sticky;
    top: 0;
    transform: translateY(-1px);
    background-color: #ECE8E3;
    z-index: 100;
}
.row_swiper{
    margin-top:10px;
}
.house__image{
    width: 100%;
    height: 200px;
}
.photogalery__name{
    padding: 5px 0px;
}
.photogalery__image{
    height: 130px;
}
.house__text_description{
    font-size: 12px;
    line-height: 15px;
    & p{
        margin-bottom: 0;    
    }
}
.row_info{
    margin-bottom: 10px;
}
}
</style>