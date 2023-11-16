<template lang="pug">
div        
    .container(style="margin-top:300px")
        star-rating(:star-size="13" :animate="true" :show-rating="false")
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
import StarRating from 'vue-star-rating'
import { ref } from "vue"
export default {
    name: 'sand-box',
    components: {
        StarRating
    },
    setup () {
        let isHouse = ref(false)
        let number = ref(0)
        const inc = () => {
            number.value += 1
        }
        const dec = () => {
            number.value -= 1
        }
        return {
            isHouse,
            number,
            inc,
            dec
        }
    }
}
</script>

<style scoped>

.input_number__in{
    border: none;
    width: 91px;
    text-align: center;
}
.suffix_btn, .prefix_btn{
    background-color: inherit;
    border: none;
    padding: 0px 9px;
}
.input_number_wrapper{
    display: flex;
    align-items: center;
    width: 151px;
    height: 57px;
    border: 1px #B3B3B3 solid;
    border-radius: 10px;
}
.checkbox{
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
    height:34px;
    flex-shrink: 0;
    flex-grow: 0;
    
}
.checkbox-box{
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    height:34px;
    width: 34px;
    display: inline-block;
    box-sizing: border-box;
    border-radius:8px;
    background-color: #ffffff;
    border: 1px solid #B3B3B3;
}
.checkbox-icon{
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 34px;
    width: 34px;
}
.checkbox-box.active{    
    border: 1px solid #005D4B;    
}
input[type="checkbox"]:checked, 
input[type="checkbox"]:not(:checked){
    position: absolute;
    left: -9999px;
}
input[type="checkbox"]:checked + label, 
input[type="checkbox"]:not(:checked) + label{
    display: inline-block;
    position: relative;
    padding-left: 40px;
    line-height: 28px;
    cursor: pointer;
}
input[type="checkbox"]:checked + label:before, 
input[type="checkbox"]:not(:checked) + label:before{
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
.checkbox__name{
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
}
.checkbox__header{
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
    margin-top: -12px;
    margin-bottom: 11px;
}
.checkbox__input + label{
    display: inline-flex;
    align-items: center; 
}

.checkbox__input::before{
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
}
</style>