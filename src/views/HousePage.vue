<template lang="pug">
div    
    header.header2.active             
        .container
            .header2__container.row.align-items-center
                .header2__logo.col-5
                    img(src="../assets/images/logo2.svg")
                ul.col-3.offset-2.d-flex.header2__nav
                    li дома
                    li активный отдых
                    li услуги
                .header2__icon_feed_back.col-2
                    img(src="../assets/images/telefon2.svg")
                    button забронировать
    section.house_typ(style="padding-top: 191px")
        .container 
            .section_row
                h4.section_name виды домов 
                .d-flex.container_icon
                    .circle
                        img.circle__arrow_icon(src="../assets/images-house/arrow-left.svg")
                    .circle
                        img.circle__arrow_icon(src="../assets/images-house/arrow-right.svg") 
            .row 
                .col-6 
                    p.house__name Дом Мельника
                    .house__image(style="background-image: url(src/assets/images-house/house-2.png)")
                .col-6
                    .row(style="margin-bottom:64px") 
                        .col-6
                            .house__name_description Описание 
                            .house__text_description двухэтажный деревянный дом, где могут разместиться до 14 человек. 3 просторные комнаты, в которых будет удобно и парам, и семьям с детьми. 

                        .col-6 
                            .house__name_description Стоимость
                            .row_cost 
                                .house__text_description будни (пн-чт)
                                .house__text_description 10 000 р.
                            .row_cost 
                                .house__text_description выходные (пт-сб-вс) <br> и праздничные дни  
                                .house__text_description 15 000 р.
                            .row_cost 
                                .house__text_description Новый год 2024 (с 31 декабря <br> по 2 января) 2-е суток 
                                .house__text_description 95 000 р.
                            .row_cost 
                                .house__text_description с 2 по 7 января 2024 года <br> (сутки)
                                .house__text_description 30 000 р.
                            .row_cost 
                                .house__text_description стоимость при бронирова- <br> нии 2-х и более суток <br> (с 2 по 7 января 2024 года)
                                .house__text_description 25 000 р.
                    .row(style="margin-bottom:31px") 
                        .col-6 
                            .house__name_description Удобства  
                            .house__text_description кухня - полный комплект посуды на 14 человек, холодильник, обеденный стол, электроплита с духовым шкафом, микроволновая печь, электрочайник, санузел - горячая и холодная вода, музыкальный центр, 4 телевизора
                        .col-6 
                            .house__name_description Доступность
                            .house__text_description до воды 150 м <br> до бани 50 м <br> до беседки 5 м
                    .row 
                        .col-6 
                            .house__name_description Включено в проживание
                            .house__text_description пользование спортивными и детскими площадками, надувным аквапарком, пользование мангалом и решеткой, охраняемая парковка, охраняемый причал
                        .col-6 
                            .house__name_description Факты о доме
                            .house__text_description В пермских строгановских вотчинах, в начале XX века, действовали более 50 мельниц, которые местную и государственную казну пополняли. Поэтому и дом, названный в честь мельника, отличается особым уютом и добротностью
            .row 
                p.photogalery Фотогалерея
            .row
                .col-4
                    .photogalery__card 
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-2.png)")
                        .photogalery__name спальня
                .col-4
                    .photogalery__card 
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-3.png)")
                        .photogalery__name вторая спальня
                .col-4
                    .photogalery__card 
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-4.png)")
                        .photogalery__name третья спальня
            .photogalery_next
                .photogalery_next__text далее
                .photogalery_next__icon 
                    img(src="../assets/images-house/arrow-next.svg")
    section.house_typ_glamping
        .container
            .section_row
                h4.section_name глэмпинг
                .d-flex.container_icon
                    .circle
                        img.circle__arrow_icon(src="../assets/images-house/arrow-left.svg")
                    .circle
                        img.circle__arrow_icon(src="../assets/images-house/arrow-right.svg") 
            .row 
                .col-6
                    .row(style="margin-bottom:64px")
                        .col-6
                            .house__name_description Описание 
                            .house__text_description двухэтажный деревянный дом, где могут разместиться до 14 человек. 3 просторные комнаты, в которых будет удобно и парам, и семьям с детьми.
                        .col-6
                            .house__name_description Стоимость
                            .row_cost 
                                .house__text_description будни (пн-чт)
                                .house__text_description 10 000 р.
                            .row_cost 
                                .house__text_description выходные (пт-сб-вс) <br> и праздничные дни  
                                .house__text_description 15 000 р.
                            .row_cost 
                                .house__text_description Новый год 2024 (с 31 декабря <br> по 2 января) 2-е суток 
                                .house__text_description 95 000 р.
                            .row_cost 
                                .house__text_description с 2 по 7 января 2024 года <br> (сутки)
                                .house__text_description 30 000 р.
                            .row_cost 
                                .house__text_description стоимость при бронирова- <br> нии 2-х и более суток <br> (с 2 по 7 января 2024 года)
                                .house__text_description 25 000 р.
                    .row(style="margin-bottom:31px") 
                        .col-6 
                            .house__name_description Удобства  
                            .house__text_description кухня - полный комплект посуды на 14 человек, холодильник, обеденный стол, электроплита с духовым шкафом, микроволновая печь, электрочайник, санузел - горячая и холодная вода, музыкальный центр, 4 телевизора
                        .col-6 
                            .house__name_description Доступность
                            .house__text_description до воды 150 м <br> до бани 50 м <br> до беседки 5 м
                    .row 
                        .col-6 
                            .house__name_description Включено в проживание
                            .house__text_description пользование спортивными и детскими площадками, надувным аквапарком, пользование мангалом и решеткой, охраняемая парковка, охраняемый причал                        
                .col-6
                    p.house__name Для двоих
                    .house__image(style="background-image: url(src/assets/images-house/house-3.png)")
            .row 
                p.photogalery Фотогалерея
            .row
                .col-4
                    .glamping__photogalery__card
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-2.png)")
                        .photogalery__name веранда
                .col-4
                    .glamping__photogalery__card 
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-3.png)")
                        .photogalery__name внутри
                .col-4
                    .glamping__photogalery__card 
                        .photogalery__image(style="background-image: url(src/assets/images-house/house-1-4.png)")
                        .photogalery__name спальные места
            .photogalery_next
                .photogalery_next__text далее
                .photogalery_next__icon 
                    img(src="../assets/images-house/arrow-next.svg")
    section.placement 
        .container           
            h4.about_us__header бронирование
            .placement__form.row
                .date_time.date_time__icon.date_time__text.col-3
                    input.date_time__input
                .date_time.date_time__icon.date_time_end__text.col-3
                    input.date_time__input
                .quantity_guests.quantity_guests__text  
                    input.quantity_guests__input
                .checkbox_container
                    div.checkbox__header показать свободные:
                    input.checkbox__input(type="checkbox" id="house")
                    label.checkbox__name(for="house") дома
                    input.checkbox__input(type="checkbox" id="glamping")
                    label.checkbox__name(for="glamping" style="margin-left:10px") глемпинг
                button.placement__form__button_search найти
            .row.placement__cantainer_card
                .col-4 
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house1-1.png)")
                        .container_info-graph
                            .house_name Дом Кузнеца
                            .wrapper_cost_capacity
                                .house_cost ₽ 10000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 11 чел
                        .container_footer 
                            .footer_text 2 смежные и 2 изолированые спальни, просторная кухня-гостиная, санузел
                            .footer_button забронировать
                .col-4 
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house2-1.png)")
                        .container_info-graph
                            .house_name Дом Мельника
                            .wrapper_cost_capacity
                                .house_cost ₽ 10000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 11 чел
                        .container_footer 
                            .footer_text 3 изолированные спальни, просторная кухня-гостиная с диваном, санузел
                            .footer_button забронировать
                .col-4 
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house3-1.png);background-position: 0px -170px")
                        .container_info-graph
                            .house_name Дом Ямщика
                            .wrapper_cost_capacity
                                .house_cost ₽ 10000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 14 чел
                        .container_footer 
                            .footer_text 3 изолированные спальни, просторная кухня-гостиная с диваном и два санузла
                            .footer_button забронировать
                            .row.placement__cantainer_card
                .col-4(style="margin-top: 41px")
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house4-1.png)")
                        .container_info-graph
                            .house_name Дом Охотника
                            .wrapper_cost_capacity
                                .house_cost ₽ 25000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 40 чел
                        .container_footer 
                            .footer_text Дом полностью + большая веранда или половина дома + кафе и малая веранда
                            .footer_button забронировать
                .col-4(style="margin-top: 41px")
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house5-1.png)")
                        .container_info-graph
                            .house_name Дом Рыбака
                            .wrapper_cost_capacity
                                .house_cost ₽ 5500
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 4 чел
                        .container_footer 
                            .footer_text 2 изолированные спальни, просторная кухня-гостиная с диваном и два санузел
                            .footer_button забронировать
                .col-4(style="margin-top: 41px; margin-bottom:95px")
                    .placement__card 
                        .wrapper_img(style="background-image:url(src/assets/images/house6-1.png);background-position: 0px -114px")
                        .container_info-graph
                            .house_name Дом Гончара(1 этаж)
                            .wrapper_cost_capacity
                                .house_cost ₽ 5000
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до 6 чел
                        .container_footer 
                            .footer_text  изолированные спальни, просторная кухня-гостиная с диваном и санузел
                            .footer_button забронировать
    footer.footer
        .container
            .footer_container
                div 2023 @ СТРОГАНОВСКИЕ ПРОСТОРЫ
                div Пермь. Официальный сайт.
</template>

<script>
export default {
    name: 'house-page',
    setup () {
        

        return {}
    }
}
</script>

<style scoped>
/* ГЛЭМПИНГ */
.glamping__photogalery__card{
    background-color: #F5F3F1;
    border-radius: 30px;
}
.house_typ_glamping{
    padding-top: 72px;
}
.house_typ_glamping{
    background-color: #fff;
}
.circle{
    width: 55px;
    height: 55px;
    border-radius: 50%;
    background-color: #005D4B;
    display: flex;
    align-items: center;
    justify-content: center;
}

.row_cost{
    display: flex;
    justify-content: space-between;    
    align-items: center;
}
.row_cost:not(:last-child){
    border-bottom: 1px #005D4B solid;
}
.house__text_description{
    color: black;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300;
    line-height: 20.33px;    
}
.photogalery{
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
    margin-top: 22px;
    margin-bottom: 10px;
}
.house__name_description{
    color: #003731;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
    margin-bottom: 10px;
}
.photogalery_next{
    display: flex;
    justify-content: flex-end;
    margin-top: 8px;
    padding-bottom: 70px;
}
.photogalery__image{
    border-radius: 30px;
    width: 407px;
    height: 246px;    
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
.photogalery__name{
    color: #032D28;
    font-size: 11px;
    font-family: 'Lato';
    font-weight: 400;
    display: flex;
    justify-content: center;
    padding: 19px 0px;
}
.photogalery__card{
    background-color: #fff;
    border-radius: 30px;
}
.house__image{
    border-radius: 30px;
    width: 621px;
    height: 641px;    
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
.house__name{
    color: #003731;
    font-size: 17px;
    font-family: Lato;
    font-weight: 400;
    margin-bottom: 18px;
}
.section_name{
    color: #003C30;
    font-size: 47px;
    font-family: 'Apoc Normal';
    font-weight: 300;    
}
.section_row{
    margin-bottom: 45px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.house_typ{
    background-color: #F5F3F1;
}
</style>