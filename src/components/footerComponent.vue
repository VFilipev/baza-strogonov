<template lang="pug">
footer.footer
    .container
        .row(style="padding-top:32px") 
            .col-2.d-none.d-sm-flex
                ul.footer__item
                    li.footer__item_bold размещение и проживание 
                    li дома 
                    li активный отдых и услуги 
                    li главная страница 
            .col-2.d-none.d-sm-flex
                ul.footer__item
                    li.footer__item_bold расчётные часы
                    li время заезда: с 15:00  
                    li время выезда: до 13:00                        
            .col-4.col-sm-2
                ul.footer__item
                    li.footer__item_bold адрес
                    li.footer__item_line-height Пермский край, Ильинский район, п. Ильинский, с. Дмитриевское                         
            .col-4.col-sm-2
                ul.footer__item
                    li.footer__item_bold контакты
                    li +7 (902) 643-92-94 
                    li +7 (342) 288-00-89 
                    li stroganovprostor@gmail.com                
            .col-2.col-sm-2.d-none.d-sm-flex
                ul.footer__item
                    li.footer__item_bold правовые документы
                    li.footer__item_line-height Согласие на обработку персональных данных  
                    li Политика конфиденциальности
            .col-2.d-flex.d-sm-none
                ul.footer__item
                    li.footer__item_bold Политика конфиденциал<br>ьности
            .col-2.col-sm-2.d-flex.justify-content-sm-end                    
                ul.footer__item
                    li.footer__item_bold мы в соцсетях
                    li
                        .d-flex.gap-sm-2
                            a(href="https://vk.com/stroganovskie_prostory" target="_blank")
                                img.footer__link(src="../assets/images/icon-vk.svg" alt="Мы в социальных сетях")                        
                            a(href="https://t.me/stroganovskie_prostory" target="_blank")
                                img.footer__link(src="../assets/images/icon-telegram.svg" alt="Мы в социальных сетях")    
        .footer-bottom.d-flex.justify-content-between.pb-3
            div 2023 @ СТРОГАНОВСКИЕ ПРОСТОРЫ
            div Пермь. Официальный сайт.
</template>

<script>
export default {
    name: 'footer-component',
    setup() {


        return {}
    }
}
</script>

<style scoped>

li {
    list-style-type: none;
}

ul {
    margin-left: 0;
    padding-left: 0;
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
.footer-bottom{
    margin-top: 50px;
}
@media (max-width: 1200px) {
    ul.footer__item {
        font-size: 8px;
    }
    li.footer__item_bold{
        margin-bottom: 8px;
    }

    li.footer__item_line-height {
        line-height: 11px;
    }
    ul.footer__item li {
    margin-top: 0;
    }
    img.footer__link{
        width: 17px;
    }
    .footer-bottom{
        font-size: 8px;
        margin-top: 7px;
    }
}
</style>