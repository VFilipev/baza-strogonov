<template lang="pug">
div        
    div.container(style="margin-top:300px")
        .row 
            .col-3
                .card(style="background: #F5F3F1;")               
                    .card__header
                        .card__user_photo-form
                            label(class="input-file")
                                input(type="file" name="file" @change="handleFileUpload")
                                span(:style="[photoUser ? {'background-image': 'url(' + previewFilePath + ')', 'background-size': 'cover'} :'']")
                        .card__user_container
                            .card__user_name 
                                input.card__input_user_name(placeholder="ФИО")
                            star-rating(:star-size="13" :animate="true" :show-rating="false")
                    .card__body.card_form
                        textarea.card__input(placeholder="Введите текст..." rows="4")
                        button.card_button оставить отзыв   
    //-     .input_number_wrapper
    //-         .input_number__prefix
    //-             button.prefix_btn(@click="dec")
    //-                 img(src="../assets/images/prefix.svg")
    //-         .input_number__input 
    //-             input.input_number__in(type="text" v-model="number")
    //-         .input_number__suffix
    //-             button.suffix_btn(@click="inc") 
    //-                 img(src="../assets/images/suffix.svg")
    //- h4 Песочница
    //- div(style="display:flex; max-width: 100%;")
    //-     .checkbox 
    //-         .checkbox-box-wrapper 
    //-             .checkbox-box(@click="isHouse = !isHouse" :class="{ active : isHouse == true}")
    //-                 .checkbox-icon(v-if="isHouse")
    //-                     img(src="../assets/images/checkbox.svg")
    //-     span label 
    //- <!-- //- ПЕСОЧНИЦА 
    //- Развернутый header
    //- .header2(:class="{'active' : showHeader}")             
    //-     .container
    //-         .header2__container
    //-             .header2__icon_social
    //-                 img(src="../assets/images/facebook.svg")
    //-                 img(src="../assets/images/youtube.svg")
    //-                 img(src="../assets/images/vk.svg")
    //-             .header2__logo 
    //-                 img(src="../assets/images/logo2.svg")
    //-             .header2__icon_feed_back 
    //-                 img(src="../assets/images/telefon2.svg")
    //-                 button забронировать
    //-         .header2__container__nav 
    //-             ul.header2__nav
    //-                 li дома 
    //-                 li активный отдых
    //-                 li услуги
    //-                 li отзывы
    //-                 li контакты
    //-                 li расположение 
    //-                 li FAQ     
    //- Стрелки
    //- .d-flex.container_icon
    //-     img.first_page__arrow_icon(src="../assets/images/Arrow-left.svg")
    //-     img.first_page__arrow_icon(src="../assets/images/Arrow-right.svg") 
    //- Старые чекБоксы
    //- input.checkbox__input(type="checkbox" id="glamping")
    //- label.checkbox__name(for="glamping" style="margin-left:10px") глемпинг -->
    //- <!-- img(src="./") -->    
</template>

<script>
import houseList from "./houseList"
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
import { ref, computed } from "vue"
export default {
    name: 'sand-box',
    components: {
        Swiper,
        SwiperSlide,
    },
    setup() {
        let isHouse = ref(false)
        let number = ref(0)
        const inc = () => {
            number.value += 1
        }
        const dec = () => {
            number.value -= 1
        }
        let photoUser = ref(null)
        const handleFileUpload = (event) => {
            const file = event.target.files[0]   
            photoUser.value = file
        }
        const previewFilePath = computed(() => {            
            let URL = window.URL || window.webkitURL
            if(photoUser.value){
                return URL.createObjectURL(photoUser.value)
            }
            else{
                return '#'
            }
        })
        return {
            isHouse,
            number,
            inc,
            dec,
            houseList,
            handleFileUpload,
            previewFilePath,
            photoUser
        }
    }
}
</script>

<style scoped>
.input-file {
	position: relative;
	display: inline-block;
}
.input-file span {
	position: relative;
	display: inline-block;
	cursor: pointer;
	outline: none;
	text-decoration: none;	
	vertical-align: middle;	
	border-radius: 30px;
    background-image: url("../assets/images/user_photo-form.svg");
    background-repeat: no-repeat;
    background-position: center;   
	height: 46px;
	padding: 22px 23px;
	box-sizing: border-box;
	border: none;
	margin: 0;	
}
.input-file input[type=file] {
	position: absolute;
	z-index: -1;
	opacity: 0;
	display: block;
	width: 0;
	height: 0;
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

.input_number__in {
    border: none;
    width: 91px;
    text-align: center;
}

.suffix_btn,
.prefix_btn {
    background-color: inherit;
    border: none;
    padding: 0px 9px;
}

.input_number_wrapper {
    display: flex;
    align-items: center;
    width: 151px;
    height: 57px;
    border: 1px #B3B3B3 solid;
    border-radius: 10px;
}

.checkbox {
    width: 34px;
    height: 34px;
    display: inline-flex;
    flex-wrap: nowrap;
    cursor: pointer;
    align-items: flex-start;
    word-break: break-word;
}

.checkbox-box-wrapper {
    position: relative;
    width: 34px;
    height: 34px;
    flex-shrink: 0;
    flex-grow: 0;

}

.checkbox-box {
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    height: 34px;
    width: 34px;
    display: inline-block;
    box-sizing: border-box;
    border-radius: 8px;
    background-color: #ffffff;
    border: 1px solid #B3B3B3;
}

.checkbox-icon {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 34px;
    width: 34px;
}

.checkbox-box.active {
    border: 1px solid #005D4B;
}

input[type="checkbox"]:checked,
input[type="checkbox"]:not(:checked) {
    position: absolute;
    left: -9999px;
}

input[type="checkbox"]:checked+label,
input[type="checkbox"]:not(:checked)+label {
    display: inline-block;
    position: relative;
    padding-left: 40px;
    line-height: 28px;
    cursor: pointer;
}

input[type="checkbox"]:checked+label:before,
input[type="checkbox"]:not(:checked)+label:before {
    content: "";
    position: absolute;
    left: 0px;
    top: 0px;
    width: 34px;
    height: 34px;
    border-radius: 8px;
    border: 1px #B3B3B3 solid;
    background-color: #ffffff;
}

.checkbox__name {
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
}

.checkbox__header {
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
    margin-top: -12px;
    margin-bottom: 11px;
}

.checkbox__input+label {
    display: inline-flex;
    align-items: center;
}

.checkbox__input::before {
    content: '';
    display: inline-block;
    width: 1em;
    height: 1em;
    flex-shrink: 0;
    flex-grow: 0;
    border: 1px solid #adb5bd;
    border-radius: 0.25em;
    margin-right: 0.5em;
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 50% 50%;
}</style>