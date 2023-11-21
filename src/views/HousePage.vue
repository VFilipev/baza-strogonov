<template lang="pug">
div    
    header.p-20    
        .container
            .row.align-items-center
                .col-5
                    router-link(to="/")
                        img(src="../assets/images/logo2.svg")
                ul.header_sticky__nav.col-2.offset-3.d-flex
                    router-link(to="/house" tag="li" class="header_sticky__nav_link") дома
                    //- router-link(to="/" tag="li" class="header_sticky__nav_link") активный отдых
                    router-link(to="/uslugi" tag="li" class="header_sticky__nav_link") услуги
                .header_sticky__icon_feed_back.col-2
                    img(src="../assets/images/telefon2.svg")
                    button забронировать
    section.house_typ(style="padding-top: 63px")
        .container 
            .section_row
                h4.section_name виды домов 
                .d-flex.container_icon
                    .circle-left(@click="selectHouseIndex--")                        
                    .circle-right(@click="selectHouseIndex++")                         
            .card_house__wrapper
                div(v-for="(house, index) in houseList" :key="house.id")                     
                    Transition(name="fade" mode="out-in")
                        div.card_house(v-show="selectHouseIndex == index")
                            .row                         
                                p.house__name {{ house.name }} 
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
        .container
            .section_row
                h4.section_name глэмпинг
                .d-flex.container_icon
                    .circle-left                        
                    .circle-right                        
            .row 
                .col-6
                    .row(style="margin-bottom:64px")
                        .col-6
                            .house__name_description Описание 
                            .house__text_description двухэтажный деревянный дом, где могут разместиться до 14 человек. 3 просторные комнаты, в которых будет удобно и парам, и семьям с детьми.
                        .col-6
                            .house__name_description Стоимость
                            .row_cost 
                                .house__text_description будни (пн-чт)
                                .house__text_description 10 000 р.
                            .row_cost 
                                .house__text_description выходные (пт-сб-вс) <br> и праздничные дни  
                                .house__text_description 15 000 р.
                            .row_cost 
                                .house__text_description Новый год 2024 (с 31 декабря <br> по 2 января) 2-е суток 
                                .house__text_description 95 000 р.
                            .row_cost 
                                .house__text_description с 2 по 7 января 2024 года <br> (сутки)
                                .house__text_description 30 000 р.
                            .row_cost 
                                .house__text_description стоимость при бронирова- <br> нии 2-х и более суток <br> (с 2 по 7 января 2024 года)
                                .house__text_description 25 000 р.
                    .row(style="margin-bottom:31px") 
                        .col-6 
                            .house__name_description Удобства  
                            .house__text_description кухня - полный комплект посуды на 14 человек, холодильник, обеденный стол, электроплита с духовым шкафом, микроволновая печь, электрочайник, санузел - горячая и холодная вода, музыкальный центр, 4 телевизора
                        .col-6 
                            .house__name_description Доступность
                            .house__text_description до воды 150 м <br> до бани 50 м <br> до беседки 5 м
                    .row 
                        .col-6 
                            .house__name_description Включено в проживание
                            .house__text_description пользование спортивными и детскими площадками, надувным аквапарком, пользование мангалом и решеткой, охраняемая парковка, охраняемый причал                        
                .col-6
                    p.house__name Для двоих
                    .house__image(style="background-image: url(src/assets/images-house/house-3.png)")
            .row 
                p.photogalery Фотогалерея
            .row
                .col-4
                    .glamping__photogalery__card
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-2.png)")
                        .photogalery__name веранда
                .col-4
                    .glamping__photogalery__card 
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-3.png)")
                        .photogalery__name внутри
                .col-4
                    .glamping__photogalery__card 
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-4.png)")
                        .photogalery__name спальные места
            .photogalery_next
                .photogalery_next__text далее
                .photogalery_next__icon 
                    img(src="../assets/images-house/arrow-next.svg")
    section.placement 
        .container           
            h4.about_us__header бронирование
            .placement__form.row
                .date_time.date_time__icon.date_time__text.col-3
                    input.date_time__input
                .date_time.date_time__icon.date_time_end__text.col-3
                    input.date_time__input
                .quantity_guests.quantity_guests__text  
                    input.quantity_guests__input
                .checkbox_container
                    div.checkbox__header показать свободные:
                    input.checkbox__input(type="checkbox" id="house")
                    label.checkbox__name(for="house") дома
                    input.checkbox__input(type="checkbox" id="glamping")
                    label.checkbox__name(for="glamping" style="margin-left:10px") глемпинг
                button.placement__form__button_search найти
            .row.placement__cantainer_card
                .col-4 
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house1-1.png)")
                        .container_info-graph
                            .house_name Дом Кузнеца
                            .wrapper_cost_capacity
                                .house_cost ₽ 10000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 11 чел
                        .container_footer 
                            .footer_text 2 смежные и 2 изолированые спальни, просторная кухня-гостиная, санузел
                            .footer_button забронировать
                .col-4 
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house2-1.png)")
                        .container_info-graph
                            .house_name Дом Мельника
                            .wrapper_cost_capacity
                                .house_cost ₽ 10000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 11 чел
                        .container_footer 
                            .footer_text 3 изолированные спальни, просторная кухня-гостиная с диваном, санузел
                            .footer_button забронировать
                .col-4 
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house3-1.png);background-position: 0px -170px")
                        .container_info-graph
                            .house_name Дом Ямщика
                            .wrapper_cost_capacity
                                .house_cost ₽ 10000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 14 чел
                        .container_footer 
                            .footer_text 3 изолированные спальни, просторная кухня-гостиная с диваном и два санузла
                            .footer_button забронировать
                            .row.placement__cantainer_card
                .col-4(style="margin-top: 41px")
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house4-1.png)")
                        .container_info-graph
                            .house_name Дом Охотника
                            .wrapper_cost_capacity
                                .house_cost ₽ 25000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 40 чел
                        .container_footer 
                            .footer_text Дом полностью + большая веранда или половина дома + кафе и малая веранда
                            .footer_button забронировать
                .col-4(style="margin-top: 41px")
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house5-1.png)")
                        .container_info-graph
                            .house_name Дом Рыбака
                            .wrapper_cost_capacity
                                .house_cost ₽ 5500
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 4 чел
                        .container_footer 
                            .footer_text 2 изолированные спальни, просторная кухня-гостиная с диваном и два санузел
                            .footer_button забронировать
                .col-4(style="margin-top: 41px; margin-bottom:95px")
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house6-1.png);background-position: 0px -114px")
                        .container_info-graph
                            .house_name Дом Гончара(1 этаж)
                            .wrapper_cost_capacity
                                .house_cost ₽ 5000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 6 чел
                        .container_footer 
                            .footer_text  изолированные спальни, просторная кухня-гостиная с диваном и санузел
                            .footer_button забронировать
    footer.footer
        .container
            .footer_container
                div 2023 @ СТРОГАНОВСКИЕ ПРОСТОРЫ
                div Пермь. Официальный сайт.
</template>

<script>
import { ref, watch } from "vue"
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';


import houseList from '../components/houseList'

export default {
    name: 'house-page',
    components: {
      Swiper,
      SwiperSlide,
    },
    setup () {                
        let selectHouseIndex = ref(0)        
        let showSliderIcon = ref(true)                   
        watch(()=>selectHouseIndex.value,()=>{
            if(selectHouseIndex.value < 0){
                selectHouseIndex.value = houseList.length - 1
            }
            if(selectHouseIndex.value == houseList.length){
                selectHouseIndex.value = 0
            }                                 
        })             
        return {
            showSliderIcon,                
            selectHouseIndex,
            showSliderIcon,
            houseList 
        }
    }
}
</script>

<style scoped>
/* ANIMATED FOR HOUSECARD */
.card_house__wrapper{
    position: relative;  
    min-height: 770px;  
}
.card_house{
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
}
.fade-enter-from,
.fade-leave-to{
  opacity: 0;  
}

.fade-enter-active,
.fade-leave-active{
  transition: opacity 1.2s ease-out;
  
}
/* SWIPER */

.swiper{    
    position: relative;
}
.slider_icon {
    position: absolute;
    bottom: -31px;
    right: 0;
    z-index: 100;
    animation:hand-swipe 2s infinite ease;
}
@keyframes hand-swipe { 
    50% {          
        transform:rotate(-80deg); 
    } 
    100%{
        transform:rotate(0deg); 
    }
}
/* ГЛЭМПИНГ */
.glamping__photogalery__card{
    background-color: #F5F3F1;
    border-radius: 30px;
}
.house_typ_glamping{
    padding-top: 72px;
}
.house_typ_glamping{
    background-color: #fff;
}
.circle-left{
    width: 55px;
    height: 55px;
    border-radius: 50%;
    background-color: #005D4B;
    background-image: url("../assets/images-house/arrow-left.svg");
    background-repeat: no-repeat;
    background-position: center;
    &:hover{
        background-color: #fff;
        border: 1px #005D4B solid;
        background-image: url("src/assets/images-house/arrow-left-hover.svg");        
        cursor: pointer;
    }
}
.circle-right{
    width: 55px;
    height: 55px;
    border-radius: 50%;
    background-color: #005D4B;    
    background-image: url("../assets/images-house/arrow-right.svg");
    background-repeat: no-repeat;
    background-position: center;
    &:hover{
        background-color: #fff;
        border: 1px #005D4B solid;        
        background-image: url("src/assets/images-house/arrow-right-hover.svg");        
        cursor: pointer;
    }
}
.circle:hover{
    cursor: pointer;
    user-select: none
}
.circle__arrow_icon{
    user-select: none
}
.row_cost{
    display: flex;
    justify-content: space-between;    
    align-items: center;    
}
.row_cost:not(:last-child){
    border-bottom: 1px #005D4B solid;
    padding-bottom: 14px;
}
.row_cost:not(:first-child){
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
.photogalery{
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
    margin-top: 22px;
    margin-bottom: 10px;
}
.house__name_description{
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
    margin-bottom: 10px;
}
.photogalery_next{
    display: flex;
    justify-content: flex-end;
    margin-top: 8px;
    padding-bottom: 70px;
}
.photogalery__image{
    border-radius: 30px;
    width: 291px;
    height: 204px;    
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
.photogalery__name{
    color: #032D28;
    font-size: 11px;
    font-family: 'Lato';
    font-weight: 400;
    display: flex;
    justify-content: center;
    padding: 19px 0px;
}
.photogalery__card{
    background-color: #fff;
    border-radius: 30px;
}
.house__image{
    border-radius: 30px;
    width: 621px;
    height: 354px;    
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
.house__name{
    color: #003731;
    font-size: 17px;
    font-family: Lato;
    font-weight: 400;
    margin-bottom: 18px;
}
.section_name{
    color: #003C30;
    font-size: 47px;
    font-family: 'Apoc Normal';
    font-weight: 300;    
}
.section_row{
    margin-bottom: 45px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.house_typ{
    background-color: #F5F3F1;
}
.p-20{
    padding: 20px 0px;
}
</style>