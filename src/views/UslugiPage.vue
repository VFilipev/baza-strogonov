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
                            .header__nav.d-flex.col-3.offset-2.d-none.d-sm-flex
                                router-link(to="/house/dom-kuznetsa", tag="a", class="header__nav__link") дома
                                router-link(to="/uslugi", tag="a", class="header__nav__link") активный отдых / услуги
                            .header__nav.d-flex.col-2.d-none.d-sm-flex     
                                a(href="tel:+79026439294")                       
                                    img(src='../assets/images/telefon.svg')
                                button.header__nav__link.header__nav__button забронировать
                    .row.d-flex.justify-content-between(style="margin-top: 11px")
                        .first_page__h1.col-xs-12.col-sm-4.col-xxl-4 зимние <br> развлечения
                        .first_page__h2.col-xs-12.col-sm-4.col-xxl-4 {{ photoWinterList[selPhoto].text }}                     
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
        serviceList
    footerComponent
</template>

<script>
import { ref, onMounted } from "vue"
import footerComponent from "../components/footerComponent.vue"
import serviceList from "../components/serviceList.vue"
import { uslugiList, uslugiSummerList, photoWinterList, photoSummerList  } from "../components/serviceList"

export default {
    name: 'uslugi-page',
    components: {
        footerComponent,
        serviceList
    },
    setup() {        
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
        const sliderPhotoSummer = () => {
            incSelPhotoSummer()
            timerId = setTimeout(sliderPhotoSummer, 8000)
        }
        onMounted(() => {
            window.scrollTo({ top: 0, behavior: 'smooth' })
            setTimeout(sliderPhoto, 8000)
            setTimeout(sliderPhotoSummer, 8000)
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
            uslugiSummerList
        }
    }
}
</script>

<style scoped>
.first_page__h2 {
    font-family: 'Lato';
    font-size: 17px;
    color: #fff;
    line-height: 23px;
}
.first_page__h1 {
    font-family: 'Apoc Normal';
    font-weight: 400;
    font-size: 30px;
    color: #fff;
    line-height: 35px;
    letter-spacing: 2px;
}
a.header__nav__link {
    text-decoration: none;
    color: #fff;
    opacity: .8;

    &:hover {
        opacity: 1;
    }

    &:hover:after {
        transform: scaleX(1);
    }
}
a.header__nav__link:after {
    display: block;
    content: '';
    border-bottom: solid 1px #fff;
    transform: scaleX(0);
    transition: transform 250ms ease-in-out;
}
.header__nav {
    color: #fff;
    gap: 15px;
}

.header__nav__link {
    font-family: 'Lato';
    font-size: 17px;
}
button.header__nav__button {
    background-color: transparent;
    border: 1px solid #fff;
    color: #fff;
    border-radius: 35px;
    transition: background-color 0.4s ease-in-out, border 250ms ease-in-out;
    text-decoration: none;

    &:hover {
        background-color: #003731;
        border: 1px solid transparent
    }
}
.container__header{
    position: relative;
    z-index: 100;
}
.service_section{
    padding-top: 75px;
    background-color: #fff;
}
.description{
    position: absolute;
    bottom: 100px;
}
.container__second_page{
    min-height: 100svh;
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
min-height: 100svh;
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