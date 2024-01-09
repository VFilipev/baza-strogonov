<template lang="pug">
.container         
    .row.service     
        .service__header.col-4.col-sm-2 услуги
    .row(style="padding-bottom: 94px") 
        .col-xs-12.mb-5.mb-sm-0.col-sm-6
            p.service__name_typ Активный отдых                    
            .service__item(v-for="item in recreation")
                .service__name {{ item.name }}
                .service__cost {{ item.cost }}                    
        .col-xs-12.col-sm-6
            p Банные процедуры
            .service__item(v-for="item in bathProcedures") 
                .service__name {{ item.name }}
                .service__cost {{ item.cost }}    
</template>

<script setup>
import { recreation, bathProcedures } from './serviceList';
</script>

<style scoped>
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
@media (max-width: 1200px) {
    .service_section {
        padding-top: 34px;
    }

    .service__header {
        font-size: 25px;
        line-height: 30px;
        margin-bottom: 14px;
    }

    .service__name_typ {
        font-size: 15px;
    }
}
</style>