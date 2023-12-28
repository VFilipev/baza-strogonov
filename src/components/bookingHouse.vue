<template lang="pug">
div
    h4.header_section размещение
    .row.placement__form.d-flex.d-sm-none
        .date_time.date_time__icon.date_time__text.col-6(style="margin-bottom:13px")
            DatePicker(v-model="filter.dateStart" :masks="masks" :color="selectedColor")
                template(#default="{ inputValue, inputEvents }")                        
                    input.date_time__input(:value="inputValue" v-on="inputEvents" name="date_time_input-m" id="inputDateStart-m")
        .date_time.date_time__icon.date_time_end__text.col-6(style="margin-bottom:13px")
            DatePicker(v-model="filter.dateEnd" :masks="masks" :color="selectedColor")
                template(#default="{ inputValue, inputEvents }")                        
                    input.date_time__input(:value="inputValue" v-on="inputEvents" name="date_time_input-m") 

        .col-4
            .quantity_guests.quantity_guests__text(:class="{active : filter.personQuantity > 0}") 
                .input_number_wrapper(:class="{active : filter.personQuantity > 0}")
                    .input_number__prefix
                        button.prefix_btn(@click="dec")
                            img(v-if="filter.personQuantity == 0" alt="" src="../assets/images/prefix.svg")
                            img(v-else alt="" src="../assets/images/prefix-active.svg")
                    .input_number__input 
                        input.input_number__in(type="text" :class="{active : filter.personQuantity > 0}" v-model="filter.personQuantity" name="person_quantity-m")
                    .input_number__suffix
                        button.suffix_btn(@click="inc") 
                            img(v-if="filter.personQuantity == 0" src="../assets/images/suffix.svg")
                            img(v-else src="../assets/images/suffix-active.svg")
        .col-4.d-flex.align-items-center(style="padding-left:0")
            .checkbox_container
                div.checkbox__header показать свободные:
                .checkbox-wrapper
                    .checkbox
                        .checkbox-box-wrapper 
                            .checkbox-box(@click="filter.isHouse = !filter.isHouse" :class="{ active : filter.isHouse == true}")
                                .checkbox-icon(v-if="filter.isHouse")
                                    img(src="../assets/images/checkbox.svg")
                    span.checkbox__label(style="margin-right: 4px" :class="{ active: filter.isHouse == true}") дома                    
                    .checkbox 
                        .checkbox-box-wrapper 
                            .checkbox-box(@click="filter.isGlamping = !filter.isGlamping" :class="{ active : filter.isGlamping == true}")
                                .checkbox-icon(v-if="filter.isGlamping")
                                    img(src="../assets/images/checkbox.svg")
                    span.checkbox__label(:class="{ active: filter.isGlamping == true}") глэмпинг                    
        .col-4
            button.placement__form__button_search(@click="getAvailableLodge") найти 
    .placement__form.row.d-none.d-sm-flex
        .date_time.date_time__icon.date_time__text.col-3
            DatePicker(v-model="filter.dateStart" :masks="masks" :color="selectedColor")
                template(#default="{ inputValue, inputEvents }")                        
                    input.date_time__input(:value="inputValue" v-on="inputEvents" name="date_time_input" id="inputDateStart")
        .date_time.date_time__icon.date_time_end__text.col-3
            DatePicker(v-model="filter.dateEnd" :masks="masks" :color="selectedColor")
                template(#default="{ inputValue, inputEvents }")                        
                    input.date_time__input(:value="inputValue" v-on="inputEvents" name="date_time_input") 
            .date_picker_wrapper
        .quantity_guests.quantity_guests__text(:class="{active : filter.personQuantity > 0}") 
            .input_number_wrapper(:class="{active : filter.personQuantity > 0}")
                .input_number__prefix
                    button.prefix_btn(@click="dec")
                        img(v-if="filter.personQuantity == 0" alt="" src="../assets/images/prefix.svg")
                        img(v-else alt="" src="../assets/images/prefix-active.svg")
                .input_number__input 
                    input.input_number__in(type="text" :class="{active : filter.personQuantity > 0}" v-model="filter.personQuantity" name="person_quantity")
                .input_number__suffix
                    button.suffix_btn(@click="inc") 
                        img(v-if="filter.personQuantity == 0" src="../assets/images/suffix.svg")
                        img(v-else src="../assets/images/suffix-active.svg")
        .checkbox_container
            div.checkbox__header показать свободные:
            .checkbox-wrapper
                .checkbox
                    .checkbox-box-wrapper 
                        .checkbox-box(@click="filter.isHouse = !filter.isHouse" :class="{ active : filter.isHouse == true}")
                            .checkbox-icon(v-if="filter.isHouse")
                                img(src="../assets/images/checkbox.svg")
                span.checkbox__label(style="margin-right: 15px" :class="{ active: filter.isHouse == true}") дома                    
                .checkbox 
                    .checkbox-box-wrapper 
                        .checkbox-box(@click="filter.isGlamping = !filter.isGlamping" :class="{ active : filter.isGlamping == true}")
                            .checkbox-icon(v-if="filter.isGlamping")
                                img(src="../assets/images/checkbox.svg")
                span.checkbox__label(:class="{ active: filter.isGlamping == true}") глэмпинг                    
        button.placement__form__button_search(@click="getAvailableLodge") найти
    .row.placement__cantainer_card
        template(v-if="houseList.length > 0")
            .col-xs-12.col-sm-4(v-for="(house, index) in houseList")
                .placement__card 
                    .wrapper_img()
                        picture
                            source(type="image/webp" :srcset="house.img")
                            img(:src="house.img")
                        .btn_house_detail(@click="showModalHouse(house)")
                    .container_info-graph
                        .house_name {{ house.name }}
                        .wrapper_cost_capacity
                            .house_cost {{ '₽ ' + formatNumber(house.cost_per_unit) }}
                            .house_capacity
                                .house_capacity__icon 
                                    img(src="../assets/images/icon_emoji.svg")
                                .house_capacity__text до {{ house.maxP }} чел
                    .container_footer 
                        .footer_text {{ house.short_description }}
                        button.footer_button(:disabled="notFilter()" @click="toBooking(house)") забронировать 
        template(v-else)
            div Выберите дату
</template>

<script>
import { ref, onMounted } from "vue"
import { Lodge } from '../api'
import { Calendar, DatePicker } from 'v-calendar';
import 'v-calendar/style.css';
import { formatNumber } from "./formatNumber";
import { useRouter } from 'vue-router'
import { useOrderStore } from "../stores/orderStore";
import moment from "moment";

export default {
    name: "booking-house",    
    components: {
        Calendar,
        DatePicker,
    },
    setup(props, { emit }) {
        let filter = ref({
            dateStart: '',
            dateEnd: '',
            isHouse: false,
            isGlamping: false,
            personQuantity: 0
        })
        const incPersonQuantity = () => {
            filter.value.personQuantity += 1
        }
        const decPersonQuantity = () => {
            filter.value.personQuantity > 0 ? filter.value.personQuantity -= 1 : filter.value.personQuantity = 0
        }
        let houseList = ref([])
        const getHouseList = async() =>{
            houseList.value = (await Lodge.getList({avalible: true})).results
        }
        const getAvailableLodge = async () => {
            if(checkDate()){
                let start = moment(filter.value.dateStart).format('DD.MM.YYYY')
                let end = moment(filter.value.dateEnd).format('DD.MM.YYYY')
                let tmp = (await Lodge.get_available_house({ 'date_start': start, 'date_end': end })).data
                houseList.value = tmp
            }
        }              
        const showModalHouse = (lodge) => {
            emit('selLodge', lodge)
        }
        const orderStore = useOrderStore()
        const router = useRouter()
        const selectedColor = ref('green')
        const masks = ref({
            modelValue: 'DD.MM.YYYY',
            L: 'DD.MM.YYYY'
        })
        let toBooking = (lodge) => {            
            if (orderStore.orderlodge_set.length > 0){
                orderStore.orderlodge_set = []
            }
            let tmp = {
                lodge: lodge,
                start_date: filter.value.dateStart,
                end_date: filter.value.dateEnd,
            }
            orderStore.orderlodge_set.push(tmp)            
            router.push({
                name: 'booking',
            })
        }
        const notFilter = () => {
            if (!filter.value.dateStart || !filter.value.dateEnd) { return true }
            else { return false }
        }
        const checkDate = () => {
            let start = moment(filter.value.dateStart)
            let end = moment(filter.value.dateEnd)
            let diff = end.diff(start, 'day')
            if (diff <= 0) {
                filter.value.dateEnd = ''
                return false
            } else {
                return true
            }
        }
        onMounted(() => {
            getHouseList()
        })
        return {            
            formatNumber,
            filter,
            incPersonQuantity,
            decPersonQuantity,
            getAvailableLodge,
            toBooking,
            showModalHouse,
            houseList,
            masks,
            selectedColor,
            notFilter
        }
    }
}
</script>

<style scoped>
picture {
    width: 100%;
    height: 100%;
    display: flex;

}

picture img {
    object-fit: cover;
    height: auto;
    width: 100%;
}
.checkbox__label {
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
    padding-left: 6px;
}

.checkbox__label.active {
    color: #005D4B;
}

.checkbox-wrapper {
    display: flex;
    width: 100%;
    align-items: center;
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
.input_number__in {
    border: none;
    width: 91px;
    text-align: center;
    color: #B3B3B3;
}

.input_number__in.active {
    color: #003731;
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

.input_number_wrapper.active {
    border: 1px #003B30 solid;
}
.header_section {
    font-family: 'Apoc Normal';
    font-weight: 300;
    font-size: 47px;
    line-height: 49px;
    color: #003731;
    margin-bottom: 69px;
}
.placement__form__button_search {
    width: 180px;
    margin-left: 0px;
    color: #005D4B;
    font-size: 17px;
    font-family: Lato;
    font-weight: normal;
    border: 1px #005D4B solid;
    border-radius: 55px;
    background-color: #fff;
}
.container_footer {
    display: flex;
    width: 373px;
    margin-left: 14px;
    margin-top: 36px;
    align-items: flex-end;
    justify-content: space-between;
}

.footer_text {
    display: flex;
    color: #003731;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300;
    line-height: 20.33px;
    width: 215px;
    height: 60px;
}

button.footer_button {
    display: flex;
    color: #FCF2EA;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 400;
    line-height: 17.25px;
    background-color: #005D4B;
    border-radius: 26px;
    width: 143px;
    height: 35px;
    align-items: center;
    justify-content: center;
    border: 0;

    &:hover {
        cursor: pointer;
    }
}

button.footer_button:disabled {
    background-color: #333333;
    cursor: not-allowed;
    opacity: .8;
}

.container_info-graph {
    font-family: 'Lato';
    font-size: 17px;
    color: #003731;
    font-weight: 400;
    display: flex;
    align-items: center;
    width: 373px;
    margin-top: 14px;
    margin-left: 14px;
    justify-content: space-between;
}

.wrapper_cost_capacity {
    display: flex;
}

.house_cost {
    font-weight: 300;
    margin-right: 38px;
}

.house_capacity {
    font-weight: 300;
    display: flex;
    align-items: center;
}

.house_capacity__icon {
    display: flex;
    margin-right: 9px;
}

.wrapper_img {
    border-radius: 30px;
    width: 400px;
    height: 248px;
    /* background-repeat: no-repeat;
    background-size: cover;
    background-position: center; */
    position: relative;
}

.wrapper_img picture img {
    border-radius: 30px;
}

.placement__cantainer_card {
    margin-top: 48px;
}

.placement__card {
    height: 399px;
    width: 400px;
    background: #ECE8E3;
    border-radius: 30px;
    margin-bottom: 40px;
}

.checkbox__header {
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
    margin-top: -12px;
    margin-bottom: 11px;
}

.checkbox_container {
    width: 250px;
    margin-left: 40px;
}

.quantity_guests {
    position: relative;
    width: 151px;
}

.quantity_guests__text::before {
    font-family: 'Montserrat';
    font-size: 17px;
    content: 'кол-во гостей';
    color: #bdbdbd;
    position: absolute;
    display: flex;
    align-items: center;
    left: 1.225rem;
    background-color: #fff;
    z-index: 10;
    transform: translateY(-13px);
    padding-left: 5px;
    padding-right: 5px;
}

.quantity_guests__text.active::before {
    color: #003B30;
}

.quantity_guests__input {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    height: 57px;
    max-width: 151px;
}

input:focus-visible {
    outline: 2px #005D4B solid;
}

.date_time__input {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 289px;
    height: 57px;
    color: #003731;
}

.date_time {
    position: relative;
}

.date_time__icon::before {
    content: url(../assets/images/calendar.svg);
    color: #bdbdbd;
    position: absolute;
    display: flex;
    align-items: center;
    top: 0;
    bottom: 0;
    left: 260px;
}

.date_time__text::after {
    font-family: 'Montserrat';
    font-size: 17px;
    content: 'заезд';
    color: #bdbdbd;
    position: absolute;
    display: flex;
    align-items: center;
    left: 1.625rem;
    background-color: #fff;
    z-index: 10;
    transform: translateY(-69px);
    padding-left: 5px;
    padding-right: 5px;
}

.date_time_end__text::after {
    font-family: 'Montserrat';
    font-size: 17px;
    content: 'выезд';
    color: #bdbdbd;
    position: absolute;
    display: flex;
    align-items: center;
    left: 1.625rem;
    background-color: #fff;
    z-index: 10;
    transform: translateY(-69px);
    padding-left: 5px;
    padding-right: 5px;
}

li {
    list-style-type: none;
}

ul {
    margin-left: 0;
    padding-left: 0;
}

.about_us__wrapper_img {
    width: 400px;
    height: 272px;
    /* background-image: url(../assets/images/diana.jpeg);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 0px -135px; */
}

.about_us__wrapper_img picture img {
    border-radius: 30px;
    object-position: 0px -135px;
}
@media (max-width: 1440px) {
    .first_page__header {
        margin-bottom: 320px;
    }

    .first_page__h1 {
        font-size: 25px;
        margin-bottom: 32px;
    }

    .first_page__h2 {
        font-size: 15px;
    }

    img.logo {
        width: 80%;
        display: block;
        margin: 0 auto;
    }

    .header__nav__link {
        font-size: 15px;
    }

    button.header__nav__button a {
        font-size: 15px;
    }

    .about_us {
        padding-top: 34px;
        padding-bottom: 47px;
    }

    .about_us__header {
        font-weight: 400;
        font-size: 23px;
        line-height: 27px;
        margin-bottom: 21px;
    }

    .about_us__card__header {
        font-weight: 400;
        margin-bottom: 0;
        font-size: 10px;
    }

    .about_us__card__text {
        font-size: 8px;
    }

    .about_us__card__img {
        height: 12px;
        margin-bottom: -4px;
    }

    .about_us__wrapper_img {
        width: 100%;
        height: 126px;
        background-position: 0px -70px;
    }

    .container {
        padding-right: calc(var(--bs-gutter-x) * 0.5);
        padding-left: calc(var(--bs-gutter-x) * 0.5);
    }

    .placement {
        padding-top: 35px;
    }

    .date_time__input {
        width: 100%;
        height: 27px;
        font-size: 10px;
        font-family: Lato;
        font-weight: 300;
        padding-left: 17px;
    }

    .date_time__text::after {
        font-size: 10px;
        content: 'дата заезда';
        transform: translateY(-35px);
    }

    .date_time_end__text::after {
        font-size: 10px;
        content: 'дата выезда';
        transform: translateY(-35px);
    }

    .date_time__icon::before {
        left: 170px;
        content: url(/src/assets/images/i-m-calendar.svg);
    }

    .quantity_guests {
        width: 100%;
    }

    .quantity_guests__text::before {
        transform: translate(-5px, -9px);
        font-size: 10px;
    }

    .input_number_wrapper {
        width: 100%;
        height: 27px;
    }

    .input_number__in {
        width: 52px;
        height: 20px;
    }

    .checkbox_container {
        width: 100%;
        margin-left: 0;
    }

    .checkbox__header {
        font-size: 10px;
        margin-bottom: 0;
    }

    .checkbox {
        width: 16px;
        height: 16px;
    }

    .checkbox-box-wrapper {
        width: 16px;
        height: 16px;
    }

    .checkbox-box {
        width: 16px;
        height: 16px;
        border-radius: 4px;
    }

    .checkbox__label {
        font-size: 10px;
    }

    .placement__form__button_search {
        width: 100%;
        margin-left: 0;
    }

    .checkbox-icon {
        width: 16px;
        height: 16px;
    }

    .checkbox-icon img {
        width: 80%;
    }

    .placement__card {
        width: 100%;
    }

    .wrapper_img {
        width: 100%;
    }

    .card__input {
        width: 100%;
    }

    .card {
        border-radius: 15px;
        padding: 7px 7px;
        height: 200px;
    }

    .card__header {
        width: 100%;
        border-radius: 15px;
        margin: 0;
        height: 40px;
    }

    .card__input_user_name {
        width: 99%;
        color: black;
        font-size: 10px;
        font-family: Lato;
        font-weight: 400;
    }

    .card__user_photo-form {
        margin-left: 6px;
        height: 25px;
        width: 25px;
    }

    .input-file span {
        height: 25px;
        padding: 0px 13px;
        background-size: 52%;
        transform: translateY(-2px);
    }

    .card__user_name {
        display: flex;
        align-items: center;
    }

    .card__body.card_form {
        margin-right: 0;
        align-items: center;
    }

    .card__body {
        margin-left: 0;
    }

    .card_button {
        width: 130px;
        height: 25px;
        font-size: 14px;
    }

    .feedback_section .section_header {
        margin-top: 40px;
    }

    .section_header {
        margin-bottom: 0px;
    }

    .card__user_photo img {
        width: 25px;
    }

    .card__user_name {
        font-size: 10px;
    }

    .card__user_photo {
        margin-left: 6px;
    }

    .card__text {
        font-size: 10px;
    }

    .info_header {
        font-size: 23px;
    }

    .adress__header,
    .attention__header {
        font-size: 10px;
    }

    .adress__text,
    .attention__text {
        font-size: 10px;
    }

    .container_adress {
        margin-top: 27px;
    }

    .container_attention {
        margin-top: 5px;
    }

    .map_wrapper {
        height: 145px;
        position: relative;
        background-image: url(../assets/images/map.jpg);
        background-position: center;
        background-repeat: no-repeat;
        border-radius: 15px;
        padding: 0 12px;
    }

    button.info__button {
        border: 1px #fff solid;
        font-size: 10px;
        padding: 7px 0px;
        position: absolute;
        bottom: 13px;
        left: 15px;
        right: 15px;
        width: 152px;
    }

    button.info__button a {
        color: #fff;
    }

    .section_header {
        font-size: 23px;
        font-weight: 400;
    }

    .faq__questions {
        padding: 7px 0px;
        font-size: 10px;
    }

    .faq__reply {
        font-size: 10px;
        height: 94px;
    }

    .container_questions {
        margin-top: 0;
        margin-bottom: 79px;
    }

    .contact__container {
        font-size: 10px;
        margin-top: 0px;
    }

    .container__phone {
        flex-direction: column;
        justify-content: space-between;
        gap: 0;
        margin: 0;
    }

    .service_section {
        padding-top: 34px;
    }

    .service__header {
        font-size: 25px;
        line-height: 30px;
        margin-bottom: 14px;
    }

    .service__name_typ {
        font-size: 15px;
    }

    .contact__form {
        width: 100%;
        height: 100%;
        margin-top: 14px;
        padding: 7px 14px;
    }

    .form__input {
        width: 100%;
        height: 29px;
        margin-bottom: 8px;
        border-radius: 14px;
    }

    input.form__input::placeholder {
        padding-left: 8px;
        font-size: 10px;
        font-family: Lato;
        font-weight: 300;
    }

    button.contact__button {
        width: 88px;
        height: 28px;
    }

    .contact__form {
        border-radius: 15px;
    }

    .modal-mask.active {
        overflow-y: scroll;
    }
}
@media (max-width: 390px) {
    .date_time__icon::before {
        left: 160px;
    }

    .container_info-graph {
        width: 340px;
        font-size: 15px;
    }

    .container_footer {
        width: 342px;
    }

    .footer_text {
        width: 195px;
        font-size: 13px;
    }

    button.info__button {
        width: 143px;
    }

    .first_page__header {
        margin-bottom: 240px;
    }
}
</style>