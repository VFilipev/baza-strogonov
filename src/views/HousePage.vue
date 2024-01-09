<template lang="pug">
div    
    header-main
    section.house_typ(style="padding-top: 63px")
        .container 
            .row
                .col-12.col-sm-6
                    .d-flex.justify-content-between.align-items-center
                        h4.section_name виды домов 
                        .d-flex.container_icon.align-items-center
                            .circle-left(@click="decSelectHouseIndex")   
                            div(style="display:flex; flex-direction: column; align-items: center" )
                                p.house__name {{ houseList[selectHouseIndex]?.name }}                      
                                .d-flex.gap-2
                                    .house_point(v-for="(house, index) in houseList" :class="{active : index == selectHouseIndex}" @click="selectHouseIndex = index")
                            .circle-right(@click="addSelectHouseIndex")                         
            .card_house__wrapper
                div(v-for="(house, index) in houseList" :key="house.id")                     
                    Transition(name="fade" mode="out-in")
                        div.card_house(v-show="selectHouseIndex == index")                            
                            .row 
                                .col-12.col-sm-6
                                    .row
                                        .col-12
                                            .house__image(:style="{ backgroundImage: `url(${house.img})` }")
                                    .row.row_swiper
                                        .swiper__wrapper(style="position: relative")                  
                                            swiper(slidesPerView="2" :spaceBetween="spaceBetweenSlider")
                                                swiper-slide(v-for="card in house.photo_gallery_set")
                                                    .photogalery__card 
                                                        .photogalery__image(:style="{ backgroundImage: `url(${card.img})`}")
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
                                            .house__text_description {{ house.include }}        
    section.placement 
        .container           
            booking-house(@selLodge='selLodge')
    footerComponent
    Transition(name="modalBottom")
        div.modal-mask(v-show="isShowModalHouse" :class="{active : isShowModalHouse}")  
            house-detail(:house="selectLodge" @modalClose="closeModal")
</template>

<script>
import { formatNumber } from '../components/formatNumber'
import { ref, watch, onMounted } from "vue"
import { Swiper, SwiperSlide } from 'swiper/vue';
import bookingHouse from "../components/bookingHouse.vue";
import houseDetail from "../components/houseDetail.vue";
import footerComponent from "../components/footerComponent.vue";
// import houseList from '../components/houseList'
import headerMain from "../components/headerMain.vue";
import { Lodge } from '../api'
import { useRoute, useRouter } from 'vue-router';

export default {
    name: 'house',
    components: {
        Swiper,
        SwiperSlide,
        headerMain,
        bookingHouse,
        houseDetail,
        footerComponent
    },
    setup() {
        let spaceBetweenSlider = ref(40)
        let selectHouseIndex = ref(0)
        let showSliderIcon = ref(true)
        let selectLodge = ref({})
        let isShowModalHouse = ref(false)
        const route = useRoute()
        const router = useRouter()
        let selLodge = (lodge) => {
            selectLodge.value = lodge
            isShowModalHouse.value = true
        }
        let houseList = ref([])
        const getLodgeList = async () => {
            let res = (await Lodge.getList({ 'avalible': true })).results
            houseList.value = res
            let slug = route.params.slug
            let findIndex = houseList.value.findIndex(l => l.slug == slug)
            selectHouseIndex.value = findIndex
        }
        const closeModal = () => {
            document.body.classList.remove('modal-open')
            isShowModalHouse.value = false
        }
        const decSelectHouseIndex = () => {
            if (selectHouseIndex.value > 0) {
                selectHouseIndex.value--
            } else {
                selectHouseIndex.value = houseList.value.length - 1
            }
        }
        const addSelectHouseIndex = () => {
            if (selectHouseIndex.value == houseList.value.length - 1) {
                selectHouseIndex.value = 0
            } else {
                selectHouseIndex.value++
            }
        }
        watch(()=>selectHouseIndex.value,()=>router.push({name:'house', params:{slug:houseList.value[selectHouseIndex.value]?.slug}}))
        onMounted(() => {
            window.scrollTo({ top: 0, behavior: 'smooth' })
            if (window.innerWidth < 600 || /Mobi/i.test(navigator.userAgent)) {
                spaceBetweenSlider.value = 20
            }
            getLodgeList()
        })
        return {
            selectHouseIndex,
            showSliderIcon,
            selLodge,
            houseList,
            closeModal,
            isShowModalHouse,
            selectLodge,
            formatNumber,
            decSelectHouseIndex,
            addSelectHouseIndex,
            spaceBetweenSlider

        }
    }
}
</script>

<style scoped>
.house_point {
    height: 8px;
    width: 8px;
    border-radius: 50%;
    background-color: transparent;
    border: 1px #005D4B solid;

    &.active {
        background-color: #005D4B;
    }

    &:hover {
        cursor: pointer;
    }
}

.row_swiper {
    margin-top: 40px;
}

.modal-mask {
    position: fixed;
    top: 0;
    height: 100vh;
    width: 100%;
    background-color: #ECE8E3;
    z-index: 200;
}

/* HOUSE DETAIL */
.modalBottom-enter-active {
    animation: animatebottom 1s;
}

.modalBottom-leave-active {
    animation: animatebottom 1s reverse;
}

@keyframes animatebottom {
    from {
        top: 100%;
        opacity: 0;
    }

    to {
        top: 0%;
        opacity: 1;
    }
}

/* ANIMATED FOR HOUSECARD */
.card_house__wrapper {
    position: relative;
    min-height: 770px;
    margin-top: 34px;
}

.card_house {
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 1.2s ease-out;

}

/* SWIPER */

.swiper {
    position: relative;
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

/* ГЛЭМПИНГ */

.circle-left {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    background-color: #005D4B;
    background-image: url("../assets/images-house/arrow-left.svg");
    background-repeat: no-repeat;
    background-position: center;

    &:hover {
        background-color: #fff;
        border: 1px #005D4B solid;
        background-image: url("src/assets/images-house/arrow-left-hover.svg");
        cursor: pointer;
    }
}

.circle-right {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    background-color: #005D4B;
    background-image: url("../assets/images-house/arrow-right.svg");
    background-repeat: no-repeat;
    background-position: center;

    &:hover {
        background-color: #fff;
        border: 1px #005D4B solid;
        background-image: url("src/assets/images-house/arrow-right-hover.svg");
        cursor: pointer;
    }
}

.circle:hover {
    cursor: pointer;
    user-select: none
}

.circle__arrow_icon {
    user-select: none
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

.house__text_description {
    color: black;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300;
    line-height: 20.33px;
    max-width: 483px;
}

.photogalery {
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
    margin-top: 22px;
    margin-bottom: 10px;
}

.house__name_description {
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
    margin-bottom: 10px;
}

.photogalery__image {
    border-radius: 30px;
    width: 100%;
    height: 204px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
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

.photogalery__card {
    background-color: #fff;
    border-radius: 30px;
}

.house__image {
    border-radius: 30px;
    width: 621px;
    height: 354px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}

.house__name {
    width: 160px;
    display: flex;
    justify-content: center;
    color: #003731;
    font-size: 17px;
    font-family: Lato;
    font-weight: 400;
    margin-bottom: 0px;
}

.section_name {
    color: #003C30;
    font-size: 47px;
    font-family: 'Apoc Normal';
    font-weight: 300;
}

.house_typ {
    background-color: #F5F3F1;
}

@media (max-width: 1200px) {
    .section_name {
        font-size: 25px;
    }

    .circle-left {
        width: 35px;
        height: 35px;
    }

    .circle-right {
        width: 35px;
        height: 35px;
    }

    .house__image {
        width: 100%;
        height: 200px;
    }

    .photogalery__image {
        height: 130px;
    }

    .row_swiper {
        margin-top: 10px;
    }

    .photogalery__name {
        padding: 5px 0px;
    }

    .house__text_description {
        font-size: 12px;
        line-height: 15px;

        & p {
            margin-bottom: 0;
        }
    }

    .house__name_description {
        margin-bottom: 0px;
        font-size: 15px;
    }
}
</style>