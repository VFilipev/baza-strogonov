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
                .order_info__header.order_number Подтверждение №20200123
                .row.p-0.d-flex.main_info
                    .col-6.col-sm-4.order_info__input_wrapper.order_info__date_start__text.p-sm-0
                        .order_info__input_date {{getDate(orderStore.orderlodge_set[0].start_date)}}
                    .col-6.col-sm-4.order_info__input_wrapper.order_info__date_end__text.p-sm-0
                        .order_info__input_date {{getDate(orderStore.orderlodge_set[0].end_date)}}
                    .col-6.col-sm-1.order_info__input_wrapper.order_info__day__text.p-sm-0
                        .order_info__input_day {{ getDurationOrder() }}
                    .col-6.col-sm-3.order_info__input_wrapper.order_info__lodge__text.p-sm-0
                        .order_info__input_lodge {{ orderStore.orderlodge_set[0].lodge.name }}
                .order_info__header.detail_info Детали бронирования
                .order_info__item.mt-0
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
                .row.row_cost
                    .col-6.order_info__header Итоговая стоимость:
                    .col-6.order_info__header Стоимость предоплаты:
                .d-flex(style="margin-bottom:24px")
                    .order_info__input_wrapper(style="width:50%")
                        .order_info__input_cost {{ orderStore.cost + ' р.' }}
                    .order_info__input_wrapper(style="width:50%")
                        .order_info__input_pay {{ orderStore.cost * 0.5 + ' р.' }}
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
                    button.confirm__btn(@click="saveOrder") Отправить договор на почту
    .modal-mask(v-if="isShowModalConfirm")
        .modal-wrapper
            .modal-container 
                .modal-body 
                    .modal-text Договор №20200123 
                    .modal-text(style="margin-bottom: 19px; color:black") отправлен на электронную почту
                    button.modal-button(@click="toMainPage") вернуться на главную 

</template>

<script>
import { useOrderStore } from '../stores/orderStore';
import { ref, onMounted } from 'vue'
import moment from 'moment-with-locales-es6';
import { Order } from '../api'
import { useRouter } from 'vue-router'


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
            let available = moment(service.end_date, 'YYYY-MM-DDTHH:mm').hour() - moment(service.start_date, 'YYYY-MM-DDTHH:mm').hour()
            return dateStart + ', ' + time + ', ' + available + ' часа'
        }
        const getDate = (date) => {
            moment.locale('ru')
            let dat = moment(date).format('DD MMMM YYYY')
            return dat + ' г.' + ' (' + moment(date).format('ddd') + ')'
        }
        const getDurationOrder = () => {
            let start = moment(orderStore.orderlodge_set[0].start_date)
            let end = moment(orderStore.orderlodge_set[0].end_date)
            let diff = moment.duration(end.diff(start)).as('days')
            return diff
        }
        const saveOrder = async () => {
            let order = {}
            order.customer = orderStore.customer
            order.cost = orderStore.cost
            order.email = orderStore.email
            order.phone = orderStore.phone
            let start = moment(orderStore.orderlodge_set[0].start_date).format('DD.MM.YYYY')
            let end = moment(orderStore.orderlodge_set[0].end_date).format('DD.MM.YYYY')
            order.orderlodge_set = [{}]
            order.orderlodge_set[0].lodge = orderStore.orderlodge_set[0].lodge.id
            order.orderlodge_set[0].start_date = start
            order.orderlodge_set[0].end_date = end
            order.orderlodge_set[0].cost = 0
            order.products_set = orderStore.products_set
            order.services_set = orderStore.services_set
            console.log(order);
            isShowModalConfirm.value = true
            await Order.save(order)
        }
        let isShowModalConfirm = ref(false)
        const router = useRouter()
        const getOrderId = async() =>{
            let orderId = (await Order.last()).data
            console.log(orderId);
        }
        const toMainPage = () => {
            router.push({
                name: 'main-page',
            })
        }
        onMounted(() =>{
            getOrderId()
        })
        return {
            orderStore,
            isFeedback,
            serviceList,
            getTime,
            getDate,
            getDurationOrder,
            saveOrder,
            isShowModalConfirm,
            toMainPage
        }
    }
}
</script>

<style scoped>
button.modal-button {
    width: 205px;
    height: 36px;
    border: 0;
    background-color: #005D4B;
    border-radius: 36px;
    color: #FCF2EA;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 400;
}

.modal-text {
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
}

.modal-body {
    width: 244px;
}

.modal-wrapper {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
}

.modal-container {
    display: flex;
    text-align: center;
    align-items: center;
    justify-content: center;
    position: relative;
    width: 400px;
    height: 205px;
    margin: 0 auto;
    top: 40%;
    padding: 10px;
    background-color: #fff;
    border-radius: 30px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    /*max-height: calc(100vh - 50px);*/
    overflow: hidden;
}

.modal-mask {
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    backdrop-filter: blur(2px);
    display: table;
    transition: opacity .3s ease
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
}
.order_info__item:not(:first-child) {
        margin-top: 28px;
    }

.item__name {
    width: 176px;
}

.order_info__input_date {
    border-radius: 20px;
    border: 1px #A4A4A4 solid;
    width: 100%;
    height: 67px;
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
    padding-left: 20px;
    display: flex;
    align-items: center;
}

.order_info__input_day {
    border-radius: 20px;
    border: 1px #A4A4A4 solid;
    width: 100%;
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
    border-radius: 20px;
    border: 1px #A4A4A4 solid;
    width: 100%;
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
    border-radius: 20px;
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
    border-radius: 20px;
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
    left: 15px;
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
    left: 1.125rem;
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
    left: 15px;
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
.order_number{
    margin-top:28px
}
.main_info{
    margin-top:38px
}
.detail_info{
    margin-top:32px;
    margin-bottom:35px;
}
.row_cost{
    margin-top:34px;
    margin-bottom:13px;
}
@media (max-width: 1200px) {
    .top__header p{
        font-size: 25px;
        font-weight: 400;
    }
    .top__header{
        width: 80%;
        display: flex;
        text-align: center;
    }
    .top__wrapper{
        height: 125px;
    }
    .order_info__header{
        font-size: 12px;
    }
    .order_info__input_date{
        height: 30px;
        width: 100%;
        font-size: 12px;
        padding-left: 15px;
    }
    .order_info__date_start__text::after{
        font-size: 12px;
        left: 10px;
        transform: translateY(-39px);
    }
    .order_info__date_start__text{
        margin-bottom: 10px;
    }
    .order_info__date_end__text::after{
        font-size: 12px;
        left: 10px;
        transform: translateY(-39px);
    }
    .order_number{
        margin-top: 15px;
    }
    .main_info{
        margin-top: 15px;
    }
    .order_info__input_day{
        height: 30px;
        width: 100%;
        font-size: 12px;
        padding-left: 15px;
        justify-content: start;
    }
    .order_info__day__text::after{
        font-size: 12px;
        left: 10px;
        transform: translateY(-39px);
    }
    .order_info__input_lodge{
        height: 30px;
        width: 100%;
        font-size: 12px;
        padding-left: 15px;
    }
    .order_info__lodge__text::after{
        font-size: 12px;
        left: 10px;
        transform: translateY(-39px);
    }
    .detail_info{
        margin: 15px 0px;
    }
    .order_info__item{
        padding-bottom: 18px;   
        align-items: center;     
    }
    .order_info__item:not(:first-child) {
        margin-top: 18px;
    }
    .row_cost{        
        margin: 19px 0px 15px 0px;
    }
    .order_info__input_cost,.order_info__input_pay{
        height: 30px;
        font-size: 12px;
        padding-left: 15px;
    }
    .confirm__checkbox__label{
        font-size: 10px;
    }
    .confirm__btn{
        font-size: 10px;
    }
}
</style>