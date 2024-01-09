<template lang="pug">

header.header_sticky(:class="{'active' : isHeaderShow()}")         
    .container
        .header_sticky__container.row.align-items-center
            .header_sticky__logo.col-2.col-sm-5
                img(src="../assets/images/logo2.svg")
            ul.header_sticky__nav.col-6.col-sm-3.offset-sm-2.d-flex
                router-link(to="/house/dom-kuznetsa" tag="li" class="header_sticky__nav_link") дома                    
                router-link(to="/uslugi" tag="li" class="header_sticky__nav_link") активный отдых / услуги
            .header_sticky__icon_feed_back.col-2
                a(href="tel:+79026439294")
                    img(src="../assets/images/telefon2.svg")
                button забронировать
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue"


let isScroll = ref(false)
let distance = ref(0)
const isHeaderShow = () => {
    if (isScroll.value == true) {
        let el
        if(window.innerWidth < 600 || /Mobi/i.test(navigator.userAgent)){        
            el = document.getElementById('aboutUsMobile')
        }else{
            el = document.getElementById('aboutUs')
        }            
        distance.value = el.offsetTop - window.scrollY        
        if (distance.value <= 300) {
            return true
        }
        else {
            return false
        }
    }
    return false
}
onMounted(() => {
    if(window.innerWidth < 600 || /Mobi/i.test(navigator.userAgent)){        
    }    
    isScroll.value = true
    window.addEventListener('scroll', (event) => { isHeaderShow() });    
})
onUnmounted(() => {
    isScroll.value = false
    window.removeEventListener('scroll', (event) => { fil() });
})
</script>

<style scoped>
.header_sticky {
    transform: translateY(-160px);
    transition-duration: 1s;
    transition-property: all;
    opacity: 0;
    position: fixed;
    width: 100%;
    top: 0;

    &.active {
        position: fixed;
        background-color: #fff;
        padding-top: 20px;
        padding-bottom: 20px;
        top: 0;
        opacity: 1;
        z-index: 150;
        transform: translateY(0px);
    }
}

.header_sticky__nav {
    display: flex;
    gap: 11px;
    font-family: 'Lato';
    font-weight: 300;
    font-size: 17px;
    color: black;
    margin-bottom: 0;
}
.header_sticky__nav_link {
    text-decoration: none;
    color: black;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 300;

    &:after {
        display: block;
        content: '';
        border-bottom: solid 1px black;
        transform: scaleX(0);
        transition: transform 250ms ease-in-out;
    }

    &:hover:after {
        transform: scaleX(1);
    }

}

.header_sticky__container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header_sticky__icon_feed_back {
    display: flex;
    justify-content: flex-end;
    padding-right: 20px;
}

.header_sticky__icon_feed_back img {
    margin-right: 8px;
}

.header_sticky__icon_feed_back button {
    background-color: rgba(0, 93, 75, 1);
    color: #fff;
    border: 0px;
    border-radius: 35px;
}

@media (max-width: 1200px){
.header_sticky__logo img{
    width: 68px;
    height: 26px;
}
.header_sticky {
    /* width: 100wh; */
    &.active{
        padding-top: 15px;
        padding-bottom: 15px;

    }
}
.header_sticky__nav_link{
    font-size: 10px;
}
.header_sticky__icon_feed_back{
    font-size: 10px;
}
.header_sticky__icon_feed_back a img{
    width: 16px;
}
.header_sticky__icon_feed_back{
    padding-right: calc(var(--bs-gutter-x) * 0.5);
}
}
</style>