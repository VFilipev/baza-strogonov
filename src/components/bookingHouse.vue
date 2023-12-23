<template lang="pug">
div
    h4.about_us__header размещение
    .placement__form.row
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
                    button.prefix_btn(@click="decPersonQuantity")
                        img(v-if="filter.personQuantity == 0" alt="" src="../assets/images/prefix.svg")
                        img(v-else alt="" src="../assets/images/prefix-active.svg")
                .input_number__input 
                    input.input_number__in(type="text" :class="{active : filter.personQuantity > 0}" v-model="filter.personQuantity" name="person_quantity")
                .input_number__suffix
                    button.suffix_btn(@click="incPersonQuantity") 
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
        button.placement__form__button_search(@click="getAvailableHouse") найти
    .row.placement__cantainer_card
        template(v-if="houseList.length > 0")
            .col-4(v-for="(house, index) in houseList")
                .placement__card 
                    .wrapper_img(:style="{ backgroundImage: `url(${house.img})` }")
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
                        .footer_button(@click="toBooking(house)") забронировать 
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
        const getAvailableHouse = async () => {
            let start = moment(filter.value.dateStart).format('DD.MM.YYYY')
            let end = moment(filter.value.dateEnd).format('DD.MM.YYYY')
            let tmp = (await Lodge.get_available_house({ 'date_start': start, 'date_end': end })).data
            houseList.value = tmp
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
        onMounted(() => {
            getHouseList()
        })
        return {            
            formatNumber,
            filter,
            incPersonQuantity,
            decPersonQuantity,
            getAvailableHouse,
            toBooking,
            showModalHouse,
            houseList,
            masks,
            selectedColor      
        }
    }
}
</script>

<style scoped></style>