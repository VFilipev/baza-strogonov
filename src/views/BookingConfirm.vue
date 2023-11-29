<template lang="pug">
div
    section.top 
        .container
            .top__wrapper 
                .top__header 
                    p подтверждение бронирования
    section.order_info(style="margin-top:13px")
        .container
            .order_info__wrapper
                .p-18
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
                        .item__value Иванов Илья Кириллович
                    .order_info__item 
                        .item__name Телефон
                        .item__value +7(905)136-55-37
                    .order_info__item 
                        .item__name Email
                        .item__value iipochta@gmail.com
                    .order_info__item 
                        .item__name Проживание
                        .item__value Дом Кузнеца
                    .order_info__item 
                        .item__name Завтрак
                        .item__value Добавлен
                    .order_info__item 
                        .item__name Баня
                        .item__value 15.09.2023, 10:00, 2 часа
                    .row
                        .col-6.order_info__header(style="margin-top:34px;margin-bottom:13px") Итоговая стоимость:
                        .col-6.order_info__header(style="margin-top:34px") Стоимость предоплаты:
                    .d-flex
                        .order_info__input_wrapper(style="width:50%")
                            .order_info__input_cost 82400 р.
                        .order_info__input_wrapper(style="width:50%")
                            .order_info__input_pay 40000 р.
</template>

<script>
export default {
    name: 'BookingConfirm',
    setup () {
        

        return {}
    }
}
</script>

<style >
.order_info__item{
    display: flex;
    padding-left: 9px;
    padding-bottom: 27px;
    border-bottom: 1px #A4A4A4 solid;
    &:not(:first-child){
        margin-top: 28px;
    }
}
.item__name{
    width: 176px;
}
.order_info__input_date{
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
.order_info__input_day{
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
.order_info__input_lodge{
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
.order_info__input_cost{
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
.order_info__input_pay{
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
.order_info__input_wrapper{
    position: relative;
}
.order_info__date_start__text::after{
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
.order_info__day__text::after{
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
.order_info__lodge__text::after{
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
.order_info__date_end__text::after{
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
.top__header p{
    color: white;
    font-size: 47px;
    font-family: 'Apoc Normal';
    font-weight: 300;    
    
}
.order_info__wrapper{    
    border: 1px #A4A4A4 solid;
    border-radius: 20px;
    padding-bottom: 24px;
}
.p-18{
    padding: 0px 18px;
}
.order_info__header{    
    color: #003731;
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 400;
}
</style>