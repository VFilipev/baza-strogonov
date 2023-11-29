<template lang="pug"> 
div.container  
  h1.name-section бронирование
  section.info 
    .row 
      .col-6.info-form
        div.name_subsection Введите данные:
        input.text-field__input(placeholder="ФИО" type="text")
        input.text-field__input(placeholder="Телефон" type="tel")
        input.text-field__input(placeholder="Email" type="email")
        div.data-time-container
          .date_time.date_time__icon.date_time__text
            input.date_time__input(@focus="datePicker.dateStart = true, datePicker.dateEnd = false" 
            v-model="order.dateStart") 
            .date_picker_wrapper
              DatePicker(v-if="datePicker.dateStart" :masks="masks" :color="selectedColor" v-model.string="order.dateStart")
          .date_time.date_time__icon.date_time_end__text
            input.date_time__input(@focus="datePicker.dateEnd = true, datePicker.dateStart = false" 
            v-model="order.dateEnd") 
            .date_picker_wrapper
              DatePicker(v-if="datePicker.dateEnd" :masks="masks" :color="selectedColor" v-model.string="order.dateEnd")
      .col-6
        .info-card-lodge 
          .lodge__img(:style="{'background-image': 'url(' + order.lodge.mainPhoto + ')'}")
          .card_lodge__footer 
            .lodge__name 
              p {{ order.lodge.name }}
            .footer__icon 
              button.footer__btn выбрано                
              .icon__check   
  section.uslugi(style="margin-top: 20px") 
    .row 
      .name_subsection Добавить услуги:
    .row 
      .col-12
        .slider_wrapper 
          swiper(slidesPerView="6" :spaceBetween="40" ref="swiper")
            swiper-slide(v-for="service in servicesList")
              .col-2 
                .uslugi_card 
                  .uslugi_card__img(:style="{ backgroundImage: `url(${service.photo})` }")
                  .uslugi_card__footer 
                    .uslugi_card__text {{ service.name }}
                    .footer_right 
                      .uslugi_card__text {{ service.cost }}
                      .uslugi_card__add(v-if="!service.isAdd" @click="addService(service)")
                      .uslugi_card__check(v-else @click="removeService(service)")
            swiper-slide(v-for="product in productsList")
              .col-2 
                .uslugi_card 
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
    .order_item 
      .order_item__name {{ order.lodge.name }}
      .order_item__info
        .order_item__cost {{ calcCost }}
        .order_item__date {{ parserDate(order.dateStart) + '-' + parserDate(order.dateEnd)}}
    template(v-if="order.products.length > 0")
      .order_item(v-for="product in order.products") 
        .order_item__name {{ product.name }}
        
        .order_item__cost {{ product.cost + 'р' }}
        
  section.confirm(style="margin-top:25px; height: 1080px" )
    div.d-flex.justify-content-between  
      .confirm__checkbox-wrapper
        .confirm__checkbox
            .confirm__checkbox-box-wrapper 
                .confirm__checkbox-box(@click="isConfirm = !isConfirm" :class="{icon_check : isConfirm}")
                    //- .confirm__checkbox-icon(v-if="filter.isHouse")
                    //-     img(src="../assets/images/checkbox.svg")
        span.confirm__checkbox__label Я согласен с условиями политики конфиденциальности и даю разрешение на обработку персональных данных    
      button.confirm__btn(:disabled="!isConfirm" @click="toBooking") забронировать
  

</template>

<script>
import { Calendar, DatePicker } from 'v-calendar';
import { ref, computed } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue';
import moment from 'moment';
import 'swiper/css';

import controlSwiper from '../components/controlSwiper.vue';

import { useRouter } from 'vue-router'

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
    let datePicker = ref({
      dateStart: false,
      dateEnd: false
    })
    const calcCost = computed(() => {
      let start = moment(order.value.dateStart, 'DD.MM.YYYY')
      let end = moment(order.value.dateEnd, 'DD.MM.YYYY')      
      let diff = moment.duration(end.diff(start)).as('days')
      return diff * order.value.lodge.cost
    })    
    const parserDate = (date) => {
      return moment(date, 'DD.MM.YYYY').format('DD/MM/YY')
    }
    let order = ref({
      user: {
        name: '',
        phone: '',
        mail: ''
      },
      dateStart: '22.11.2023',
      dateEnd: '25.11.2023',
      lodge: {
        name: 'Дом Кузнеца',
        mainPhoto: 'src/assets/images-booking/lodge.png',
        cost: 15000
      },
      services: [],
      products:[]
    })
    const selectedColor = ref('green')
    const masks = ref({
      modelValue: 'DD.MM.YYYY',
    })
    let servicesList = ref([      
      {
        photo: 'src/assets/images-uslugi/images-2.png',
        name: 'чан',
        cost:'3000р/2ч', 
      },
      {
        photo: 'src/assets/images-uslugi/images-3.png',
        name: 'баня',
        cost:'2400р/2ч',        
      },                        
    ])
    let productsList = ref([
      {
        id:1,
        photo: 'src/assets/images-uslugi/images-1.png',
        name: 'Снегоход',
        cost:3200,      
      },
      {
        id:2,
        photo: 'src/assets/images-uslugi/images-11.png',
        name: 'Зоопарк',
        cost:150,
      },
      {
        id:3,
        photo: 'src/assets/images-uslugi/images-10.png',
        name: 'Сапы',
        cost:1000,        
      },
      {
        id:4,
        photo: 'src/assets/images-uslugi/images-6.png',
        name: 'Каток',
        cost:150,        
      },
      {
        id:5,
        photo: 'src/assets/images-uslugi/images-4.png',
        name: 'Лыжи',
        cost:150,        
      },      
    ])
    const addService = (service) => {
      service.isAdd = true
    }
    const removeService = (service) => {
      service.isAdd = false
    }
    const addProduct = (product) => {            
      order.value.products.push(product)
    }
    const removeProduct = (product) => {
      let findIndex = order.value.products.findIndex(x => x.id == product.id)
      order.value.products.splice(findIndex, 1)
    }
    const isAdd = (id) =>{
      if(order.value.products.length > 0){
        let item = order.value.products.find(x => x.id == id)
        if(item){
          return true
        }
      }      
      else {
        return false
      }
    }
    let isConfirm = ref(false)
    const router = useRouter()    
    let toBooking = () => {
      router.push({
        name: 'BookingConfirm',        
      })
    }
    return {
      order,
      datePicker,
      selectedColor,
      masks,
      servicesList,
      addService,
      removeService,
      addProduct,
      removeProduct,      
      calcCost,
      parserDate,
      productsList,
      isAdd,
      isConfirm,
      toBooking
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.confirm__checkbox__label{
    font-family: 'Lato';
    font-weight: 400;
    font-size: 20px;
    color: black;
    padding-left: 6px;
}
.confirm__checkbox__label.active{
    color: #005D4B;
}
.confirm__checkbox-wrapper{
    display: flex;
    width: 100%;
    align-items: center;
}
.confirm__checkbox{
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
    height:22px;
    flex-shrink: 0;
    flex-grow: 0;
    
}
.confirm__checkbox-box{
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    height:22px;
    width: 22px;
    display: inline-block;
    box-sizing: border-box;
    border-radius:8px;
    background-color: #fff;    
    border: 1px solid #B3B3B3;
    &.icon_check{
      background-color: #005D4B;
      background-image: url('src/assets/images-booking/icon-check-2.svg');
      background-repeat: no-repeat;
      background-position: center;
    }
}

.confirm__checkbox-icon{
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 22px;
    width: 22px;
}
.confirm__checkbox-box.active{    
    border: 1px solid #005D4B;    
}

.confirm__btn{
  width: 144px;
  height: 36px;
  border: 0;
  background-color: #005D4B;
  border-radius: 36px;
  color: #FCF2EA;
  font-size: 15px;
  font-family: 'Lato';
  font-weight: 400;
  &:disabled{
    background-color: #333333;
    cursor: not-allowed;
    opacity: .8;
  }
}

.order_item__info{
  display: flex;
  gap: 259px;
  
}

.order_item{
  display: flex;
  justify-content: space-between;
  color: #333333;
  font-size: 20px;
  font-family: 'Lato';
  font-weight: 400;
  border-bottom: 1px black solid;
  padding-bottom: 25px;
}

.order_item:not(:first-child){
  margin-top: 24px;
}

.uslugi_card__footer{
  display: flex;
  justify-content: space-between;
  padding-left: 22px;
  padding-right: 10px;
}

.footer_right{
  display: flex;
  gap: 4px;
  align-items: center;
}

.uslugi_card__add{
  width: 30px;
  height: 30px;
  border-radius: 30px;
  background-color: #005D4B;
  background-image: url('src/assets/images-booking/icon-add.svg');
  background-repeat: no-repeat;
  background-position: center;
  cursor: pointer;
}

.uslugi_card__check{
  width: 30px;
  height: 30px;
  border-radius: 30px;
  background-color: #005D4B;
  background-image: url('src/assets/images-booking/icon-check-service.svg');
  background-repeat: no-repeat;
  background-position: center;
  cursor: pointer;
}

.uslugi_card__text{
    display: flex;
    justify-content: center;
    color: #003731;
    font-size: 11px;
    font-family: 'Lato';
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
  margin-top: 97px;
  margin-bottom: 47px;
}

.name_subsection {
  font-family: 'Lato';
  font-size: 20px;
  margin-bottom: 21px;
}

.text-field__input {
  border-radius: 9px;
  border: 1px #A4A4A4 solid;
  width: 100%;
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
}</style>
