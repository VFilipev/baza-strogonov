<template lang="pug">
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
</template>

<script>
export default {
    name: 'footer-component',
    setup() {


        return {}
    }
}
</script>

<style></style>