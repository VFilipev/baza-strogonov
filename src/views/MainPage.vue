<template lang="pug"> 
div     
    header-sticky
    section.first_page        
        .first_page__wrapper
            .overlay
            template(v-for="(photo, index) in photoList" ) 
                img.photo(:src="photo" :class="{ active : index == selPhoto }")                
            .first_page__header
                .container
                    div(style="padding-top: 42px;margin-bottom: 384px;")
                        .row.align-items-center
                            .logo.col-5
                                img(src="../assets/images/logo.png")
                            .header__nav.d-flex.col-3.offset-2
                                router-link(to="/house", tag="a", class="header__nav__link") дома
                                router-link(to="/uslugi", tag="a", class="header__nav__link") активный отдых / услуги
                            .header__nav.d-flex.col-2     
                                a(@click="toRefContact" style="cursor:pointer")                       
                                    img(src='../assets/images/telefon.svg')
                                button.header__nav__button 
                                    a(@click="toRefBooking") забронировать
                    .row.d-flex.justify-content-between
                        .first_page__h1.col-4 уютные коттеджи 
                            |и глемпинг хвойном лесу
                            |на берегу камского моря
                        .first_page__h2.col-4 Уединеный отдых в уютном историческом месте Пермского края. 
                            |Насладитесь первозданой природой и европейским уровнем комфорта размещения в уютных коттеджах и номерах. 
                            |Зарядитесь эмоциямиот прогулки на квадроциклах, а после отдахните душой и телом в традиционной русской бане.                                     
    section.about_us(id="aboutUs")
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
                    .about_us__wrapper_img                     
    section.placement(id="booking")
        .container           
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
    section.service_section
        .container         
            .row.service     
                .service__header.col-2 услуги
            .row(style="padding-bottom: 94px") 
                .col-6
                    p.service__name_typ Активный отдых                    
                    .service__item(v-for="item in recreation")
                        .service__name {{ item.name }}
                        .service__cost {{ item.cost }}                    
                .col-6
                    p Банные процедуры
                    .service__item(v-for="item in bathProcedures") 
                        .service__name {{ item.name }}
                        .service__cost {{ item.cost }}                              
    section.feedback_section(style="height: 1080px")
        .container
            .section_header ваши отзывы
            .row 
                .col-3(v-for="(comment, index) in commentList")
                    .card.rotate(:class="{ 'feedback_card_background' : isEval(index + 1)}")
                        .card__header
                            .card__user_photo
                                img(:src="comment.img")
                            .card__user_container
                                .card__user_name {{ comment.user_name }}
                                star-rating(:star-size="13" :readOnly="true" :rating="comment.rating" :show-rating="false")                                
                        .card__body
                            p.card__text(:class="{'text_black' : isEval(index + 1)}") {{ comment.text }}
                .col-3
                    .card(style="background: #F5F3F1;")               
                        .card__header
                            .card__user_photo-form
                                label(class="input-file")
                                    input(type="file" name="file" @change="handleFileUpload" id="user_img" ref="user_img")
                                    span(:style="[feedback.userPhoto ? {'background-image': 'url(' + previewFilePath + ')', 'background-size': 'cover'} :'']")
                            .card__user_container
                                .card__user_name 
                                    input.card__input_user_name(v-if="!isCreateFeedBack" placeholder="ФИО" v-model="feedback.userName" name="user_name")
                                    .card__user_name(v-else) {{ feedback.userName }}
                                star-rating(:star-size="13" :animate="true" :show-rating="false" @update:rating ="setRating")
                        .card__body(:class="{card_form : !isCreateFeedBack}")
                            textarea.card__input(v-if="!isCreateFeedBack" placeholder="Введите текст..." rows="4" v-model="feedback.text"
                            name="card_text")
                            p.card__text(v-else style="color: black") {{ feedback.text }}
                            button.card_button(v-if="!isCreateFeedBack" @click="saveFeedBack") оставить отзыв
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
                    button.info__button 
                        a(href="https://yandex.ru/maps/-/CDq0rB9Q" target="_blank") построить маршрут
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
    section.contact__section(id="contact") 
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
                        input.form__input(placeholder="Напишите что-нибудь" type="text" style="margin-bottom: 37px" name="contact_form")
                        .form__label Номер телефона или адрес электронной почты, куда направить ответ:
                        input.form__input(placeholder="Email или телефон" type="email" style="margin-bottom: 30px" name="contact_form")
                        button.contact__button отправить 
    footerComponent
    Transition(name="modalBottom")
        div.modal-mask(v-show="isShowModalHouse" :class="{active : isShowModalHouse}")  
            house-detail(:house="selectedHouse" @modalClose="closeModal")

</template>

<script>
import { ref, onMounted, watch, computed, onUnmounted } from "vue"
import { Calendar, DatePicker } from 'v-calendar';
import { formatNumber } from '../components/formatNumber'

import headerSticky from "../components/headerSticky.vue";

import 'v-calendar/style.css';
import StarRating from 'vue-star-rating'

import houseDetail from "../components/houseDetail.vue";
import footerComponent from "../components/footerComponent.vue";
import { useRouter } from 'vue-router'
import { useOrderStore } from "../stores/orderStore";

import { Lodge, Comment } from '../api'
import { recreation, bathProcedures } from "../components/serviceList";
import moment from "moment";
export default {

    name: 'main-page',
    components: {
        Calendar,
        DatePicker,
        StarRating,
        houseDetail,
        headerSticky,
        footerComponent
    },
    setup() {        
        const orderStore = useOrderStore()
        const router = useRouter()

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
        const photoList = [
            '/static/main-page-winter.png',
            '/static/main-page-winter2-source.png',
            '/static/main-page-winter3-source.png',
        ]
        let datePicker = ref({
            dateStart: false,
            dateEnd: false
        })
        let isScroll = ref(false)
        let distance = ref(0)
        let showHeader = ref(false)
        const fil = () => {
            if (isScroll.value == true) {
                const el = document.getElementById('aboutUs')
                distance.value = el.offsetTop - window.scrollY
                if (distance.value <= 300) {
                    showHeader.value = true
                }
                else {
                    showHeader.value = false
                }
            }
        }
        const selectedColor = ref('green')
        const masks = ref({
            modelValue: 'DD.MM.YYYY',
            L: 'DD.MM.YYYY'
        })

        const inc = () => {
            filter.value.personQuantity += 1
        }
        const dec = () => {
            filter.value.personQuantity > 0 ? filter.value.personQuantity -= 1 : filter.value.personQuantity = 0
        }
        let filter = ref({
            dateStart: '',
            dateEnd: '',
            isHouse: false,
            isGlamping: false,
            personQuantity: 0
        })
        let selPhoto = ref(0)
        let timerId
        const incSelPhoto = () => {
            if (selPhoto.value < 2 - 1) {
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
            userName: '',
            userPhoto: null,
            text: '',
            rating: 0
        })
        const handleFileUpload = (event) => {
            const file = event.target.files[0]
            feedback.value.userPhoto = file
        }
        const previewFilePath = computed(() => {
            let URL = window.URL || window.webkitURL
            if (feedback.value.userPhoto) {
                return URL.createObjectURL(feedback.value.userPhoto)
            }
            else {
                return '#'
            }
        })
        let isCreateFeedBack = ref(false)
        const setRating = (rating) => {
            feedback.value.rating = rating
        }
        const validateFeedBack = () => {
            if (feedback.value.userName && feedback.value.text && feedback.value.rating) {
                isCreateFeedBack.value = true
            }else{
                return false
            }
            
        }
        const saveFeedBack = async() => {
            validateFeedBack()
            if(feedback.value.userPhoto){
                let formData = new FormData();
                formData.append('user_name', feedback.value.userName)
                formData.append('rating', feedback.value.rating)
                formData.append('img', feedback.value.userPhoto)
                formData.append('text', feedback.value.text)
                await Comment.save(formData)
            }else{
                let tmp = {}
                tmp.user_name = feedback.value.userName
                tmp.rating = feedback.value.rating
                tmp.text = feedback.value.text
                await Comment.save(tmp)
            }
            
            
        }
        let houseList = ref([])
        const getAvailableLodge = async () => {
            let start = moment(filter.value.dateStart).format('DD.MM.YYYY')
            let end = moment(filter.value.dateEnd).format('DD.MM.YYYY')
            let tmp = (await Lodge.get_available_house({ 'date_start': start, 'date_end': end })).data
            houseList.value = tmp
        }
        let selectedHouse = ref({})
        let isShowModalHouse = ref(false)
        const showModalHouse = (lodge) => {
            document.body.classList.add('modal-open')
            isShowModalHouse.value = true
            selectedHouse.value = lodge
        }
        const closeModal = () => {
            document.body.classList.remove('modal-open')
            isShowModalHouse.value = false
        }
        const getLodgeList = async () => {
            let tmp = (await Lodge.getList({'avalible': true})).results
            houseList.value = tmp
        }
        const commentList = ref([])
        const getComment = async() => {
            commentList.value = (await Comment.getList({'avalible': true})).results
        }
        const isEval = (index) => {
            if (index % 2 == 0) {
                console.log(index % 2 == 0);
                return true
            }
        }
        const toRefBooking = () => {
            const el = document.getElementById('booking')
            el.scrollIntoView({ behavior: 'smooth' })
        }
        const toRefContact = () => {
            const el = document.getElementById('contact')
            el.scrollIntoView({ behavior: 'smooth' })
        }
        watch(() => filter.value.dateStart, () => {
            datePicker.value.dateStart = false
        })
        watch(() => filter.value.dateEnd, () => {
            datePicker.value.dateEnd = false
        })
        onMounted(() => {
            getLodgeList()
            getComment()
            isScroll.value = true
            window.addEventListener('scroll', (event) => { fil() });
            setTimeout(sliderPhoto, 5000)
        })
        onUnmounted(() => {
            isScroll.value = false
            window.removeEventListener('scroll', (event) => { fil() });
        })
        return {
            photoList,
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
            saveFeedBack,
            setRating,
            houseList,
            selectedHouse,
            showModalHouse,
            closeModal,
            isShowModalHouse,
            getAvailableLodge,
            toBooking,
            formatNumber,  
            getComment,
            commentList,
            isEval,
            recreation,
            bathProcedures,
            toRefBooking,
            toRefContact
        }
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

section.placement:before {
  display: block;
  content: " ";
  margin-top: -100px;
  height: 100px;
  visibility: hidden;
}

p.card__text.text_black{
    color: #000;
}

.card.feedback_card_background{
    background-color: #F5F3F1;
}

.modalBottom-enter-active {
    animation: animatebottom 1s;
}

.modalBottom-leave-active {
    animation: animatebottom 1s reverse;
}

.modal-mask {
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

.btn_house_detail {
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

    &:hover {
        cursor: pointer;
    }
}

.date_picker_wrapper {
    position: absolute;
    top: 59px;
    width: 289px;
    z-index: 100;
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

.vc-container {
    display: block !important;
    margin: 0 auto;
}

a.header__nav__link {
    text-decoration: none;
    color: #fff;
    opacity: .8;

    &:hover {
        opacity: 1;
    }

    &:hover:after {
        transform: scaleX(1);
    }
}

a.header__nav__link:after {
    display: block;
    content: '';
    border-bottom: solid 1px #fff;
    transform: scaleX(0);
    transition: transform 250ms ease-in-out;
}

.card__user_photo-form {
    display: flex;
    margin-left: 13px;
    height: 46px;
    width: 46px;
    border-radius: 25px;
    background-color: #bdbdbd;
}

.card__user_photo-form img {
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

.footer_button {
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

    &:hover {
        cursor: pointer;
    }
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
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
    position: relative;
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

.placement__form__button_search {
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

.about_us__wrapper_img{
    width: 400px;
    height: 272px;
    border-radius: 30px;
    background-image: url(../assets/images/diana.jpeg);
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 0px -135px;
}

.about_as__container_row {
    margin-bottom: 32px;
}

.about_us__card__img {
    height: 75px;
    margin-bottom: 13px;
}

.about_us__card__header {
    font-family: 'Lato';
    font-size: 17px;
    color: #003731;
    margin-bottom: 10px;
}

.about_us__card__text {
    font-family: 'Lato';
    font-weight: 300;
    font-size: 15px;
    color: black;
}

.container_icon {
    gap: 23px;
}

.first_page__arrow_icon {
    width: 33px;
}

.first_page__h2 {
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

button.header__nav__button {
    background-color: transparent;
    border: 1px solid #fff;
    color: #fff;
    border-radius: 35px;
    transition: background-color 0.4s ease-in-out, border 250ms ease-in-out;
    text-decoration: none;
    &:hover {
        background-color: #003731;
        border: 1px solid transparent
    } 
}
button.header__nav__button a{
    color: #fff;
    text-decoration: none;
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

.first_page__header {
    position: relative;
    z-index: 100;
}

.first_page__wrapper {
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

img.photo.active {
    opacity: 1;
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

.about_us {
    background-color: #ECE8E380;
    padding-top: 94px;
    padding-bottom: 93px;
}

.container {
    padding: 0;
}

.service_section {
    background-color: #ECE8E380;
    padding-top: 84px;
}

.service__header {
    font-family: 'Apoc Normal';
    font-weight: 300;
    font-size: 47px;
    line-height: 49px;
    color: #003731;
    margin-bottom: 60px;
}

.service__name_typ {
    font-family: 'Lato';
    font-size: 17px;
    font-weight: 400;
}

.service__item {
    display: flex;
    justify-content: space-between;
    font-family: 'Lato';
    font-size: 15px;
    font-weight: 300;
    border-bottom: 1px #005D4B solid;
    padding-bottom: 13px;
}

.service__item:not(:first-child) {
    margin-top: 14px;
}

.section_header {
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

.card {
    background: #005D4B;
    border-radius: 30px;
    height: 233px;
}

.card__header {
    background: white;
    border-radius: 19px;
    height: 60px;
    width: 268px;
    margin-top: 11px;
    margin-left: 11px;
    display: flex;
    align-items: center;
}

.card__user_photo {
    display: flex;
    margin-left: 13px;
}

.card__user_name {
    color: black;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
}

.card__user_container {
    margin-left: 13px;
}

img.card__rating {
    height: 11px;
}

img.card__rating:not(:last-child) {
    margin-right: 2px;
}

.card__text {
    color: white;
    font-size: 15px;
    font-family: Lato;
    font-weight: 300;
}

.card__body {
    margin-top: 9px;
    margin-left: 14px;
}

.card.rotate:hover {
    transform: rotate(10deg);
}

.card_form {
    border-radius: 30px;
    height: 233px;
}

.card__input_user_name {
    border: 0px;
}

input.card__input_user_name:focus-visible {
    outline: 0px;
}

.container_map {
    margin-top: 183px;
    width: 840px;
    display: flex;
    justify-content: center;
    gap: 41px;
    margin-bottom: 183px;
}

.info_header {
    font-family: 'Apoc Normal';
    font-weight: 300;
    font-size: 47px;
}

.container_adress {
    margin-top: 57px;
}

.adress__header,
.attention__header {
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
}

.adress__text,
.attention__text {
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300;
}

.container_attention {
    margin-top: 36px;
}

button.info__button {
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
    cursor: default;
}
button.info__button a{
    text-decoration: none;
    color: #005D4B;
}
.container_questions {
    margin-top: 61px;
    margin-bottom: 179px;
}

.faq__questions {
    background: #F5F3F1;
    border-radius: 30px;
    display: flex;
    justify-content: center;
    padding: 29px 0px;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 400;
}

.faq__reply {
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

.contact__container {
    margin-top: 51px;
    font-size: 15px;
    font-family: 'Lato';
    font-weight: 300;
    margin-bottom: 94px;
}

.container__phone {
    display: flex;
    gap: 27px;
    margin-top: 18px;
    margin-bottom: 22px;
}

a.contact__phone {
    text-decoration: none;
    color: #005D4B;
    border-bottom: 1px #005D4B solid;
}

.container__social_network {
    display: flex;
}

.social_network__name {
    margin-right: 3px;
}

.social_network__link {
    color: #005D4B;
    text-decoration: none;
}

.contact__form {
    background: #F5F3F1;
    border-radius: 30px;
    width: 620px;
    height: 328px;
    padding: 24px 14px;
}

.form__label {
    margin-bottom: 10px;
}

.form__input {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 594px;
    height: 57px;
}

.card__input {
    border-radius: 10px;
    border: 1px #A4A4A4 solid;
    width: 268px;
}

textarea.card__input::placeholder {
    padding-left: 10px;
    color: #919191;
    font-size: 15px;
    font-family: Lato;
    font-weight: 300;
}

.card_button {
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

.card__body.card_form {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-right: 14px;
    gap: 10px;

}

input.form__input::placeholder {
    padding-left: 19px;
    color: #CCCCCC;
    font-size: 15px;
    font-family: Lato;
    font-weight: 300;
}

button.contact__button {
    display: block;
    margin-left: auto;
    width: 196px;
    height: 47px;
    background-color: inherit;
    border-radius: 30px;
    border: 1px #005D4B solid;
    color: #005D4B;
}

footer.footer {
    background-color: #F5F3F1;
    color: rgba(0, 0, 0, 0.40);
    font-size: 20px;
    font-family: 'Lato';
    font-weight: 300;
}

.footer_container {
    display: flex;
    justify-content: space-between;
    padding-top: 182px;
    padding-bottom: 20px;
}

ul.footer__item {
    font-size: 13px;
}

ul.footer__item li {
    margin-top: 6px;
}

li.footer__item_line-height {
    line-height: 23px;
}

.footer__item_bold {
    font-weight: 400;
}

.footer__link:hover {
    cursor: pointer;
}
</style>