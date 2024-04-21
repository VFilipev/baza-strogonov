<template lang="pug">
transition(name="modal" )
    .modal-mask(aria-hidden="true" )
        .modal-wrapper(ref="modal" @click="$emit('input',false)"  role="dialog"  aria-hidden="true" @keydown.esc="$emit('input',false)" tabindex='-1')
        .modal-container(@click.stop="" role="document" @keydown.esc="$emit('input',false)")
            .modal-header
                div(class="modal-header-slot")
                    div Новый заказ
                div(class="modal-header-close-btn")
                    button(class="btn btn-primary float-right btn-close" @click="$emit('close',false)") 
            .modal-container-fil.d-flex.justify-content-between 
                .modal-body
                    h5 Контактная информация 
                    div(class="form-group")
                        label(for="exampleInputEmail1") ФИО покупателя
                        input(type="text" v-model="order.customer" class="form-control" placeholder="ФИО")                    
                    div(class="form-group")
                        label(for="exampleInputEmail1") Номер телефона 
                        input(type="text" v-model="order.phone" class="form-control" placeholder="+7-(000)-000-00-00") 
                    div(class="form-group")
                        label(for="exampleInputEmail1") Email 
                        input(type="email" v-model="order.email" class="form-control" aria-describedby="emailHelp" placeholder="Email") 
                    div(class="form-group")
                        label(for="exampleInputEmail1") Номер заказа
                        input(v-model="order.number" type="text" class="form-control" placeholder="Номер заказа")  
                    div(class="form-group")
                        label(for="exampleInputEmail1") Статус договора
                        select(v-model="order.dogovor_status" class="form-select" name="" id="")
                            option(value="") --
                            option(v-for="status in statusContractList" :key="status.status" :value="status.status") {{status.name}}
                    h5 Детали заказа
                    div(class="form-group")
                        label(for="exampleFormControlInput1" class="form-label") День заезда 
                        input(v-model="order.orderlodge_set[0].start_date" class="form-control" type="datetime-local" name="" id="")
                    div(class="form-group")
                        label(for="exampleFormControlInput1" class="form-label") День выезда
                        input(v-model="order.orderlodge_set[0].end_date" class="form-control" type="datetime-local" name="" id="")
                    div(class="form-group")
                        label(for="exampleInputEmail1") Выберите дом
                        select(v-model="order.orderlodge_set[0].lodge" class="form-select" name="" id="")
                            option(value="") --
                            option(v-for="lodge in lodgeList" :value="lodge.id") {{lodge.name}}
                    div(class="form-group")
                        label(for="exampleFormControlInput1" class="form-label") Стоимость
                        input(v-model="order.orderlodge_set[0].cost" class="form-control" name="" id="")
                
                    button(class="btn btn-success" @click="saveOrderTest()") сохранить
                    
                .modal-body
                    h5 Выбор товаров
                    .table-outer
                        .table-iner
                            table(class="w-100")
                                thead
                                    tr
                                        th №
                                        th Товар 
                                        th Кол-во 
                                        th Цена(руб)               
                                        th(style="min-width: 32px;")                                                                                                             
                                tbody(class="scroll" v-if="productList")
                                    template(v-for="(product, index) in productList")
                                        tr()
                                            td(class="w-30px") {{ index + 1 }}
                                            td()
                                                select(v-if="product.id" v-model="product.id" class="form-select" name="" id="")
                                                    option(value="") {{ product.product ? product.product.name : '--' }}
                                                    option(v-for="product in allProductsList" :value="product.id") {{product.name}}
                                                select(v-else v-model="product.product" class="form-select" name="" id="")
                                                    option(value="") {{ product.product ? product.product.name : '--' }}
                                                    option(v-for="product in allProductsList" :value="product.id") {{product.name}}
                                            td(class="w-25")
                                                input(v-model="product.value" class="form-control" type="number" step="1") 
                                            td(class="w-25")
                                                input(v-model="product.cost" class="form-control" type="number" step="1") 
                                            td(v-if="!product.id" @click="removeItem(index)")
                                                svg(xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16")
                                                    path(d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z")
                                        //- tr(v-else)
                                        //-     td(class="w-30px") {{ index + 1 }}
                                        //-     td()
                                        //-         select(class="form-select" name="" id="")
                                        //-             option(value="") {{ service.service ? service.service.name : '--' }}
                                        //-             option(v-for="service in allServiceList" :value="service.id") {{service.name}}
                                        //-     td(class="w-25")
                                        //-         input(v-model="service.value" class="form-control" type="number" step="1") 
                                        //-     td(class="w-25")
                                        //-         input(v-model="service.cost" class="form-control" type="number" step="1") 
                                        //-     td(v-if="!service.id" @click="removeItem(index)")
                                        //-         svg(xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16")
                                        //-             path(d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z")
                    button(class="btn btn-primary" @click="addNewRow()") Добавить
                    div(class="form-check")
                        input(v-model="IsSauna" type="checkbox" class="form-check-input" id="exampleCheck1")
                        label(class="form-check-label" for="exampleCheck1") Баня                    
                    div(v-if="IsSauna" class="form-group")
                        label(for="exampleInputEmail1" style="margin-right: 10px;") С
                        input(v-model="sauna.start_date" type="datetime-local")
                        label(for="exampleInputEmail1" style="margin-right: 10px;") ДО
                        input(v-model="sauna.end_date" type="datetime-local")
                    div(class="form-check")
                        input(v-model="IsChan" type="checkbox" class="form-check-input" id="exampleCheck1")
                        label(class="form-check-label" for="exampleCheck1") Чан 
                    div(v-if="IsChan" class="form-group")
                        label(for="exampleInputEmail1" style="margin-right: 10px;") С
                        input(v-model="chan.start_date" type="datetime-local")
                        label(for="exampleInputEmail1" style="margin-right: 10px;") ДО
                        input(v-model="chan.end_date" type="datetime-local")
                        
            .modal-footer
                slot(name="footer") 
</template>
<script>

import moment from "moment";
import { Order } from "@/api";
// import { Sauna } from "@/api";


export default {
    name: 'modal-create-order',
    data: function () {
        return {
            IsSauna:false,
            IsChan:false,
            sauna:{},
            chan:{},
            saunaTime:null,
            productList: [],
            allProductsList: [],
            statusList: [
                { status: 'WT', name: 'Ожидает' },
                { status: 'DF', name: 'Подтвержден' },
                { status: 'PP', name: 'Внесена предоплата' },
                { status: 'PM', name: 'Оплачен' },
                { status: 'CP', name: 'Завершeн' },
            ],
            statusContractList: [
                { status: 'NC', name: 'Нет договоров' },
                { status: 'HC', name: 'Есть договоры' },
                { status: 'WS', name: 'Есть договоры(один без подписи)' },
                { status: 'WP', name: 'Есть договоры(один без печати)' },
                { status: 'SP', name: 'Есть два договора без печати и без подписи' },
            ],
            order: {                
                orderlodge_set: [{}],
                services_set: [],
                products_set:[]
            },
            lodgeList: []

        }
    },
    props:['orderProp'],
    watch: {
    },
    methods: {
        // async saveSauna() {        
        //     this.sauna.lodge_id = this.order.orderlodge_set[0].lodge
        //     await Sauna.objects.save(this.sauna)            
        // },
        validate(){
            
            if(!this.order.customer){
                         this.$notify({
                                group: 'foo',
                                type: 'warn',
                                title: 'Ошибка',
                                text: 'Укажите ФИО Покупателя'
                            });
                return false
            }
            if(!this.order.orderlodge_set[0].lodge){
                         this.$notify({
                                group: 'foo',
                                type: 'warn',
                                title: 'Ошибка',
                                text: 'Укажите Дом'
                            });
                return false
            }
            return true
        },
        removeItem(index){
                    this.productList.splice(index, 1)
                },
        addNewRow:function(){
                let def ={}                
                this.productList.push(def)
            },
        async getAllServices(){
            const url = "/api/uslugi/"            
            const response = await (
                await fetch(
                    url 
                )
            ).json();
            this.allProductsList = response
        },
        async getOrderProduct(id) {
            const url = "/api/product/?"
            let params = new URLSearchParams({
                order: id,                  
            })
            const response = await (
                await fetch(
                    url + params
                )
            ).json();
            this.productList = response
        },
        prerapeSave(){
            if (!this.validate()){
                return 'err'
            }
            if(this.sauna.start_date && this.sauna.end_date && this.IsSauna){
                this.sauna.name = 'SN'
                this.order.services_set.push(this.sauna)
            }
            if(this.chan.start_date && this.chan.end_date && this.IsChan){
                this.chan.name = 'CH'
                this.order.services_set.push(this.chan)
            }
            
            // else{
            //     this.order.services_set = []
            // }
        },
        // СОХРАНЕНИЕ ЗАКАЗА
        async saveOrderTest() {
            this.prerapeSave()
            this.order.products_set = this.productList
            await Order.objects.save(this.order)
            this.item = {}
            this.closeModal()
        },
        
        closeModal() {
            this.$emit('closeModal')
        },
        
        // ПОЛУЧЕНИЕ ЗАКАЗА ЕСЛИ ЕСТЬ ID
        
        async getOrder(id) {
            const url = "/api/order/?"
            let params = new URLSearchParams({
                id: id,
            })
            const response = await (
                await fetch(
                    url + params
                )
            ).json();
            this.order = response[0];
            this.order.orderlodge_set = [{}]
            this.order.orderlodge_set[0].start_date = moment(this.order.order_lodge_set[0].start_date).subtract(2, 'hours').format('yyyy-MM-DDTHH:mm')
            this.order.orderlodge_set[0].end_date = moment(this.order.order_lodge_set[0].end_date).subtract(2, 'hours').format('yyyy-MM-DDTHH:mm')
            this.order.orderlodge_set[0].lodge = this.order.order_lodge_set[0].lodge.id
            this.order.orderlodge_set[0].cost = this.order.order_lodge_set[0].cost
            if(this.order.services){
                this.IsSauna = true
            }
            if(this.order.services[1]){
                this.IsChan = true
            }
            this.sauna.start_date = moment(this.order.services[0].start_date).subtract(2, 'hours').format('yyyy-MM-DDTHH:mm')
            this.sauna.end_date = moment(this.order.services[0].end_date).subtract(2, 'hours').format('yyyy-MM-DDTHH:mm')
            this.sauna.id = this.order.services[0].id
            this.chan.start_date = moment(this.order.services[1].start_date).subtract(2, 'hours').format('yyyy-MM-DDTHH:mm')
            this.chan.end_date = moment(this.order.services[1].end_date).subtract(2, 'hours').format('yyyy-MM-DDTHH:mm')
            this.chan.id = this.order.services[0].id
            this.order.sauna_set = []
            
        },
        async getLodgeList() {
            const url = "/api/lodge/"
            const response = await (
                await fetch(
                    url
                )
            ).json();
            this.lodgeList = response;
        },
    },
    mounted() {
        if(this.orderProp){
            this.getOrder(this.orderProp)
            this.getOrderProduct(this.orderProp)
        }
        
        this.getLodgeList()
        // this.getOrderServices()
        this.getAllServices()
    },
}
</script>
<style scoped>
.w-30px{
    width: 30px;
}    
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

.modal-footer {
    display: block
}

.modal-header {

    flex-direction: row;
    justify-content: space-between;
    padding: 5px;

}
.modal-body{
    max-width: 765px;
}
.modal-header-slot {
    flex: 8;
    padding: 0px 15px;
}

.modal-header-btn {
    flex: 2
}

.modal-header .btn {
    padding: 5px !important;
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
    overflow: hidden;
    margin-top: 0.75rem;
}

.modal-container.modal-lg {
    max-width: 800px
}

.modal-body2 {
    max-height: calc(90vh);
    min-height: 600px;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 0px
}

.modal-enter-active,
.modal-leave-active {
    transition: opacity .2s;
}

.modal-enter,
.modal-leave-to

/* .fade-leave-active до версии 2.1.8 */
    {
    opacity: 0;
}

.btn-close {
    background: transparent url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z'/%3e%3c/svg%3e") center/1em auto no-repeat;
    box-sizing: content-box;
    width: 1em;
    height: 1em;
    padding: .25em .25em;
    color: #000;
}
</style>
