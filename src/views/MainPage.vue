<template lang="pug"> 
div     
    .header_sticky(:class="{'active' : showHeader}")             
        .container
            .header_sticky__container.row.align-items-center
                .header_sticky__logo.col-5
                    img(src="../assets/images/logo2.svg")
                ul.header_sticky__nav.col-3.offset-2.d-flex
                    router-link(to="/house" tag="li" class="header_sticky__nav_link") дома                    
                    router-link(to="/uslugi" tag="li" class="header_sticky__nav_link") активный отдых / услуги
                .header_sticky__icon_feed_back.col-2
                    a(href="tel:+79026439294")
                        img(src="../assets/images/telefon2.svg")
                    button забронировать
                                          
    section.first_page        
        .container__first_page
            .overlay
            template(v-for="(photo, index) in photoList" ) 
                img.photo(:src="photo" :class="{ active : index == selPhoto }")                
            .container__header
                .container
                    .header
                        .row.align-items-center
                            .col-5.logo
                                img(src="../assets/images/logo.png")
                            .col-3.offset-2.d-flex.header__nav                                
                                router-link(to="/house", tag="a",  class="header__nav__link") дома
                                router-link(to="/uslugi", tag="a",  class="header__nav__link") активный отдых / услуги
                            .col-2.d-flex.header__nav     
                                a(href="tel:+79026439294")                       
                                    img(src='../assets/images/telefon.svg')
                                button.header__nav__link.header__nav__button забронировать
                    .row.d-flex.justify-content-between
                        .col-4.first_page__h1 уютные коттеджи 
                            |и глемпинг хвойном лесу
                            |на берегу камского моря
                        .col-4.first_page__h2 Уединеный отдых в уютном историческом месте Пермского края. 
                            |Насладитесь первозданой природой и европейским уровнем комфорта размещения в уютных коттеджах и номерах. 
                            |Зарядитесь эмоциямиот прогулки на квадроциклах, а после отдахните душой и телом в традиционной русской бане.                       
    .container_bg_gray            
    section.about_us(ref="au" id="aboutUs")
        .container
            h4.about_us__header нас выбирают, <br> потому что 
            .row.about_as__container_row
                .about_us__card_container.col-3                    
                    img.about_us__card__img(src="../assets/images/yoga.svg")
                    .about_us__card__header Комфорт
                    .about_us__card__text высокий уровень обслуживания <br>
                        |и внимание к деталям: сотрудники клуба стремятся удовлетворить все потребности и пожелания гостей,
                        |чтобы каждый момент проведенного времени <br> был приятным 
                        |и незабываемым
                .about_us__card_container.col-3.offset-1                   
                    img.about_us__card__img(src="../assets/images/bed.svg")
                    .about_us__card__header Уют
                    .about_us__card__text проживание в просторных и уютных <br> домиках, которые оборудованы всем <br> необходимым для идеального отдыха
                .col-4.offset-1 
                    img(src="../assets/images/about-as-winter-1.png" style="border-radius: 30px")
            .row.about_as__container_row
                .col-4 
                    img(src="../assets/images/about-as-winter-2.png" style="border-radius: 30px")
                .about_us__card_container.col-3   
                    img.about_us__card__img(src="../assets/images/uslugi.svg")
                    .about_us__card__header Услуги
                    .about_us__card__text благодаря широкому спектру услуг каждый <br> найдёт себе развлечение по душе: будь <br>
                        |то релакс в бане, или драйв на квадроцикле
                .about_us__card_container.col-3.offset-1                   
                    img.about_us__card__img(src="../assets/images/donate.svg")
                    .about_us__card__header Семейность
                    .about_us__card__text мы приветствуем семейность <br> и ориентацию на семейные ценности, <br> поэтому создали атмосферу, где каждый член семьи может насладиться отдыхом,  развлечениями и обществом друг друга
            .row.about_as__container_row
                .about_us__card_container.col-3                    
                    img.about_us__card__img(src="../assets/images/pine.svg")
                    .about_us__card__header Природа
                    .about_us__card__text у нас вы сможете насладиться и прочувствовать энергию богатой природы Пермского края, 
                        |ведь, благодаря расположению отеля вдали городской суеты, невозможно не проникнуться окружающим нас живописным миром  
                .about_us__card_container.col-3.offset-1                 
                    img.about_us__card__img(src="../assets/images/emoji.svg")
                    .about_us__card__header Впечатления
                    .about_us__card__text отдых в Строгановских Просторах оставит множество положительных впечатлений: об уникальной природе, спокойствии 
                        |и уединении с ней, комфорте, развлечениях и релаксе, а также о драгоценном времени, проведённом друг с другом
                .col-4.offset-1 
                    img(src="../assets/images/about-as-winter-3.png" style="border-radius: 30px")
    section.placement 
        .container           
            h4.about_us__header размещение
            .placement__form.row
                .date_time.date_time__icon.date_time__text.col-3
                    input.date_time__input(@focus="datePicker.dateStart = true, datePicker.dateEnd = false" 
                    v-model="filter.dateStart") 
                    .date_picker_wrapper
                        DatePicker(v-if="datePicker.dateStart" :masks="masks" :color="selectedColor" v-model.string="filter.dateStart")
                .date_time.date_time__icon.date_time_end__text.col-3
                    input.date_time__input(@focus="datePicker.dateEnd = true, datePicker.dateStart = false" 
                    v-model="filter.dateEnd") 
                    .date_picker_wrapper
                        DatePicker(v-if="datePicker.dateEnd" :masks="masks" :color="selectedColor" v-model.string="filter.dateEnd")
                .quantity_guests.quantity_guests__text(:class="{active : filter.personQuantity > 0}") 
                    .input_number_wrapper(:class="{active : filter.personQuantity > 0}")
                        .input_number__prefix
                            button.prefix_btn(@click="dec")
                                img(v-if="filter.personQuantity == 0" src="../assets/images/prefix.svg")
                                img(v-else src="../assets/images/prefix-active.svg")
                        .input_number__input 
                            input.input_number__in(type="text" :class="{active : filter.personQuantity > 0}" v-model="filter.personQuantity")
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
                button.placement__form__button_search найти
            .row.placement__cantainer_card
                .col-4(v-for="(house, index) in houseList")
                    .placement__card 
                        .wrapper_img(:style="{ backgroundImage: `url(${house.main_photo})` }")
                            .btn_house_detail(@click="showModalHouse = true, selectedHouse = house")
                        .container_info-graph
                            .house_name {{ house.name }}
                            .wrapper_cost_capacity
                                .house_cost ₽ {{ house.cost[0].cost }}
                                .house_capacity
                                    .house_capacity__icon 
                                        img(src="../assets/images/icon_emoji.svg")
                                    .house_capacity__text до {{ house.capacity }} чел
                        .container_footer 
                            .footer_text {{ house.short_description }}
                            .footer_button забронировать                
    section.service_section
        .container         
            .row.service     
                .service__header.col-2 услуги
            .row(style="padding-bottom: 94px") 
                .col-6
                    p.service__name_typ Активный отдых                    
                    .service__item 
                        .service__name настольный теннис
                        .service__cost 200
                    .service__item 
                        .service__name прокат лыж (1 час)
                        .service__cost 150
                    .service__item 
                        .service__name входной билет
                        .service__cost 250
                    .service__item 
                        .service__name аренда квадроцикла (30 мин)
                        .service__cost 1600
                    .service__item
                        .service__name аренда квадроцикла (1 час)
                        .service__cost 3200
                    .service__item
                        .service__name аренда снегохода (30 мин)
                        .service__cost 1600
                    .service__item
                        .service__name аренда снегохода (1 час)
                        .service__cost 3200
                    .service__item
                        .service__name доплата за пассажира
                        .service__cost 20%
                    .service__item
                        .service__name прицепные санки к снегоходу (не более 4-х человек)
                        .service__cost 40%
                .col-6
                    p Банные процедуры
                    .service__item 
                        .service__name баня на дровах (2 часа/пихтовый веник/травяной чай)
                        .service__cost 2400
                    .service__item
                        .service__name веник берёзовый
                        .service__cost 150
                    .service__item
                        .service__name банное полотенце
                        .service__cost 50
                    .service__item
                        .service__name халат
                        .service__cost 150
                    .service__item
                        .service__name тапочки
                        .service__cost 50
                    .service__item
                        .service__name чан (2 часа до 6 человек)
                        .service__cost 3000
    section.feedback_section(style="height: 1080px")
        .container
            .section_header ваши отзывы
            .row 
                .col-3
                    .card.rotate                   
                        .card__header
                            .card__user_photo
                                img(src="../assets/images/user_photo1.png")
                            .card__user_container
                                .card__user_name Екатерина Малинина
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                        .card__body
                            p.card__text Отдых в загородном клубе в Пермском крае был незабываемым. Мы оценили внимательный персонал, который
                                |был всегда готов помочь нам в любых вопросах. Обязательно приедем ещё!
                .col-3
                    .card.rotate(style="background: #F5F3F1")              
                        .card__header
                            .card__user_photo
                                img(src="../assets/images/user_photo2.jpg")
                            .card__user_container
                                .card__user_name Сергей Карпов
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                        .card__body
                            p.card__text(style="color: black") Загородный клуб обладает отличной инфраструктурой как для активного отдыха, так и для релакса. Мы попро-бовали множество развлечений, дети особенно оценили верёвочный парк, 
                                |их было не вытащить оттуда
                .col-3
                    .card.rotate         
                        .card__header
                            .card__user_photo
                                img(src="../assets/images/user_photo3.jpg")
                            .card__user_container
                                .card__user_name Виктория Минаева
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                                span
                                    img.card__rating(src="../assets/images/star.svg")
                        .card__body
                            p.card__text Мы провели незабываемое время 
                                |в Строгановских просторах. В домике было все необходимое для комфорт-ного проживания, мы наслаждались прекрасным видом и уединением 
                                |с природой.
                .col-3
                    .card(style="background: #F5F3F1;")               
                        .card__header
                            .card__user_photo-form
                                label(class="input-file")
                                    input(type="file" name="file" @change="handleFileUpload")
                                    span(:style="[feedback.userPhoto ? {'background-image': 'url(' + previewFilePath + ')', 'background-size': 'cover'} :'']")
                            .card__user_container
                                .card__user_name 
                                    input.card__input_user_name(v-if="!isCreateFeedBack" placeholder="ФИО" v-model="feedback.userName")
                                    .card__user_name(v-else) {{ feedback.userName }}
                                star-rating(:star-size="13" :animate="true" :show-rating="false" @update:rating ="setRating")
                        .card__body(:class="{card_form : !isCreateFeedBack}")
                            textarea.card__input(v-if="!isCreateFeedBack" placeholder="Введите текст..." rows="4" v-model="feedback.text")
                            p.card__text(v-else style="color: black") {{ feedback.text }}
                            button.card_button(v-if="!isCreateFeedBack" @click="validateFeedBack") оставить отзыв
            .container_map
                img(src="../assets/images/map.jpg")
                .container_map_info
                    .info_header как добраться
                    .container_adress 
                        .adress__header Адрес
                        .adress__text п. Ильинский, с. Дмитриевское
                    .container_attention 
                        .attention__header Внимание!
                        .attention__text в связи с ремонтными работами путь 
                            |к нашей базе теперь пролегает через село Мироны.
                    .info__button построить маршрут
    section.faq__section
        .container
            .section_header FAQ - часто задаваемые вопросы
            .row.container_questions
                .col-4 
                    .faq__questions Во сколько заселение и выезд? 
                    .faq__reply Расчетные часы: <br>
                        |Время заезда: с 15:00 ; Время выезда: до 13:00*
                        |*Независимо от фактического времени прибытия 
                        |на базу отдыха. О возможности продления времени прибывания в доме необходимо уточнять накануне заезда.
                .col-4 
                    .faq__questions Можно ли арендовать весь загородный клуб?
                    .faq__reply Да, в нашем загородном клубе предусмотрена аренда всей территории. Для более подробной информации 
                        |о доступности и стоимости аренды, пожалуйста, свяжитесь с нашим менеджером через форму ниже.
                .col-4 
                    .faq__questions Можно ли со своим питомцем?
                    .faq__reply У нас разрешено проживать со своим питомцем, 
                        |однако существуют некоторые ограничения по размеру, породе или числу питомцев, а также важно наличие прививочных сертификатов и соблюдение правил поведения.
    section.contact__section 
        .container 
            .section_header контакты
            .row.contact__container
                .col-6 
                    .col-10 Если у вас остались вопросы, вы можете задать их менеджеру 
                        |<br>в этой форме, или связаться с ним по следующим номерам телефона 
                    .container__phone 
                        a.contact__phone(href="tel:+79026439294") 8-902-64-39-294
                        a.contact__phone(href="tel:+73422880089") 8-(342) 288-00-89
                    .col-12(style="margin-bottom: 18px") Также вы можете найти нас в соцсетях
                    .container__social_network
                        .social_network__name Телеграмм-канал:
                        a.social_network__link(href="https://t.me/stroganovskie_prostory" target="_blank") t.me/stroganovskie_prostory
                    .container__social_network
                        .social_network__name Вконтакте:
                        a.social_network__link(href="https://vk.com/stroganovskie_prostory" target="_blank") vk.com/stroganovskie_prostory
                .col-6 
                    .contact__form 
                        .form__label Задать вопрос менеджеру
                        input.form__input(placeholder="Напишите что-нибудь" type="text" style="margin-bottom: 37px")
                        .form__label Номер телефона или адрес электронной почты, куда направить ответ:
                        input.form__input(placeholder="Email или телефон" type="email" style="margin-bottom: 30px")
                        button.contact__button отправить 
    footer.footer
        .container
            .row(style="padding-top:32px") 
                .col-2
                    ul.footer__item
                        li.footer__item_bold размещение и проживание 
                        li дома 
                        li активный отдых и услуги 
                        li главная страница 
                .col-2
                    ul.footer__item
                        li.footer__item_bold расчётные часы
                        li время заезда: с 15:00  
                        li время выезда: до 13:00                        
                .col-2
                    ul.footer__item
                        li.footer__item_bold адрес
                        li.footer__item_line-height Пермский край, Ильинский район, п. Ильинский, с. Дмитриевское                         
                .col-2
                    ul.footer__item
                        li.footer__item_bold контакты
                        li +7 (902) 643-92-94 
                        li +7 (342) 288-00-89 
                        li stroganovprostor@gmail.com                
                .col-2
                    ul.footer__item
                        li.footer__item_bold правовые документы
                        li.footer__item_line-height Согласие на обработку персональных данных  
                        li Политика конфиденциальности
                .col-2.d-flex.justify-content-end                    
                    ul.footer__item
                        li.footer__item_bold мы в соцсетях
                        li
                            .d-flex.gap-2
                                a(href="https://vk.com/stroganovskie_prostory" target="_blank")
                                    img.footer__link(src="../assets/images/icon-vk.svg")                        
                                a(href="https://t.me/stroganovskie_prostory" target="_blank")
                                    img.footer__link(src="../assets/images/icon-telegram.svg")                        
            .d-flex.justify-content-between.pb-3(style="margin-top: 50px")
                div 2023 @ СТРОГАНОВСКИЕ ПРОСТОРЫ
                div Пермь. Официальный сайт.
    Transition(name="modalBottom")
        div.modal-mask(v-show="showModalHouse" :class="{active : showModalHouse}")  
            house-detail(:house="selectedHouse" @modalClose="showModalHouse = false")

</template>

<script>
import { ref, onMounted, watch, computed } from "vue"
import { Calendar, DatePicker } from 'v-calendar';
import 'v-calendar/style.css';
import StarRating from 'vue-star-rating'

import houseList from '../components/houseList'
import houseDetail from "../components/houseDetail.vue";

export default {
    
    name: 'main-page',
    components: {
        Calendar,
        DatePicker,
        StarRating,
        houseDetail
    },
    setup() {
        const photoList = [
            'src/assets/images/main-page-winter.png',
            'src/assets/images/main-page-winter2-source.png',
            'src/assets/images/main-page-winter3-source.png',
        ]
        let datePicker = ref({
            dateStart:false,
            dateEnd:false
        })
        let distance = ref(0)
        let showHeader = ref(false)
        const fil = () => {
            const el = document.getElementById('aboutUs')
            distance.value = el.offsetTop - window.scrollY
            if (distance.value <= 300) {
                showHeader.value = true
            }
            else {
                showHeader.value = false
            }
        }
        const au = ref(null)        
        const selectedColor = ref('green')
        const masks = ref({
            modelValue: 'DD.MM.YYYY',
        })                

        const inc = () => {
            filter.value.personQuantity += 1
        }
        const dec = () => {
            filter.value.personQuantity > 0 ? filter.value.personQuantity -= 1 : filter.value.personQuantity = 0
        }
        let filter = ref({
            dateStart:'',
            dateEnd:'',
            isHouse:false,
            isGlamping:false,
            personQuantity:0
        })
        let selPhoto = ref(0)
        let timerId                
        const incSelPhoto = () => {
            if (selPhoto.value < 2 - 1){
                selPhoto.value += 1
            }
            else {
                selPhoto.value = 0
            }
        }                
        const sliderPhoto = () => {
            incSelPhoto()
            timerId = setTimeout(sliderPhoto, 5000)
        }
        let feedback = ref({
            userName:'',
            userPhoto:null,
            text:'',
            rating: 0
        })
        const handleFileUpload = (event) => {
            const file = event.target.files[0]   
            feedback.value.userPhoto = file
        }
        const previewFilePath = computed(() => {            
            let URL = window.URL || window.webkitURL
            if(feedback.value.userPhoto){
                return URL.createObjectURL(feedback.value.userPhoto)
            }
            else{
                return '#'
            }
        })
        let isCreateFeedBack = ref(false)
        const setRating = (rating) => {
            feedback.value.rating = rating
        }
        const validateFeedBack = () => {            
            if (feedback.value.userName && feedback.value.text && feedback.value.rating){
                isCreateFeedBack.value = true
            }
        }
        let selectedHouse = ref({})        
        let showModalHouse = ref(false)
        watch(()=>filter.value.dateStart,()=>{
            datePicker.value.dateStart = false
        })
        watch(()=>filter.value.dateEnd,()=>{
            datePicker.value.dateEnd = false
        })
        onMounted(() => {
            window.addEventListener('scroll', (event) => { fil() });
            setTimeout(sliderPhoto, 5000)
        })
        return {
            photoList,
            au,
            distance,
            showHeader,
            datePicker,            
            masks,
            selectedColor,            
            inc,
            dec,
            filter,
            selPhoto,
            handleFileUpload,
            previewFilePath,
            feedback,
            isCreateFeedBack,
            validateFeedBack,
            setRating,
            houseList,
            selectedHouse,
            showModalHouse
        }
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
.modalBottom-enter-active {
  animation: animatebottom 1s;
}
.modalBottom-leave-active {
  animation: animatebottom 1s reverse;
}
.modal-mask{
    position: fixed;    
    top: 0;
    height: 100vh;
    width: 100%;
    background-color: #ECE8E3;
    z-index: 200;    
}
@keyframes animatebottom {
  from {
    top: 100%;
    opacity: 0;
  }

  to {
    top: 0%;
    opacity: 1;
  }
}
.btn_house_detail{
    position: absolute;
    bottom: 11px;
    right: 11px;
    height: 36px;
    width: 36px;
    border-radius: 30px;
    background-color: #005D4B;
    background-image: url("../assets/images/house_detail.svg");
    background-repeat: no-repeat;
    background-position: 12px 10px;
    &:hover{
        cursor: pointer;
    }
}

.date_picker_wrapper{
  position: absolute;
  top: 59px;
  width: 289px;
  z-index: 100;
}
.input_number__in{
    border: none;
    width: 91px;
    text-align: center;
    color: #B3B3B3;
}
.input_number__in.active{
    color: #003731;
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
.input_number_wrapper.active{
    border: 1px #003B30 solid;
}
.checkbox__label{
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
    padding-left: 6px;
}
.checkbox__label.active{
    color: #005D4B;
}
.checkbox-wrapper{
    display: flex;
    width: 100%;
    align-items: center;
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

.vc-container{
    display: block !important;
    margin: 0 auto;
}

a.header__nav__link {
    text-decoration: none;
    color: #fff;
    opacity: .8;
    &:hover{
        opacity: 1;
    }    
    &:hover:after{
        transform: scaleX(1);      
    }
}

a.header__nav__link:after{
    display:block;
    content: '';
    border-bottom: solid 1px #fff;  
    transform: scaleX(0);  
    transition: transform 250ms ease-in-out;
}

.card__user_photo-form{
    display: flex;
    margin-left: 13px;
    height: 46px;
    width: 46px;
    border-radius: 25px;
    background-color: #bdbdbd;
}
.card__user_photo-form img{
    width: 22px;
    display: block;
    margin: 0 auto;
}

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

.container_footer{
    display: flex;
    width: 373px;
    margin-left: 14px;
    margin-top: 36px;
    align-items: flex-end;
    justify-content: space-between;
}

.footer_text{
    display: flex;
    color: #003731;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300;
    line-height: 20.33px;
    width: 215px;
    height: 60px;
}

.footer_button{
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
}
.container_info-graph{
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
.wrapper_cost_capacity{
    display: flex;
}

.house_cost{
    font-weight: 300;
    margin-right: 38px;
}
.house_capacity{
    font-weight: 300;
    display: flex;
    align-items: center;
}
.house_capacity__icon{
    display: flex;
    margin-right: 9px;    
}
.wrapper_img{
    border-radius: 30px;
    width: 400px;
    height: 248px;    
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    position: relative;
}

.placement__cantainer_card{
    margin-top: 48px;
}
.placement__card{    
    height: 399px;
    width: 400px;
    background: #ECE8E3;
    border-radius: 30px;  
    margin-bottom: 40px;  
}
.placement__form__button_search{
    width: 180px;
    margin-left: 26px;
    color: #005D4B;
    font-size: 17px;
    font-family: Lato;
    font-weight: normal;
    border: 1px #005D4B solid;
    border-radius: 55px;
    background-color: #fff;
}
.checkbox__header{
    font-family: 'Montserrat';
    font-size: 17px;
    color: #bdbdbd;
    margin-top: -12px;
    margin-bottom: 11px;
}
.checkbox_container{
    width: 250px;
    margin-left: 40px;
}
.quantity_guests{
    position: relative;
    width: 151px;
}
.quantity_guests__text::before{
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
.quantity_guests__text.active::before{
    color: #003B30;
}
.quantity_guests__input{
    border-radius: 10px; 
    border: 1px #A4A4A4 solid;
    height: 57px;
    max-width: 151px;
}
input:focus-visible{
    outline: 2px #005D4B solid;
}
.date_time__input{
    border-radius: 10px; 
    border: 1px #A4A4A4 solid;
    width: 289px;
    height: 57px;
    color: #003731;
}
.date_time{
    position: relative;
}
.date_time__icon::before{
    content: url(../assets/images/calendar.svg);
    color: #bdbdbd;
    position: absolute;
    display: flex;
    align-items: center;
    top: 0;
    bottom: 0;
    left: 260px;    
    
}
.date_time__text::after{
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
.date_time_end__text::after{
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
.about_as__container_row{
    margin-bottom: 32px;
}
.header_sticky__nav_link{
    text-decoration: none;
    color: black;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 300;
    &:after{
        display:block;
        content: '';
        border-bottom: solid 1px black;  
        transform: scaleX(0);  
        transition: transform 250ms ease-in-out;
    }
    &:hover:after{
        transform: scaleX(1);  
    }
    
}
.header_sticky__nav{
    display: flex;
    gap: 11px;
    font-family: 'Lato';
    font-weight: 300;
    font-size: 17px;
    color: black;   
    margin-bottom: 0; 
}
.header_sticky__container{
    display: flex;
    justify-content: space-between;
    align-items: center;    
}
.header_sticky__icon_feed_back{
    display: flex;
    justify-content: flex-end;
    padding-right: 20px;
}
.header_sticky__icon_feed_back img {
    margin-right: 8px;
}
.header_sticky__icon_feed_back button {
    background-color: rgba(0, 93, 75, 1);
    color: #fff;
    border: 0px;
    border-radius: 35px;
}
.about_us__card__img{
    height: 75px;
    margin-bottom: 13px;
}
.about_us__card__header{
    font-family: 'Lato';
    font-size: 17px;
    color: #003731;
    margin-bottom: 10px;
}
.about_us__card__text{
    font-family: 'Lato';
    font-weight: 300;
    font-size: 15px;
    color: black;
}
.container_icon{
    gap: 23px;
}
.first_page__arrow_icon{
    width: 33px;
}
.first_page__h2{
    font-family: 'Lato';
    font-size: 17px;
    color: #fff;
    line-height: 23px;
}
.first_page__h1 {
    font-family: 'Apoc Normal';
    font-weight: 400;
    font-size: 30px;
    color: #fff;
    line-height: 35px;
    letter-spacing: 2px;
}

.header__nav__button {
    background-color: transparent;
    border: 1px solid #fff;
    color: #fff;
    border-radius: 35px;
    transition: background-color 0.4s ease-in-out, border 250ms ease-in-out;
    
    &:hover{
        background-color: #003731;
        border: 1px solid transparent
    }
}

.header_sticky {
    transform: translateY(-160px);
    transition-duration: 1s;
    transition-property: all;
    opacity: 0;      
    position: fixed;
    width: 100%;
    top: 0;
}

.header_sticky.active {     
    position: fixed;
    background-color: #fff;
    padding-top: 20px;
    padding-bottom: 20px;
    top: 0;   
    opacity: 1;
    z-index: 150;
    transform: translateY(0px); 
}

.overlay {
    background-color: rgb(0, 0, 0, 0.6);
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 10;
}

.container__header {
    position: relative;
    z-index: 100;
}

.container__first_page {
    height: 100vh;
    width: 100%;
    position: relative;
}

img.photo {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    transition: opacity .8s ease-in-out;
}

img.photo.active{
    opacity: 1;
}

.header {
    padding-top: 42px;
    margin-bottom: 384px;
}

.header__nav {    
    color: #fff;    
    gap: 15px;
}

.header__nav__link {
    font-family: 'Lato';
    font-size: 17px;
}

.background_image {
    /* background-image: url(../assets/images/main-page.png); */
    background-repeat: no-repeat;
    background-size: cover;
    height: 100vh;
}

.about_us__header {
    font-family: 'Apoc Normal';
    font-weight: 300;
    font-size: 47px;
    line-height: 49px;
    color: #003731;    
    margin-bottom: 69px;
}
.about_us{
    background-color: #ECE8E380;
    padding-top: 94px;
    padding-bottom: 93px;
}
.container {
    padding: 0;
}

.service_section{
    background-color: #ECE8E380;
    padding-top: 84px;
}

.service__header{
    font-family: 'Apoc Normal';
    font-weight: 300;
    font-size: 47px;
    line-height: 49px;
    color: #003731;    
    margin-bottom: 60px;
}
.service__name_typ{
    font-family: 'Lato';
    font-size: 17px;
    font-weight: 400;
}

.service__item{
    display: flex;
    justify-content: space-between;
    font-family: 'Lato';
    font-size: 15px;
    font-weight: 300;
    border-bottom: 1px #005D4B solid;
    padding-bottom: 13px;
}
.service__item:not(:first-child){
    margin-top: 14px;
}

.section_header{
    font-family: 'Apoc Normal';
    font-weight: 300;
    font-size: 47px;
    line-height: 49px;
    color: #003731;    
    margin-bottom: 60px;
}

.feedback_section .section_header {
    margin-top: 86px;
}

.card{
    background: #005D4B; 
    border-radius: 30px;
    height: 233px;    
}

.card__header{
    background: white; 
    border-radius: 19px;
    height: 60px;
    width: 268px;
    margin-top: 11px;
    margin-left: 11px;
    display: flex;
    align-items: center;
}

.card__user_photo{
    display: flex;
    margin-left: 13px;
}

.card__user_name{
    color: black;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;    
}

.card__user_container{
    margin-left: 13px;
}

img.card__rating{
    height: 11px;    
}

img.card__rating:not(:last-child){
    margin-right: 2px;
}

.card__text{
    color: white;
    font-size: 15px;
    font-family: Lato;
    font-weight: 300;
}

.card__body{
    margin-top: 9px;
    margin-left: 14px;
}

.card.rotate:hover{
    transform: rotate(10deg);
}
.card_form{
    border-radius: 30px;
    height: 233px;    
}
.card__input_user_name{
    border: 0px;
}
input.card__input_user_name:focus-visible{
    outline: 0px;
}
.container_map{
    margin-top: 183px;
    width: 840px;
    display: flex;
    justify-content: center;
    gap: 41px;
    margin-bottom: 183px;
}

.info_header{
    font-family: 'Apoc Normal';
    font-weight: 300;
    font-size: 47px;
}

.container_adress{
    margin-top: 57px;
}

.adress__header,
.attention__header{
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400; 
}

.adress__text,
.attention__text{
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300; 
}

.container_attention{
    margin-top: 36px;
}

.info__button{
    width: 220px;
    border: 1px #005D4B solid;
    border-radius: 35px;
    background: transparent;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400; 
    color: #005D4B;
    padding: 12px 30px;
    margin-top: 43px;
}

.container_questions{
    margin-top: 61px;
    margin-bottom: 179px;
}

.faq__questions{
    background: #F5F3F1;
    border-radius: 30px;
    display: flex;
    justify-content: center;
    padding: 29px 0px;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400; 
}

.faq__reply{
    background: #005D4B;
    border-radius: 30px;
    padding: 0px 19px;
    color: white;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300; 
    height: 170px;
    display: flex;
    align-items: center;
}

.contact__container{
    margin-top: 51px;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300; 
    margin-bottom: 94px;
}

.container__phone{
    display: flex;
    gap: 27px;    
    margin-top: 18px;
    margin-bottom: 22px;
}

a.contact__phone{
    text-decoration: none;
    color: #005D4B;
    border-bottom: 1px #005D4B solid;
}

.container__social_network{
    display: flex;
}

.social_network__name{
    margin-right: 3px;
}

.social_network__link{
    color: #005D4B;
    text-decoration: none;
}

.contact__form{
    background: #F5F3F1;
    border-radius: 30px;
    width: 620px;
    height: 328px;
    padding: 24px 14px;
}

.form__label{
    margin-bottom: 10px;
}

.form__input{
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 594px;
    height: 57px;    
}
.card__input{
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 268px;        
}

textarea.card__input::placeholder{
    padding-left: 10px;
    color: #919191;
    font-size: 15px;
    font-family: Lato;
    font-weight: 300;
}
.card_button{
    display: flex;
    color: black;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;        
    background-color: #fff;
    border-radius: 19px;
    width: 149px;
    height: 35px;
    align-items: center;
    border: none;
    justify-content: center;
}

.card__body.card_form{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-right: 14px;
    gap: 10px;

}

input.form__input::placeholder{
    padding-left: 19px;
    color: #CCCCCC;
    font-size: 15px;
    font-family: Lato;
    font-weight: 300;
}

button.contact__button{
    display: block;
    margin-left: auto;
    width: 196px;
    height: 47px;
    background-color: inherit;
    border-radius: 30px;
    border: 1px #005D4B solid;
    color: #005D4B;
}

footer.footer{
    background-color: #F5F3F1;   
    color: rgba(0, 0, 0, 0.40);
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 300; 
}

.footer_container{
    display: flex;
    justify-content: space-between;
    padding-top: 182px;
    padding-bottom: 20px;
}
ul.footer__item{
    font-size: 13px;    
}
ul.footer__item li {
    margin-top: 6px;    
}
li.footer__item_line-height{
    line-height: 23px;
}
.footer__item_bold{
    font-weight: 400;
}
.footer__link:hover{
    cursor: pointer;
}
</style>