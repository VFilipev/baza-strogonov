<template lang="pug"> 
div.container  
  .row.header_booking
    h1.name-section.col-6.col-sm-12 бронирование
    .col-4.d-flex.d-sm-none.logo
      router-link(to="/")
        img(src="../assets/images/logo2.svg")
  section.info 
    .row 
      .col-12.col-sm-6.info-form.mb-4.mb-sm-0
        div.name_subsection Введите данные:
        input.text-field__input(placeholder="ФИО" type="text" :value="orderStore.customer" @input="inputCustomer($event)")
        input.text-field__input(placeholder="Телефон" type="tel" v-model="orderStore.phone")
        input.text-field__input(placeholder="Email" type="email" v-model="orderStore.email")
        div.data-time-container(v-if="orderStore.orderlodge_set.length > 0")
          .col-6.date_time.date_time__icon.date_time__text                       
            DatePicker(v-model="orderStore.orderlodge_set[0].start_date" :masks="masks" :color="selectedColor")
              template(#default="{ inputValue, inputEvents }")
                input.date_time__input(:value="inputValue ? inputValue : order.orderlodge_set[0].start_date" v-on="inputEvents")
          .col-6.date_time.date_time__icon.date_time_end__text(v-if="orderStore.orderlodge_set.length > 0")
            DatePicker(v-model="orderStore.orderlodge_set[0].end_date" :masks="masks" :color="selectedColor")
              template(#default="{ inputValue, inputEvents }")
                input.date_time__input(:value="inputValue ? inputValue : order.orderlodge_set[0].end_date" v-on="inputEvents")
      .col-12.col-sm-6(v-if="orderStore.orderlodge_set.length > 0")
        .info-card-lodge 
          .lodge__img(:style="{'background-image': 'url(' + orderStore.orderlodge_set[0].lodge.img + ')'}")
          div
            .card_lodge__footer 
              .lodge__name 
                p {{ orderStore.orderlodge_set[0].lodge.name }}
              .footer__icon 
                button.footer__btn выбрано                
                .icon__check   
  section.uslugi(style="margin-top: 20px") 
    .row 
      .name_subsection Добавить услуги:
    .row 

      .slider_wrapper 
        swiper(:slidesPerView="uslugiPreView" :spaceBetween="40" ref="swiper")  
          //- ЧАН          
          swiper-slide

            .uslugi_card 
              .uslugi_card__img(:style="{ backgroundImage: `url(${servicesList[0].photo})` }")
              .uslugi_card__footer 
                .uslugi_card__text {{ servicesList[0].name }}
                .footer_right 
                  .uslugi_card__text {{ servicesList[0].cost }}
                  .uslugi_card__btn-popup(v-if="!checkServiceInOrder('CH')" @click="showPopUp(servicesList[0].name)" :class="{active:isShowPopUp(servicesList[0].name)}")                     
                  .uslugi_card__check(v-else) 
            Transition(name="popUp")
              .service_popup(v-if="isShowPopUp(servicesList[0].name)")
                .row_service_popup.d-flex.justify-content-between.align-items-center
                  .service_popup__item Часы
                  .uslugi__hours_wrapper
                    img(src="../assets/images-booking/icon-remove.svg" @click="preOrder['CH'].prefferedTime--")
                    input.row_service_popup__input_hours(v-model="preOrder['CH'].prefferedTime")                        
                    img(src="../assets/images-booking/icon-add-2.svg" @click="preOrder['CH'].prefferedTime++")
                .row_service_popup.d-flex.justify-content-between.align-items-center                    
                  .service_popup__item Дата                  
                  .service_popup__date_time.service_popup__date_time__icon                        
                    input.service_popup__date_time__input(@click="showPopUpCalendar('чан')" v-model="preOrder['CH'].dateStart")
                    .date_picker_wrapper
                      DatePicker(v-if="services.datePicker.includes('чан')" :masks="masks" :color="selectedColor" v-model.string="preOrder['CH'].dateStart")
                .row_service_popup.d-flex.justify-content-between.align-items-center()                    
                  .service_popup__item Время
                  .service_popup__wrapper_time                          
                    img(v-if="preOrder['CH'].availableTime.length > 0" src="../assets/images-booking/arrow-left-time.svg" @click="decAvailableTimeIndex('CH')")
                    .available_time(v-if="preOrder['CH'].availableTime.length > 0") {{ stringToHour(preOrder['CH'].availableTime[preOrder['CH'].timeIndex]) }}
                    img.popup_arrow(v-if="preOrder['CH'].availableTime.length > 0" src="../assets/images-booking/arrow-right-time.svg" @click="incAvailableTimeIndex('CH')")
                .service_popup_footer
                  .uslugi_card__add(@click="addService('CH')")
          //- БАНЯ
          swiper-slide

            .uslugi_card 
              .uslugi_card__img(:style="{ backgroundImage: `url(${servicesList[1].photo})` }")
              .uslugi_card__footer 
                .uslugi_card__text {{ servicesList[1].name }}
                .footer_right 
                  .uslugi_card__text {{ servicesList[1].cost }}
                  .uslugi_card__btn-popup(v-if="!checkServiceInOrder('SN')" @click="showPopUp(servicesList[1].name)" :class="{active:isShowPopUp(servicesList[1].name)}") 
                  .uslugi_card__check(v-else)                     
            Transition(name="popUp")
              .service_popup(v-if="isShowPopUp(servicesList[1].name)")
                .row_service_popup.d-flex.justify-content-between.align-items-center
                  .service_popup__item Часы
                  .uslugi__hours_wrapper
                    img(src="../assets/images-booking/icon-remove.svg" @click="preOrder['SN'].prefferedTime--")
                    input.row_service_popup__input_hours(v-model="preOrder['SN'].prefferedTime")                        
                    img(src="../assets/images-booking/icon-add-2.svg" @click="preOrder['SN'].prefferedTime++")
                .row_service_popup.d-flex.justify-content-between.align-items-center                    
                  .service_popup__item Дата
                  .service_popup__date_time.service_popup__date_time__icon               
                    input.service_popup__date_time__input(@focus="showPopUpCalendar('баня')" v-model="preOrder['SN'].dateStart")
                    .date_picker_wrapper
                      DatePicker(v-if="services.datePicker.includes('баня')" :masks="masks" :color="selectedColor" v-model.string="preOrder['SN'].dateStart")
                .row_service_popup.d-flex.justify-content-between.align-items-center
                  .service_popup__item Время
                  .service_popup__wrapper_time                          
                    img(v-if="preOrder['SN'].availableTime.length > 0" src="../assets/images-booking/arrow-left-time.svg" @click="decAvailableTimeIndex('SN')")
                    .available_time(v-if="preOrder['SN'].availableTime.length > 0") {{ stringToHour(preOrder['SN'].availableTime[preOrder['SN'].timeIndex]) }}
                    img.popup_arrow(v-if="preOrder['SN'].availableTime.length > 0" src="../assets/images-booking/arrow-right-time.svg" @click="incAvailableTimeIndex('SN')")                    
                .service_popup_footer
                  .uslugi_card__add(@click="addService('SN')")                      
          swiper-slide(v-for="product in productsList")
            
            .uslugi_card(style="z-index:1")
              .uslugi_card__img(:style="{ backgroundImage: `url(${product.photo})` }")
              .uslugi_card__footer 
                .uslugi_card__text {{ product.name }}
                .footer_right 
                  .uslugi_card__text {{ product.cost + 'р/1ч'}}
                  .uslugi_card__add(v-if="!isAdd(product.id)" @click="addProduct(product)")
                  .uslugi_card__check(v-else @click="removeProduct(product)")
          controlSwiper
  section.order(style="margin-top: 10px")
    .row 
      .name_subsection Добавлено:
    .row
      .order_item.col-12
        .order_item__name.col-4 {{ orderStore.orderlodge_set[0].lodge.name }}
        .order_item__info.col-8.col-sm-6.offset-sm-2.justify-content-sm-between
          .order_item__cost {{ formatNumber(calcCost) + ' р.' }}
          .order_item__date {{ parserDate(orderStore.orderlodge_set[0].start_date) + ' - ' + parserDate(orderStore.orderlodge_set[0].end_date)}}
    template(v-if="orderStore.products_set.length > 0")
      .row 
        .order_item.col-12(v-for="product in orderStore.products_set") 
          .order_item__name.col-4 {{ product.name }}
          .order_item__info.col-8.col-sm-6.offset-sm-2
            .order_item__cost {{ formatNumber(product.cost) + ' р.' }}
            .order_item__date
    template(v-if="orderStore.services_set.length > 0")
      .row
        .order_item.col-12(v-for="service in orderStore.services_set") 
          .order_item__name.col-6 {{ preOrder[service.name].name }}
          .d-flex.justify-content-between.col-6
            .order_item__cost {{ formatNumber(service.cost) + ' р.'}}
            .order_item__duration {{ getDuration(service) }}
            .order_item__date {{ parserDate(service.start_date) }}    
  section.confirm(style="margin-top:25px; margin-bottom: 80px" )
    div.d-flex.justify-content-between  
      .confirm__checkbox-wrapper
        .confirm__checkbox
          .confirm__checkbox-box-wrapper 
            .confirm__checkbox-box(@click="isConfirm = !isConfirm" :class="{icon_check : isConfirm}")              
        span.confirm__checkbox__label Я согласен с условиями <a style="color:#005D4B" href="./src/assets/politica.pdf" target="_blank"> политики конфиденциальности</a> и даю разрешение на обработку персональных данных    
      button.confirm__btn(:disabled="!isConfirm" @click="toBooking") забронировать  
  transition(name="modal")
    .modal-mask(v-if="isShowModalPopUp" aria-hidden="true")
        .modal-wrapper(ref="modal" @click="isShowModalPopUp = false"  role="dialog" aria-hidden="true")
            .modal-container-datepicker(@click.stop="" role="document")
              .modal-header
                button.btn_close(@click="isShowModalPopUp = false")
              .modal-body2-datepicker             
                DatePicker(:masks="masks" :color="selectedColor" v-model.string="preOrder['SN'].dateStart")


</template>

<script>
import { Calendar, DatePicker } from 'v-calendar';
import { ref, computed, watch, onMounted } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue';
import moment from 'moment';
import 'swiper/css';

import controlSwiper from '../components/controlSwiper.vue';
import { useOrderStore } from '../stores/orderStore'

import { useRouter } from 'vue-router'
import { formatNumber } from '../components/formatNumber'
import { Service, SpecialPrice } from '../api'

export default {
  name: 'booking',
  components: {
    Calendar,
    DatePicker,
    Swiper,
    SwiperSlide,
    controlSwiper
  },
  setup() {
    const inputCustomer = (event) => {
      orderStore.changeCustomer(event.target.value)
    }
    const orderStore = useOrderStore()
    const popover = ref({
      visibility: 'click',

    })
    const calcCost = computed(() => {
      let dateStart = moment(orderStore.orderlodge_set[0].start_date).format('YYYY-MM-DD')
      let dateEnd = moment(orderStore.orderlodge_set[0].end_date).format('YYYY-MM-DD')
      let dateListOrder = getDateList(dateStart, dateEnd)
      let totalPrice = 0
      let specPrice = []
        for (let dayOrder of dateListOrder) {
          for (let day of dateListSpecialPrice.value) {
            if (day.day.includes(dayOrder)) {
              totalPrice += day.cost
              specPrice.push(dayOrder)
            }
          }
          if (!specPrice.includes(dayOrder)){
            let indexOfWeek = moment(dayOrder, 'DD-MM-YYYY').isoWeekday()       
            totalPrice += orderStore.orderlodge_set[0].lodge.price_set_by_day[indexOfWeek]
          }
      }
      return totalPrice
    })
    const totalCost = computed(() => {
      let serviceCost = orderStore.services_set.reduce((s, c) => s + c.cost, 0);
      let productCost = orderStore.products_set.reduce((s, c) => s + c.cost, 0);
      let total = calcCost.value + serviceCost + productCost
      return total
    })
    const parserDate = (date) => {
      return moment(date).format('DD/MM/YY')
    }
    let order = ref({
      customer: 'Филипьев Василий Александрович',
      phone: '89819710592',
      email: 'mail@mail.ru',
      orderlodge_set: [
        {
          lodge: {
            "id": 1,
            "name": "Дом Кузнеца",
            "num": "1",
            "sub_name": "",
            "description": "двухэтажный деревянный дом, где могут разместиться до 11 человек. 4 просторные комнаты, в которых будет удобно и парам, и семьям с детьми.",
            "short_description": "2 смежные и 2 изолированные спальни, просторная кухня-гостиная, санузел",
            "conveniences": "кухня - полный комплект посуды на 11 человек, холодильник, обеденный стол, электроплита с духовым шкафом, микроволновая печь, электро чайник, санузел - горячая и холодная вода, музыкальный центр, 3 телевизора",
            "include": "пользование спортивными, детскими площадками, мангалом и решеткой, охраняемая парковка, охраняемый причал",
            "maxP": 11,
            "img": "http://127.0.0.1:8000/media/img/house-6.png",
            "img_small": null,
            "plan1": null,
            "plan2": null,
            "uslugi": "1",
            "slug": "",
            "avalible": true,
            "lodge_main": null
          },
          cost: 15000,
          start_date: '22.11.2023',
          end_date: '25.11.2023',
          mainPhoto: 'src/assets/images-booking/lodge.png',
        }
      ],
      // {
      //   name: 'Дом Кузнеца',
      //   mainPhoto: 'src/assets/images-booking/lodge.png',
      //   cost: 15000
      // },
      services_set: [],
      products_set: []
    })
    const selectedColor = ref('green')
    const masks = ref({
      modelValue: 'DD.MM.YYYY',
      L: 'DD.MM.YYYY'
    })
    let servicesList = ref([
      {
        photo: 'static/uslugi/images-2.webp',
        name: 'чан',
        cost: '3000р/2ч',
      },
      {
        photo: 'static/uslugi/images-3.webp',
        name: 'баня',
        cost: '2400р/2ч',
      },
    ])
    let productsList = ref([
      {
        id: 1,
        photo: 'static/uslugi/images-1.webp',
        name: 'Снегоход',
        cost: 3200,
      },
      {
        id: 2,
        photo: 'static/uslugi/images-11.webp',
        name: 'Зоопарк',
        cost: 150,
      },
      {
        id: 3,
        photo: 'static/uslugi/images-10.webp',
        name: 'Сапы',
        cost: 1000,
      },
      {
        id: 4,
        photo: 'static/uslugi/images-6.webp',
        name: 'Каток',
        cost: 150,
      },
      {
        id: 5,
        photo: 'static/uslugi/images-4.webp',
        name: 'Лыжи',
        cost: 150,
      },
    ])
    const addProduct = (product) => {
      orderStore.products_set.push(product)
    }
    const removeProduct = (product) => {
      let findIndex = orderStore.products_set.findIndex(x => x.id == product.id)
      orderStore.products_set.splice(findIndex, 1)
    }
    const isAdd = (id) => {
      if (orderStore.products_set.length > 0) {
        let item = orderStore.products_set.find(x => x.id == id)
        if (item) {
          return true
        }
      }
      else {
        return false
      }
    }
    let isConfirm = ref(false)
    const router = useRouter()
    const dateFormat = (date) => {
      tmp = moment(date, 'DD.MM.YYYY').format('YYYY-MM-DD')
      return tmp
    }
    let toBooking = () => {
      // order.value.orderlodge_set[0].start_date = order.value.orderlodge_set[0].start_date
      // let ens 
      // await Order.save(order.value)
      orderStore.cost = totalCost.value
      router.push({
        name: 'BookingConfirm',
      })
    }
    let popUpList = ref([])
    const clearDatePickerList = () => {
      let findIndex = services.value.datePicker.findIndex(x => x == 'баня')
      services.value.datePicker.splice(findIndex, 1)
      findIndex = services.value.datePicker.findIndex(x => x == 'чан')
      services.value.datePicker.splice(findIndex, 1)
    }
    const showPopUp = async(name) => {
      if (popUpList.value.includes(name)) {
        await Promise.all([
          clearDatePickerList()
        ])
        closePopUp(name)
      }
      else {
        popUpList.value.push(name)
      }
    }
    const isShowPopUp = (name) => {
      if (popUpList.value.includes(name)) {
        return true
      }
      else { return false }
    }
    const closePopUp = (name) => {
      let findIndex = popUpList.value.findIndex(x => x == name)
      popUpList.value.splice(findIndex, 1)
    }
    const incAvailableTimeIndex = (name) => {
      if (preOrder.value[name].timeIndex < preOrder.value[name].availableTime.length - 1) {
        preOrder.value[name].timeIndex++
      }
      else {
        preOrder.value[name].timeIndex = 0
      }
    }
    const decAvailableTimeIndex = (name) => {
      if (preOrder.value[name].timeIndex > 0) {
        preOrder.value[name].timeIndex--
      }
    }
    let services = ref({
      datePicker: []
    })
    let serviceReserv = ref({
      'CH': [],
      'SN': []
    })
    let unavailableHours = ref({
      'CH': [],
      'SN': []
    })

    let preOrder = ref({
      'CH': {
        'prefferedTime': 2,
        'timeIndex': 0,
        'dateStart': '',
        'availableTime': [],
        'name': 'Чан',
        'cost_per_unit': 1500
      },
      'SN': {
        'prefferedTime': 2,
        'timeIndex': 0,
        'dateStart': '',
        'availableTime': [],
        'name': 'Баня',
        'cost_per_unit': 1200
      }
    })

    const getAvailableHours = (name) => {
      let allHours = [];
      for (let i = 0; i < 24; i++) {
        allHours.push(i);
      }

      for (let i = 0; i < unavailableHours.value[name].length; i++) {
        let bookedHour = unavailableHours.value[name][i];
        let index = allHours.indexOf(bookedHour);

        if (index !== -1) {
          allHours.splice(index, 1);
        }
      }
      preOrder.value[name].availableTime = allHours
    }
    const stringToHour = (str) => {
      return moment(str, 'HH').format('HH:mm')
    }
    const getUnavailableHours = (name) => {
      unavailableHours.value[name] = []
      for (let s of serviceReserv.value[name]) {

        let start = moment.utc(s.start_date).utcOffset('UTC');
        let end = moment.utc(s.end_date).utcOffset('UTC');

        let startHour = start.hour() - preOrder.value[name].prefferedTime
        let endHour = end.hour() + 1

        for (let hour = startHour; hour < endHour; hour++) {
          if (!unavailableHours.value[name].includes(hour)) {
            unavailableHours.value[name].push(hour);
          }
        }
      }      
      getAvailableHours(name)
    }
    const getDateList = (start, end) => {
      let dateList = []
      let current = moment(start, 'YYYY-MM-DD');
      let endDate = moment(end, 'YYYY-MM-DD')
      while (current.isBefore(endDate)) {
        dateList.push(current.format('DD-MM-YYYY'));
        current.add(1, 'days');
      }
      // console.log(dateList);
      return dateList
    }
    let dateListSpecialPrice = ref([])
    const getSpecialPrice = async () => {
      let res = (await SpecialPrice.getList({ 'lodge': orderStore.orderlodge_set[0].lodge.id, 'active': true })).results
      let index = 0
      for (let spec of res) {
        let tmp = { 'name': spec.name, 'cost': spec.cost, 'day': [] }
        dateListSpecialPrice.value.push(tmp)
        let list = getDateList(spec.date, spec.date_end)
        for (let day of list) {
          dateListSpecialPrice.value[index].day.push(day)
        }
        index++
      }      

    }
    const getService = async (filter) => {
      serviceReserv.value[filter.name] = (await Service.getList(filter)).results
      getUnavailableHours(filter.name)
    }
    const checkServiceInOrder = (name) => {
      let tmp = orderStore.services_set.find(s => s.name == name)
      if (tmp) {
        return true
      }
      else { return false }
    }
    const addService = (name) => {
      let tmp = {}
      tmp.name = name
      let date = moment(preOrder.value[name].dateStart, 'DD.MM.YYYY').format('YYYY-MM-DD')
      tmp.start_date = date + 'T' + stringToHour(preOrder.value[name].availableTime[preOrder.value[name].timeIndex])
      tmp.end_date = date + 'T' + stringToHour(preOrder.value[name].availableTime[preOrder.value[name].timeIndex + preOrder.value[name].prefferedTime])
      tmp.cost = preOrder.value[name].prefferedTime * preOrder.value[name].cost_per_unit
      orderStore.services_set.push(tmp)
      closePopUp(name)
    }
    const getDuration = (service) => {
      let start = moment(service.start_date, 'YYYY-MM-DDTHH:mm').format('HH:mm')
      let end = moment(service.end_date, 'YYYY-MM-DDTHH:mm').format('HH:mm')
      let str = start + '-' + end
      return str
    }
    let isShowModalPopUp = ref(false)   
    let device = ref('')
    const showPopUpCalendar = (name) => {
      if (device.value == 'mobile'){
        isShowModalPopUp.value = true
      }
      else{
        services.value.datePicker.push(name)        
      }
    }
    let uslugiPreView = ref(6)
    let uslugiSpace = ref(40)
    onMounted(() => {
      if (window.innerWidth < 600 || /Mobi/i.test(navigator.userAgent)) {
        uslugiSpace.value = 40
        uslugiPreView.value = 3
        device.value = 'mobile'
      }
      getSpecialPrice()
    })
    watch(() => preOrder.value['CH'].dateStart, () => {
      let findIndex = services.value.datePicker.findIndex(x => x == 'чан')
      services.value.datePicker.splice(findIndex, 1)
      let dateStart = moment(preOrder.value['CH'].dateStart).format('YYYY-MM-DD')
      getService({ 'name': 'CH', 'start_date': dateStart })
    })
    watch(() => preOrder.value['SN'].dateStart, () => {
      let findIndex = services.value.datePicker.findIndex(x => x == 'баня')
      services.value.datePicker.splice(findIndex, 1)
      let dateStart = moment(preOrder.value['SN'].dateStart).format('YYYY-MM-DD')
      getService({ 'name': 'SN', 'start_date': dateStart })
    })
    watch(() => preOrder.value['CH'].prefferedTime, () => {
      if (servicesList.value[1].dateStart) {
        getService({ 'name': 'CH' })
      }
    })
    watch(() => preOrder.value['SN'].prefferedTime, () => {
      if (servicesList.value[1].dateStart) {
        getService({ 'name': 'SN' })
      }
    })
    return {
      order,
      selectedColor,
      masks,
      servicesList,
      addService,
      addProduct,
      removeProduct,
      calcCost,
      totalCost,
      parserDate,
      productsList,
      isAdd,
      isConfirm,
      toBooking,
      showPopUp,
      isShowPopUp,
      closePopUp,
      incAvailableTimeIndex,
      services,
      stringToHour,
      decAvailableTimeIndex,
      preOrder,
      getDuration,
      checkServiceInOrder,
      popover,
      orderStore,
      inputCustomer,
      showPopUpCalendar,
      uslugiPreView,
      isShowModalPopUp,
      formatNumber     
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

input:focus-visible {
  outline: 2px #005D4B solid;
}
.modal-header{
  margin-right: 15px;
  justify-content: flex-end;
}
button.btn_close {
    background-image: url('src/assets/images/btn-close-active.svg');
    background-repeat: no-repeat;
    background-position: center;
    height: 40px;
    width: 40px;
    border: 0;
    background-color: transparent;
    &:hover {
        cursor: pointer;        
    }
}
.modal-body2-datepicker
{
    height: calc(95vh );
    min-height: 600px;
    overflow-y: auto;
    overflow-x:hidden;
    padding:0px;
    align-items: center;
    display: flex;
    justify-content: center;
}
.modal-container-datepicker{

    max-width:1000px;
    margin:15px auto;
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
.date_picker_wrapper {
  top: 30px;
  position: absolute;
}

.vc-popover-content-wrapper.is-interactive {
  z-index: 100;
}

.popup_arrow:hover {
  cursor: pointer;
}

.service_popup__wrapper_time {
  color: #005D4B;
  font-size: 12px;
  font-family: 'Lato';
  font-weight: 400;
  width: 97px;
  border-radius: 7px;
  border: 1px #005D4B solid;
  height: 26px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0px 7px;
}

.service_popup__date_time__input {
  border-radius: 7px;
  border: 1px #005D4B solid;
  background-color: transparent;
  width: 97px;
  height: 26px;
  color: #005D4B;
  font-size: 14px;
}

.service_popup__date_time {
  position: relative;
}

.service_popup__date_time__icon::before {
  content: url(../assets/images-booking/calendar.svg);
  color: #bdbdbd;
  position: absolute;
  display: flex;
  align-items: center;
  top: 0;
  bottom: 0;
  left: 77px;
}

.row_service_popup {
  padding-left: 13px;
  padding-right: 8px;
  margin-top: 12px;
}

.service_popup_footer {
  padding-left: 13px;
  padding-right: 8px;
  margin-top: 6px;
  display: flex;
  justify-content: end;
}

.row_service_popup img {
  cursor: pointer;
}

.service_popup__item {
  color: #005D4B;
  font-size: 12px;
  font-family: 'Lato';
  font-weight: 400;
}

.row_service_popup__input_hours {
  width: 35px;
  text-align: center;
  background-color: transparent;
  border-radius: 7px;
  color: #005D4B;
  border: 1px #005D4B solid;
}

.popUp-enter-active {
  animation: animatePopUp 1s;
}

.popUp-leave-active {
  animation: animatePopUp 1s reverse;
}

@keyframes animatePopUp {
  from {
    top: 0%;
  }

  to {
    top: 100%;
  }
}

.swiper {
  overflow-x: clip;
  overflow-y: visible;
}

.service_popup {
  position: absolute;
  width: 180px;
  background-color: #ECE8E3;
  border-radius: 30px;
  height: 160px;
  z-index: 9;
}

.confirm__checkbox__label {
  font-family: 'Lato';
  font-weight: 400;
  font-size: 20px;
  color: black;
  padding-left: 6px;
}

.confirm__checkbox__label.active {
  color: #005D4B;
}

.confirm__checkbox-wrapper {
  display: flex;
  width: 100%;
  align-items: center;
}

.confirm__checkbox {
  width: 22px;
  height: 22px;
  display: inline-flex;
  flex-wrap: nowrap;
  cursor: pointer;
  align-items: flex-start;
  word-break: break-word;
}

.confirm__checkbox-box-wrapper {
  position: relative;
  width: 22px;
  height: 22px;
  flex-shrink: 0;
  flex-grow: 0;

}

.confirm__checkbox-box {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  height: 22px;
  width: 22px;
  display: inline-block;
  box-sizing: border-box;
  border-radius: 8px;
  background-color: #fff;
  border: 1px solid #B3B3B3;

  &.icon_check {
    background-color: #005D4B;
    background-image: url('src/assets/images-booking/icon-check-2.svg');
    background-repeat: no-repeat;
    background-position: center;
  }
}

.confirm__checkbox-icon {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 22px;
  width: 22px;
}

.confirm__checkbox-box.active {
  border: 1px solid #005D4B;
}

.confirm__btn {
  width: 144px;
  height: 36px;
  border: 0;
  background-color: #005D4B;
  border-radius: 36px;
  color: #FCF2EA;
  font-size: 15px;
  font-family: 'Lato';
  font-weight: 400;

  &:disabled {
    background-color: #333333;
    cursor: not-allowed;
    opacity: .8;
  }
}

.order_item__info {
  display: flex;
  

}

.order_item {
  display: flex;
  justify-content: space-between;
  color: #333333;
  font-size: 20px;
  font-family: 'Lato';
  font-weight: 400;
  border-bottom: 1px black solid;
  padding-bottom: 25px;
}

.order_item:not(:first-child) {
  margin-top: 24px;
}

.uslugi_card__footer {
  display: flex;
  justify-content: space-between;
  padding-left: 22px;
  padding-right: 10px;
}

.footer_right {
  display: flex;
  gap: 4px;
  align-items: center;
}

.uslugi_card__add {
  width: 30px;
  height: 30px;
  border-radius: 30px;
  background-color: #005D4B;
  background-image: url('src/assets/images-booking/icon-add.svg');
  background-repeat: no-repeat;
  background-position: center;
  cursor: pointer;
}

.uslugi_card__btn-popup {
  width: 30px;
  height: 30px;
  border-radius: 30px;
  background-color: #005D4B;
  background-image: url('src/assets/images-booking/btn-open-popup.svg');
  background-repeat: no-repeat;
  background-position: center;
  transition: transform .5s ease-in-out;

  &:hover {
    cursor: pointer;
  }
}

.uslugi_card__btn-popup.active {
  transform: rotate(180deg);
}

.uslugi_card__check {
  width: 30px;
  height: 30px;
  border-radius: 30px;
  background-color: #005D4B;
  background-image: url('src/assets/images-booking/icon-check-service.svg');
  background-repeat: no-repeat;
  background-position: center;
  cursor: pointer;
}

.uslugi_card__text {
  display: flex;
  justify-content: center;
  color: #003731;
  font-size: 11px;
  font-family: 'Lato';
  font-weight: 400;
  padding-top: 15px;
  padding-bottom: 15px;
}

.uslugi_card__img {
  border-radius: 30px;
  width: 180px;
  height: 196px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.uslugi_card {
  position: relative;
  width: 180px;
  background-color: #ECE8E3;
  border-radius: 30px;
  z-index: 10;
}

.swiper-slide.swiper-slide-next {
  z-index: 10;
}

.info-card-lodge {
  height: 335px;
  background-color: #ECE8E3;
  border-radius: 30px;
}

.lodge__img {
  height: 264px;
  display: block;
  border-radius: 30px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.card_lodge__footer {
  display: flex;
  justify-content: space-between;
  margin-top: 25px;
}

.icon__check {
  width: 36px;
  height: 36px;
  border-radius: 30px;
  background-color: #005D4B;
  background-image: url('src/assets/images-booking/icon-check.svg');
  background-repeat: no-repeat;
  background-position: center;
}

.footer__icon {
  display: flex;
  gap: 2px;
  padding-right: 10px;
}

.lodge__name {
  padding-left: 27px;
  color: #005D4B;
  font-size: 15px;
  font-family: 'Lato';
  font-weight: 400;
  text-transform: uppercase;
}

button.footer__btn {
  color: #FCF2EA;
  font-size: 15px;
  font-family: Lato;
  font-weight: 400;
  background-color: #005D4B;
  border-radius: 36px;
  border: 0;
  width: 104px;
  height: 36px;
}

.name-section {
  font-family: 'Apoc Normal';
  font-size: 47px;
  font-weight: 300;
  color: rgba(0, 93, 75, 1);
}

.name_subsection {
  font-family: 'Lato';
  font-size: 20px;
  margin-bottom: 21px;
}

.text-field__input {
  border-radius: 9px;
  border: 1px #A4A4A4 solid;
  width: 97.3%;
  height: 57px;
  padding-left: 10px;
  font-size: 24px;
  font-family: 'Montserrat', sans-serif;
  margin-bottom: 20px;
}

.data-time-container {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.date-time-in {
  width: 275px;
}

.date-time-out {
  width: 275px;
}

.header_booking {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 97px;
  margin-bottom: 47px;
}

.date_time__input {
  border-radius: 10px;
  border: 1px #005D4B solid;
  width: 289px;
  height: 57px;
  color: #003731;
  padding-left: 12px;
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
  color: #005D4B;
  position: absolute;
  display: flex;
  align-items: center;
  left: 8px;
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
  color: #005D4B;
  position: absolute;
  display: flex;
  align-items: center;
  left: 8px;
  background-color: #fff;
  z-index: 10;
  transform: translateY(-69px);
  padding-left: 5px;
  padding-right: 5px;
}
.uslugi__hours_wrapper{
  width: 97px;
  display: flex;
  justify-content: space-between;
}

@media (max-width: 1200px) {
  .header_booking {
    margin-top: 17px;
    margin-bottom: 12px;
    font-size: 25px;
  }

  .name-section {
    font-size: 25px;
  }

  .name_subsection {
    font-size: 15px;
  }

  .logo img {
    width: 100px;
    height: 38px;
  }

  .text-field__input {
    height: 27px;
    font-size: 15px;
    width: 100%;
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
    left: 13px;
  }

  .date_time_end__text::after {
    font-size: 10px;
    content: 'дата выезда';
    transform: translateY(-35px);
    left: 13px;
  }

  .date_time__icon::before {
    left: 160px;
    content: url(/src/assets/images/calendar-select.svg);
  }

  .lodge__img {
    height: 200px;
  }

  .info-card-lodge {
    height: 250px;
  }

  .lodge__name {
    font-size: 10px;

    & p {
      margin-bottom: 0;
    }
  }

  .card_lodge__footer {
    margin-top: 12px;
    align-items: center;
  }

  button.footer__btn {
    width: 88px;
    height: 23px;
    font-size: 13px;
  }

  .icon__check {
    width: 22px;
    height: 22px;
    background-size: 65%;
  }

  .uslugi_card__footer {
    padding-left: 9px;
  }

  .uslugi_card__img {
    width: 100%;
    height: 133px;
  }

  .uslugi_card {
    width: 130px;
  }

  .uslugi_card__btn-popup {
    width: 20px;
    height: 20px;
    background-size: 40%;
  }
  .uslugi_card__check {
    width: 20px;
    height: 20px;
    background-size: 40%;
  }
  

  .uslugi_card__add {
    width: 20px;
    height: 20px;
    background-size: 40%;
  }
  .order_item__info{
    justify-content: space-between;
  }
  .order_item:not(:first-child){
    margin-top: 0px;
  }
  .order_item{
    font-size: 12px;
    padding-bottom: 6px;
    margin-bottom: 6px;
  }
  .confirm__checkbox-wrapper{
    align-items: flex-start;
  }
  .confirm__checkbox__label{
    font-size: 12px;
  }
  button.confirm__btn{
    height: 29px;
    font-size: 12px;
  }
  .service_popup{
    width: 130px;
  }
  .row_service_popup img{
    width: 23px;
  }
  .row_service_popup__input_hours{
    font-size: 12px;
    width: 24px;
  }
  .uslugi__hours_wrapper{
    width: 75px;
  }
  .service_popup__date_time__input{
    width: 75px;
    font-size: 12px;    
  }
  .service_popup__date_time__icon::before{
    content: '';
  }
  .service_popup__wrapper_time{
    padding: 0px 2px;
  }
  .row_service_popup img{
    width: 14px;
  }
}
</style>
