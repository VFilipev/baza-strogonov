<template lang="pug">
div.color_bg
    section.first_page        
        .container__first_page            
            template(v-for="(photo, index) in photoWinterList" ) 
                img.uslugi-photo(:src="photo.photo" :class="{ active : index == selPhoto }")
            .container__header
                .container
                    .header
                        .row.align-items-center
                            .logo.col-5
                                router-link(to="/")
                                    img(src="../assets/images/logo.png")
                            .header__nav.d-flex.col-3.offset-2
                                router-link(to="/house", tag="a", class="header__nav__link") дома
                                router-link(to="/uslugi", tag="a", class="header__nav__link") активный отдых / услуги
                            .header__nav.d-flex.col-2     
                                a(href="tel:+79026439294")                       
                                    img(src='../assets/images/telefon.svg')
                                button.header__nav__link.header__nav__button забронировать
                    .row.d-flex.justify-content-between(style="margin-top: 11px")
                        .col-4.first_page__h1 зимние <br> развлечения
                        .col-4.first_page__h2 {{ photoWinterList[selPhoto].text }}                     
    section.uslugi_list
        .container(style="margin-top:93px; padding-bottom: 95px")
            .row                
                template(v-for="uslugi in uslugiList")
                    .col-2 
                        .uslugi_card 
                            .uslugi_card__img(:style="{ backgroundImage: `url(${uslugi.photo})` }")
                            .uslugi_card__text {{ uslugi.text }}
    section.second_page 
        .container__second_page
            template(v-for="(photo, index) in photoSummerList" ) 
                img.uslugi-photo(:src="photo.photo" :class="{ active : index == selPhotoSummer }")
            .container(style="padding-top: 721px")                
                .container__header
                    .container
                        .row.d-flex.justify-content-between(style="margin-top: 0px")
                            .col-4.first_page__h2 {{ photoSummerList[selPhotoSummer].text }} 
                            .col-4
                                .first_page__h1 летние <br> развлечения                                
    section.uslugi_list
        .container(style="margin-top:93px; padding-bottom: 95px")
            .row                
                template(v-for="uslugi in uslugiSummerList")
                    .col-2 
                        .uslugi_card 
                            .uslugi_card__img(:style="{ backgroundImage: `url(${uslugi.photo})` }")
                            .uslugi_card__text {{ uslugi.text }}
    section.service_section
        .container         
            .row.service     
                .service__header.col-2 услуги
            .row(style="padding-bottom: 94px") 
                .col-6
                    p.service__name_typ Активный отдых                    
                    .service__item(v-for="item in recreation")
                        .service__name {{ item.name }}
                        .service__cost {{ item.cost }}                    
                .col-6
                    p Банные процедуры
                    .service__item(v-for="item in bathProcedures") 
                        .service__name {{ item.name }}
                        .service__cost {{ item.cost }}    
    footerComponent
</template>

<script>
import { ref, onMounted } from "vue"
import footerComponent from "../components/footerComponent.vue"
import { recreation, bathProcedures } from "../components/serviceList";

export default {
    name: 'uslugi-page',
    components: {
        footerComponent
    },
    setup() {
        const photoWinterList = [
            {photo: 'src/assets/images-uslugi/main-page-1.png',
            text: 'по заснеженным полям тут и там: получите незабываемые впечатления от зимнего катания — аренда снегохода от 30 минут'
            },
            {photo: 'src/assets/images-uslugi/main-page-7.png',
            text: 'чан — идеальный вариант для расслабления и рефреша в сердце природы после трудовых будней'
            },
            {photo: 'src/assets/images-uslugi/main-page-3.png',
            text: 'почувствуйте себя искусным фигуристом, прокатившись с ветерком на нашем катке — аренда коньков от 150 рублей'
            },
        ]        
        const photoSummerList = [
            {photo: 'src/assets/images-uslugi/main-page-4.png',
            text: 'увлекательный поход за грибами на квадроцикле: познайте удивительную природу Пермсокого края — аренда квадроцикла от 30 минут'
            },
            {photo: 'src/assets/images-uslugi/main-page-5.png',
            text: 'настоящее уединение с природой — это определённо про катание на сапах по  реке  Каме,  у вас будет захватывать дух, но мы общаем, что вам понравится'
            },
            {photo: 'src/assets/images-uslugi/main-page-6.png',
            text: '“Душистый пар не только тело, но и душу лечит”. Наша баня  это место, где все ваши заботы — и усталость обязательно испарятся'
            },
        ]
        const uslugiList = [
            {photo: 'src/assets/images-uslugi/images-1.png',
            text: 'снегоход'
            },
            {photo: 'src/assets/images-uslugi/images-2.png',
            text: 'чан'
            },
            {photo: 'src/assets/images-uslugi/images-3.png',
            text: 'баня'
            },
            {photo: 'src/assets/images-uslugi/images-4.png',
            text: 'лыжи'
            },
            {photo: 'src/assets/images-uslugi/images-5.png',
            text: 'коньки'
            },
            {photo: 'src/assets/images-uslugi/images-6.png',
            text: 'каток'
            },
        ]
        const uslugiSummerList = [
            {photo: 'src/assets/images-uslugi/images-7.png',
            text: 'баня и чан'
            },
            {photo: 'src/assets/images-uslugi/images-8.png',
            text: 'спортивные игры'
            },
            {photo: 'src/assets/images-uslugi/images-9.png',
            text: 'квадроциклы'
            },
            {photo: 'src/assets/images-uslugi/images-10.png',
            text: 'сапы'
            },
            {photo: 'src/assets/images-uslugi/images-11.png',
            text: 'контактный зоопарк'
            },
            {photo: 'src/assets/images-uslugi/images-12.png',
            text: 'гидроциклы'
            },
        ]
        let selPhoto = ref(0)
        let selPhotoSummer = ref(0)
        let timerId
        const maxPhoto = photoWinterList.length
        const changeSelPhotoInc = () => {
            clearTimeout(timerId)
            incSelPhoto()
            timerId = setTimeout(sliderPhoto, 8000)
        }
        const incSelPhoto = () => {
            if (selPhoto.value < maxPhoto - 1){
                selPhoto.value += 1
            }
            else {
                selPhoto.value = 0
            }
        } 
        const incSelPhotoSummer = () => {
            if (selPhotoSummer.value < 2){
                selPhotoSummer.value += 1
            }
            else {
                selPhotoSummer.value = 0
            }
        }        
        const sliderPhoto = () => {
            incSelPhoto()
            timerId = setTimeout(sliderPhoto, 8000)
        }
        onMounted(() => {
            setTimeout(sliderPhoto, 8000)
        })
        return {
            photoWinterList, 
            incSelPhoto,
            selPhoto,
            changeSelPhotoInc,
            uslugiList,
            selPhotoSummer,
            photoSummerList,
            incSelPhotoSummer,
            uslugiSummerList,
            recreation, 
            bathProcedures
        }
    }
}
</script>

<style scoped>
.container__header{
    position: relative;
    z-index: 100;
}
.service_section{
    background-color: #fff;
}
.description{
    position: absolute;
    bottom: 100px;
}
.container__second_page{
    min-height: 100vh;
    width: 100%;
    position: relative;
}
.uslugi_card__text{
    display: flex;
    justify-content: center;
    color: #032D28;
    font-size: 11px;
    font-family: Lato;
    font-weight: 400;
    padding-top: 15px;
    padding-bottom: 15px;
}
.uslugi_card__img{
    border-radius: 30px;
    width: 180px;
    height: 196px;    
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
.uslugi_card{
    
    width: 180px;
    background-color: #ECE8E3;
    border-radius: 30px;
}
.color_bg{
    background-color: #f8f5f2;
}
a.header__nav__link {
    text-decoration: none;
    color: #fff;
}
.header{
    padding-top: 42px;
    margin-bottom: 481px;
}
.container__first_page {
min-height: 100vh;
min-width: 100%;
position: relative;
}
.overlay {
    background-color: rgb(0, 0, 0, 0.6);
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 10;
}
img.uslugi-photo {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;    
    opacity: 0;
    transition: opacity .8s ease-in-out;
}
img.uslugi-photo.active{
    opacity: 1;
}
img.first_page__arrow_icon:hover{
    cursor: pointer;
}
</style>