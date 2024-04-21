<template lang="pug">
transition(name="modal" )
    .modal-mask(aria-hidden="true" )
        .modal-wrapper(ref="modal" @click="$emit('input',false)"  role="dialog"  aria-hidden="true" @keydown.esc="$emit('input',false)" tabindex='-1')
        .modal-container(@click.stop="" role="document" @keydown.esc="$emit('input',false)")
                .modal-header
                    div(class="modal-header-slot")
                        div Карточка заказа №{{value.number}}
                    div(class="modal-header-close-btn")
                        button(class="btn btn-primary float-right btn-close" @click="$emit('close',false)") 

                
                .modal-container-fil.d-flex.justify-content-between.row(style="padding-left: 15px")
                    .modal-body.col-sm-6
                        h5 Контактная информация 
                        div(class="form-group row")
                            label(class="col-sm-3 col-form-label") Покупатель(ФИО):
                            div(class="col-sm-8")
                                div(class="form-control-plaintext") {{ value.customer }} 
                        div(class="form-group row" v-if="value.company")
                            label(class="col-sm-3 col-form-label") Компания:
                            div(class="col-sm-8")
                                div(class="form-control-plaintext" ) {{ value.company }}
                        div(class="form-group row")
                            label(class="col-sm-3 col-form-label") Номер: 
                            div(class="col-sm-8")
                                a(class="form-control-plaintext" :href="`tel:${value.phone}`") {{ value.phone }} 
                        div(class="form-group row")
                            label(class="col-sm-3 col-form-label") Комментарий: 
                            div(class="col-sm-8")
                                div(class="form-control-plaintext") {{ value.comment ? value.comment : 'Комментариев нет' }}                        
                        div(class="form-group row")
                            label(class="col-sm-3 col-form-label") Статус заказа: 
                            div(class="col-sm-8")
                                div(class="form-control-plaintext") {{ getChoice(value.status, statusOrder) }} 
                        div(class="form-group row" v-if="value.dogovor_status")
                            label(class="col-sm-3 col-form-label") Статус договора: 
                            div(class="col-sm-8")
                                div(class="form-control-plaintext") {{ getChoice(value.dogovor_status, statusContracrList) }} 
                        div(class="form-group row" v-if="value.dogovor")
                            label(class="col-sm-3 col-form-label") Договор: 
                            div(class="col-sm-8")
                                a(class="form-control-plaintext" :href="value.dogovor" target="_blank") {{ value.dogovor ? 'Файл' : 'Файл не загружен' }} 
                        div(class="form-group row")
                            label(class="col-sm-3 col-form-label") Сумма за аренду: 
                            div(class="col-sm-8")
                                div(class="form-control-plaintext") {{ sumCost(value.order_lodge_set) + ' Руб'}}
                    .modal-body.col-sm-6
                        h5 Услуги
                        table(class=" table")
                            thead
                                tr
                                    th №
                                    th Услуга 
                                    th Кол-во 
                                    th Цена(руб)               
                                                                                                                                                
                            tbody(class="scroll" v-if="value.products")
                                template(v-for="(product, index) in value.products")
                                    tr(v-if="product")
                                        td(class="w-30px") {{ index + 1 }}
                                        td() {{ product.product.name }}
                                        td(class="w-25") {{ product.value }}
                                            
                                        td(class="w-25") {{ product.cost }}
                        div(v-for="v in value.services" class="form-group row")
                            label(for="staticEmail" class="col-sm-1 col-form-label") {{ getChoice(v.name, serviceName) + ':' }} 
                            div(class="col-sm-7")
                                div(class="form-control-plaintext") {{ 'C '+ renderDateDMY(v.start_date) +' ПО '+renderDateDMY(v.end_date) }} 
                h5 Забронированые домики
                div(class="row")
                    div(class="col-sm-6")
                        table(class="table")
                            thead
                                tr
                                    th № 
                                    th Дом 
                                    th Заезд 
                                    th Выезд
                                    th Стоимость                                                                                                                                    
                            tbody(class="scroll" v-if="value.order_lodge_set")
                                template(v-for="(lodge, index) in value.order_lodge_set")
                                    tr(v-if="lodge")
                                        td() {{ index + 1 }}
                                        td() {{ lodge.lodge.name }}
                                        td() {{ renderDateDMY(lodge.start_date) }}
                                        td() {{ renderDateDMY(lodge.end_date) }}
                                        td() {{ lodge.cost }}
                div
                    button(class="btn btn-warning" @click="$emit('editing',false)") Редактировать 
                    button(class="btn btn-danger" style="margin-left: 10px;" @click="$emit('deleteOrder',value.id)") Удалить
                .modal-footer
                    slot(name="footer") 
</template>
<script>
import moment from 'moment'
import statusContracrList from '../assets/statusContracrList'
import statusOrder from '../assets/statusOrder'
import serviceName from '../assets/serviceName'
export default {
    name:'modal-detail-vue',
    data: function () {
        return {
            statusContracrList,
            statusOrder,
            serviceName,
        }
    },
    watch:{
    },
    methods:{        
        getChoice(ch, array){                        
            let text = ''
            array.forEach(function(item) {
                if(item.status === ch){
                    text = item.name
                }
            });
            return text    
        },
        renderDateDMY(date){            
            let a =  moment(date).format('DD-MM-YYYY')            
            return a
        },
        setFocus(){
            this.$refs.modal.focus()
        },
        sumCost(list){
            return list.map(item => item.cost).reduce((prev, next) => prev + next)
        }
    },
    props:['value'],
    beforeDestroy(){
        document.body.classList.remove('modal-open')
    },
    mounted(){
        
    },
}
</script>
<style >

.modal-mask {
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    display: table;
    transition: opacity .3s ease
}

.modal-wrapper {
    display: table-cell
}

.modal-footer{
    display:block
}
.modal-header{
    
  flex-direction: row;
  justify-content:space-between;
  padding:5px;

}
.modal-header-slot{
    flex:8;
    padding:0px 15px;
}
.modal-header-btn{
    flex:2
}
.modal-header .btn{
    padding:5px !important;
}
.modal-container {
    max-width: 1600px;
    margin: 0px auto;
    padding: 10px; 
    background-color: #fff;
    border-radius: .3rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    transition: all 0.3s ease;
    /*max-height: calc(100vh - 50px);*/
    overflow:hidden;
    margin-top: 0.75rem;
}

.modal-container.modal-lg {
    max-width: 800px
}
.modal-body2
{
    max-height: calc(90vh );
    min-height: 600px;
    overflow-y: auto;
    overflow-x:hidden;
    padding:0px
}
.modal-enter-active, .modal-leave-active {
  transition: opacity .2s;
}
.modal-enter, .modal-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}
.btn-close{
background: transparent url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z'/%3e%3c/svg%3e") center/1em auto no-repeat;
box-sizing: content-box;
width: 1em;
height: 1em;
padding: .25em .25em;
color: #000;
}
</style>
