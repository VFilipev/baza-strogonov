<template lang="pug">
div
    section.top 
        .container
            .top__wrapper 
                .top__header 
                    p подтверждение бронирования
    section.order_info(style="margin-top:13px")
        .container
            .order_info__wrapper.p-18

                .order_info__header(style="margin-top:28px") Подтверждение №20200123
                .d-flex(style="margin-top:38px")
                    .order_info__input_wrapper.order_info__date_start__text
                        .order_info__input_date 13 сентября 2023 г. (ср)
                    .order_info__input_wrapper.order_info__date_end__text
                        .order_info__input_date 21 сентября 2023 г. (чт)
                    .order_info__input_wrapper.order_info__day__text
                        .order_info__input_day 8
                    .order_info__input_wrapper.order_info__lodge__text
                        .order_info__input_lodge Дом Кузнеца
                .order_info__header(style="margin-top:32px;margin-bottom:35px") Детали бронирования
                .order_info__item 
                    .item__name ФИО
                    .item__value {{ orderStore.customer }}
                .order_info__item 
                    .item__name Телефон
                    .item__value {{ orderStore.phone }}
                .order_info__item 
                    .item__name Email
                    .item__value {{ orderStore.email }}
                .order_info__item 
                    .item__name Проживание
                    .item__value {{ orderStore.orderlodge_set[0].lodge.name }}
                .order_info__item 
                    .item__name Завтрак
                    .item__value Добавлен
                template(v-if="orderStore.products_set.length > 0")
                    .order_info__item(v-for="product in orderStore.products_set")
                        .item__name {{ product.name }} 
                        .item__value Добавлен 
                template(v-if="orderStore.services_set.length > 0")
                    .order_info__item(v-for="service in orderStore.services_set")
                        .item__name {{ serviceList[service.name] }}                
                        .item__value {{ getTime(service) }}                
                .row
                    .col-6.order_info__header(style="margin-top:34px;margin-bottom:13px") Итоговая стоимость:
                    .col-6.order_info__header(style="margin-top:34px") Стоимость предоплаты:
                .d-flex(style="margin-bottom:24px")
                    .order_info__input_wrapper(style="width:50%")
                        .order_info__input_cost 82400 р.
                    .order_info__input_wrapper(style="width:50%")
                        .order_info__input_pay 40000 р.
    section.order_info-contract(style="margin-top:13px")
        .container
            .order_info__wrapper.p-18
                .order_info__header(style="margin-top: 10px") Процедура подписания договора и предоплаты: 
                .order_info__header(style="color: black") Далее вам на почту будет направлен договор, после подписания которого, нужно будет произвести предоплату
                div.d-flex.justify-content-between(style="padding-bottom: 13px") 
                    .confirm__checkbox-wrapper
                        .confirm__checkbox
                            .confirm__checkbox-box-wrapper 
                                .confirm__checkbox-box(@click="isFeedback = !isFeedback" :class="{icon_check : isFeedback}")
                        span.confirm__checkbox__label требуется обратная связь с администратором
                    button.confirm__btn(@click="toBooking") Отправить договор на почту
    div(style="height: 300px") 
</template>

<script>
import { useOrderStore } from '../stores/orderStore';
import { ref } from 'vue'
import moment from 'moment';
export default {
    name: 'BookingConfirm',
    setup() {
        const orderStore = useOrderStore()
        const isFeedback = ref(false)      
        const serviceList = {
            'CH': 'Чан',
            'SN': 'Сауна',
        }          
        const getTime = (service) => {
            let dateStart = moment(service.start_date, 'YYYY-MM-DDTHH:mm').format('DD.MM.YYYY')            
            let time = moment(service.start_date, 'YYYY-MM-DDTHH:mm').format('HH:mm')
            let available = moment(service.start_end, 'YYYY-MM-DDTHH:mm').hour()                        
            return dateStart + ', ' + time + ', ' + available + 'часа'
            
        }
        return {
            orderStore,
            isFeedback,
            serviceList,
            getTime
        }
    }
}
</script>

<style scoped>

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
  width: 260px;
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
.order_info__item {
    display: flex;
    padding-left: 9px;
    padding-bottom: 27px;
    border-bottom: 1px #A4A4A4 solid;

    &:not(:first-child) {
        margin-top: 28px;
    }
}

.item__name {
    width: 176px;
}

.order_info__input_date {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 402.5px;
    height: 67px;
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
    padding-left: 30px;
    display: flex;
    align-items: center;
}

.order_info__input_day {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 126.5px;
    height: 67px;
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
    display: flex;
    align-items: center;
    justify-content: center;
}

.order_info__input_lodge {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 298.5px;
    height: 67px;
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
    padding-left: 30px;
    display: flex;
    align-items: center;
}

.order_info__input_cost {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    /* width: 50%; */
    height: 67px;
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
    padding-left: 25px;
    display: flex;
    align-items: center;
}

.order_info__input_pay {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    /* width: 50%; */
    height: 67px;
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
    padding-left: 25px;
    display: flex;
    align-items: center;
}

.order_info__input_wrapper {
    position: relative;
}

.order_info__date_start__text::after {
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
    transform: translateY(-80px);
    padding-left: 5px;
    padding-right: 5px;
}

.order_info__day__text::after {
    font-family: 'Montserrat';
    font-size: 17px;
    content: 'ночей';
    color: #bdbdbd;
    position: absolute;
    display: flex;
    align-items: center;
    left: 1.925rem;
    background-color: #fff;
    z-index: 10;
    transform: translateY(-80px);
    padding-left: 5px;
    padding-right: 5px;
}

.order_info__lodge__text::after {
    font-family: 'Montserrat';
    font-size: 17px;
    content: 'размещение';
    color: #bdbdbd;
    position: absolute;
    display: flex;
    align-items: center;
    left: 1.525rem;
    background-color: #fff;
    z-index: 10;
    transform: translateY(-80px);
    padding-left: 5px;
    padding-right: 5px;
}

.order_info__date_end__text::after {
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
    transform: translateY(-80px);
    padding-left: 5px;
    padding-right: 5px;
}

.top__wrapper {
    background-color: #005D4B;
    height: 225px;
    border-radius: 0px 0px 20px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.top__header p {
    color: white;
    font-size: 47px;
    font-family: 'Apoc Normal';
    font-weight: 300;

}

.order_info__wrapper {
    border: 1px #A4A4A4 solid;
    border-radius: 20px;
    padding-bottom: 24px;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.p-18 {
    padding: 0px 18px;
}

.order_info__header {
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
}
</style>