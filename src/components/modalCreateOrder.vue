<template lang="pug">
transition(name="modal" )
    .modal-mask(aria-hidden="true")
        .modal-wrapper(ref="modal" @click="$emit('input',false)"  role="dialog"  aria-hidden="true" @keydown.esc="$emit('input',false)" tabindex='-1')
        .modal-container(@click.stop="" role="document" @keydown.esc="$emit('input',false)")
            .modal-header
                div(class="modal-header-slot")
                    div(v-if="order.id") {{ 'Редактирование заказа №' + order.id }}
                    div(v-else) Новый заказ
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
                        input(type="tel" v-model="order.phone" class="form-control" placeholder="+7-(000)-000-00-00") 
                    div(class="form-group")
                        label(for="exampleInputEmail1") Email 
                        input(type="email" v-model="order.email" class="form-control" aria-describedby="emailHelp" placeholder="Email") 
                    div(class="form-group")
                        label(for="exampleInputEmail1") Статус заказа
                        select(v-model="order.status" class="form-select")
                            option(value="") --
                            option(v-for="status in statusOrder" :key="status.status" :value="status.status") {{status.name}}
                    div(class="form-group")
                        label(for="exampleInputEmail1") Статус договора
                        select(v-model="order.dogovor_status" class="form-select")
                            option(value="") --
                            option(v-for="status in statusContractList" :key="status.status" :value="status.status") {{status.name}}
                    div(class="form-group")
                        label(for="exampleFormControlInput1" class="form-label") Прикрепить файл:
                        input(class="form-control" type="file" name="" id="file" ref="file" v-on:change="handleFileUpload()")
                    div(class="form-group")
                        label(for="exampleFormControlTextarea1") Комментарий:
                        textarea(v-model="order.comment" class="form-control" rows="3")
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
                                        th $
                                        th(style="min-width: 32px;")                                                                                                             
                                tbody(class="scroll")
                                    template(v-for="(product, index) in order.products")
                                        tr()
                                            td(class="w-30px") {{ index + 1 }}
                                            td()
                                                select(v-model="product.product" class="form-select")
                                                    option(value="") {{ product.product ? product.product.name : '--' }}
                                                    option(v-if="allProductsList" v-for="product in allProductsList" :value="product.id") {{product.name}}
                                            td(class="w-25")
                                                input(@input="resultProduct(product)" v-model="product.value" class="form-control" type="number" step="1") 
                                            td(class="w-25")
                                                input(v-model="product.cost" class="form-control" type="number" step="1") 
                                            td 
                                                input(v-model="product.pay" type="checkbox" class="form-check-input")
                                            td(@click="removeItem(product, index, order.products, 1)")
                                                svg(xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16")
                                                    path(d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z")

                    button(class="btn btn-primary btn-sm" @click="addNewRow(order.products)") Добавить
                    div(class="form-check")
                        input(v-model="IsSauna" type="checkbox" class="form-check-input")
                        label(class="form-check-label") Баня                    
                    div(v-if="IsSauna" class="form-group")
                        template(v-if="order.services.length > 0" v-for="(service, index) in order.services")
                            div(v-if="service.name == 'SN'" style="margin: 10px 0px")
                                label(style="margin-right: 10px;") С
                                input(v-model="service.start_date" type="datetime-local")
                                label(style="margin-right: 10px;") ДО
                                input(v-model="service.end_date" type="datetime-local")
                                div(@click="removeItem(service, index, order.services, 3)" style="display: inline-block")
                                    svg(xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16")
                                        path(d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z")
                        button(class="btn btn-primary btn-sm" @click="addNewRowService('SN')") Добавить
                    div(class="form-check")
                        input(v-model="IsChan" type="checkbox" class="form-check-input")
                        label(class="form-check-label") Чан                    
                    div(v-if="IsChan" class="form-group")
                        template(v-if="order.services.length > 0" v-for="(service, index) in order.services")
                            div(v-if="service.name == 'CH'" style="margin: 10px 0px")
                                label(style="margin-right: 10px;") С
                                input(v-model="service.start_date" type="datetime-local")
                                label(style="margin-right: 10px;") ДО
                                input(v-model="service.end_date" type="datetime-local")
                                div(@click="removeItem(service, index, order.services, 3)" style="display: inline-block")
                                    svg(xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16")
                                        path(d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z")
                        button(class="btn btn-primary btn-sm" @click="addNewRowService('CH')") Добавить  

            h5 Детали заказа
            .table-outer
                .table-iner
                    table(class="w-100")
                        thead
                            tr
                                th №
                                th Дом 
                                th Заезд 
                                th Выезд
                                th Стоимость
                                th(style="min-width: 32px;")                                                                                                             
                        tbody(class="scroll")
                            template(v-for="(lodge, index) in order.orderlodge_set")
                                tr()
                                    td() {{ index + 1 }}
                                    td()
                                        select(v-model="lodge.lodge" class="form-select")
                                            option(value="")
                                            option(v-for="lodge in lodgeList" :value="lodge.id") {{lodge.name}}
                                    td()
                                        DatePicker(v-model.string="lodge.start_date" :masks="masks")
                                            template(#default="{ inputValue, inputEvents }")
                                                input(class="form-control" :value="inputValue" v-on="inputEvents")


                                        //- input(v-model="lodge.start_date" class="form-control" type="date" pattern="\d{2}.\d{2}.\d{4}")
                                    td()
                                        DatePicker(v-model.string="lodge.end_date" :masks="masks")
                                            template(#default="{ inputValue, inputEvents }")
                                                input(class="form-control" :value="inputValue" v-on="inputEvents")
                                        //- input(v-model="lodge.end_date" class="form-control" type="date" pattern="\d{2}.\d{2}.\d{4}")
                                    td()
                                        input(v-model="lodge.cost" class="form-control" type="number" step="1") 
                                    td(@click="removeItem(lodge, index, order.orderlodge_set, 2)")
                                        svg(xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16")
                                            path(d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z")
                    button(class="btn btn-primary" style="margin:10px 0px" @click="addNewRow(order.orderlodge_set)") Добавить        
            button(class="btn btn-success" @click="saveOrder()") сохранить            
            .modal-footer
                slot(name="footer") 
</template>
<script>

import { Order, Product, Service, Lodge } from "@/api";
import axios from 'axios'
import statusOrder from '../assets/statusOrder'
import statusContractList from '../assets/statusContracrList'
import 'v-calendar/style.css';

import { DatePicker } from 'v-calendar';
export default {
    name: 'modal-create-order',
    data: function () {
        return {
            IsSauna: false,
            IsChan: false,
            sauna: {},
            chan: {},
            saunaTime: null,
            productList: [],
            allProductsList: [],
            // order: {
            //     "order_lodge_set": [
            //         {}
            //     ],
            //     "services": [],
            //     "products": [
            //         {}
            //     ],
            //     "products_set": [],
            //     "services_set": [],
            //     "orderlodge_set": [
            //         {
            //             "lodge": {
            //                 "id": 1,
            //                 "photo_gallery_set": [
            //                     {
            //                         "id": 1,
            //                         "name": "Первая спальня",
            //                         "img": "http://127.0.0.1:8000/media/img/KC-001.webp",
            //                         "lodge": 1,
            //                         "group": null
            //                     },
            //                     {
            //                         "id": 2,
            //                         "name": "Кухня",
            //                         "img": "http://127.0.0.1:8000/media/img/1.webp",
            //                         "lodge": 1,
            //                         "group": null
            //                     },
            //                     {
            //                         "id": 3,
            //                         "name": "Вторая спальня",
            //                         "img": "http://127.0.0.1:8000/media/img/2.webp",
            //                         "lodge": 1,
            //                         "group": null
            //                     },
            //                     {
            //                         "id": 4,
            //                         "name": "Третья спальня",
            //                         "img": "http://127.0.0.1:8000/media/img/3.webp",
            //                         "lodge": 1,
            //                         "group": null
            //                     },
            //                     {
            //                         "id": 5,
            //                         "name": "Санузел",
            //                         "img": "http://127.0.0.1:8000/media/img/4.webp",
            //                         "lodge": 1,
            //                         "group": null
            //                     },
            //                     {
            //                         "id": 34,
            //                         "name": "Гостиная",
            //                         "img": "http://127.0.0.1:8000/media/img/KC-011.webp",
            //                         "lodge": 1,
            //                         "group": null
            //                     }
            //                 ],
            //                 "special_price_set": [
            //                     {
            //                         "id": 1,
            //                         "name": "Новый Год 2023",
            //                         "date_init": "2023-12-23",
            //                         "date": "2023-12-31",
            //                         "date_end": "2024-01-02",
            //                         "cost": 95000,
            //                         "active": true,
            //                         "lodge": 1
            //                     },
            //                     {
            //                         "id": 2,
            //                         "name": "Новый Год 2023 (cо 2 января по 7 января)",
            //                         "date_init": "2023-12-23",
            //                         "date": "2024-01-02",
            //                         "date_end": "2024-01-07",
            //                         "cost": 30000,
            //                         "active": true,
            //                         "lodge": 1
            //                     }
            //                 ],
            //                 "price_set": [
            //                     {
            //                         "id": 1,
            //                         "name": "Будни дни",
            //                         "date_init": "2023-12-23",
            //                         "days": "1,2,3,4,5",
            //                         "cost": 10000,
            //                         "lodge": 1
            //                     },
            //                     {
            //                         "id": 2,
            //                         "name": "Выходной день",
            //                         "date_init": "2023-12-23",
            //                         "days": "6,7",
            //                         "cost": 15000,
            //                         "lodge": 1
            //                     }
            //                 ],
            //                 "availability_set": [
            //                     {
            //                         "name": "до воды 150 м"
            //                     },
            //                     {
            //                         "name": "до бани 50 м"
            //                     },
            //                     {
            //                         "name": "до беседки 5 м"
            //                     }
            //                 ],
            //                 "name": "Дом Кузнеца",
            //                 "num": "2",
            //                 "sub_name": "",
            //                 "description": "двухэтажный деревянный дом, где могут разместиться до 11 человек. 4 просторные комнаты, в которых будет удобно и парам, и семьям с детьми.",
            //                 "short_description": "2 смежные и 2 изолированные спальни, просторная кухня-гостиная, санузел",
            //                 "conveniences": "кухня - полный комплект посуды на 11 человек, холодильник, обеденный стол, электроплита с духовым шкафом, микроволновая печь, электро чайник, санузел - горячая и холодная вода, музыкальный центр, 3 телевизора",
            //                 "include": "пользование спортивными, детскими площадками, мангалом и решеткой, охраняемая парковка, охраняемый причал",
            //                 "maxP": 11,
            //                 "cost_per_unit": 10000,
            //                 "img": "http://127.0.0.1:8000/media/img/house-6.webp",
            //                 "img_small": "http://127.0.0.1:8000/media/img/low.jpg",
            //                 "plan1": null,
            //                 "plan2": null,
            //                 "uslugi": "1",
            //                 "slug": "dom-kuznetsa",
            //                 "avalible": true,
            //                 "lodge_main": null
            //             },
            //             "start_date": "05.04.2024",
            //             "end_date": "07.04.2024",
            //             "cost": 10000
            //         }
            //     ],
            //     "customer": "ФИО",
            //     "phone": "89819710592",
            //     "email": "t@test.ru",
            //     "status": "WT",
            //     "dogovor_status": "NC"
            // },
            order: {
                order_lodge_set: [{}],
                services: [],
                products: [{}],
                products_set: [],
                services_set: [],
                orderlodge_set: [{}],
            },
            file: null,
            test: {},
            lodgeList: [],
            statusOrder,
            statusContractList,
            masks: {
                modelValue: 'DD.MM.YYYY',
                L: 'DD.MM.YYYY',
                iso: 'DD.MM.YYYY'
            }

        }
    },
    props: ['orderProp'],
    components: { DatePicker },
    watch: {
    },
    methods: {
        resultProduct(item) {
            item.cost = item.value * this.allProductsList.filter(x => x.id === item.product)[0].cost
        },
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
        },
        addNewRowService(name) {
            let def = { name: name }
            this.order.services.push(def)
        },
        validate() {
            if (!this.order.customer) {
                this.$notify({

                    type: 'warn',
                    title: 'Ошибка',
                    text: 'Укажите ФИО Покупателя'
                });
                return false
            }
            if (!this.order.order_lodge_set[0].lodge) {
                this.$notify({
                    type: 'warn',
                    title: 'Ошибка',
                    text: 'Укажите Дом'
                });
                return false
            }
        },
        removeItem(item, index, array, type) {
            if (item.id && type == 1) {
                Product.delete(item)
            }
            // if (item.id && type == 2) {
            //     OrderLodge.delete(item)            
            // }    
            if (item.id && type == 3) {
                Service.delete(item)
            }
            array.splice(index, 1)
        },
        addNewRow(array) {
            let def = {}
            array.push(def)
        },
        async getAllServices() {
            const url = "/api/uslugi/"
            const response = await (
                await fetch(
                    url
                )
            ).json();
            this.allProductsList = response.results
        },
        async getOrderProduct(id) {
            this.productList = (await Product.objects.getList({ order: id })).results
        },
        // СОХРАНЕНИЕ ЗАКАЗА
        async saveOrder() {

            if (this.file || this.order.dogovor) {
                this.saveOrderFormData()
                this.closeModal()
            }
            else {
                Object.entries(this.order.products[0]).length === 0 ? this.order.products_set = [] : this.order.products_set = this.order.products
                this.order.services_set = this.order.services
                
                await Order.save(this.order)
                this.closeModal()
            }


        },

        closeModal() {
            this.$emit('closeModal')
        },
        async getLodgeList() {
            this.lodgeList = (await Lodge.getList({ 'avalible': true })).results
        },
        async saveOrderFormData() {
            let formData = new FormData();
            formData.append('customer', this.order.customer)
            formData.append('phone', this.order.phone)
            formData.append('email', this.order.email)
            formData.append('dogovor_status', this.order.dogovor_status)
            formData.append('status', this.order.status)
            formData.append('dogovor', this.file)
            formData.append('comment', this.order.comment)
            if (Object.entries(this.order.products[0]).length === 0) {
                formData.append(`products_set[0]cost`, '')
                formData.append(`products_set[0]product`, '')
                formData.append(`products_set[0]value`, '')
            }
            else {
                this.order.products.forEach((product, index) => {
                    formData.append(`products_set[${index}]cost`, product.cost)
                    formData.append(`products_set[${index}]product`, product.product)
                    formData.append(`products_set[${index}]value`, product.value)
                    if (product.id) {
                        formData.append(`products_set[${index}]id`, product.id)
                    }
                })
            }
            this.order.orderlodge_set.forEach((lodge, index) => {
                formData.append(`orderlodge_set[${index}]cost`, lodge.cost)
                formData.append(`orderlodge_set[${index}]end_date`, lodge.end_date)
                formData.append(`orderlodge_set[${index}]lodge`, lodge.lodge)
                formData.append(`orderlodge_set[${index}]start_date`, lodge.start_date)
                if (lodge.id) {
                    formData.append(`orderlodge_set[${index}]id`, lodge.id)
                }
            });
            if (this.order.services.length > 0) {
                this.order.services.forEach((service, index) => {
                    formData.append(`services_set[${index}]end_date`, service.end_date)
                    formData.append(`services_set[${index}]name`, service.name)
                    formData.append(`services_set[${index}]start_date`, service.start_date)
                    if (service.id) {
                        formData.append(`services_set[${index}]id`, service.id)
                    }
                })
            }
            else {
                formData.append(`services_set[0]end_date`, '')
                formData.append(`services_set[0]name`, '')
                formData.append(`services_set[0]start_date`, '')
            }
            let promis
            if (this.order.id) {
                promis = axios.patch(this.apiUrl + this.order.id + '/', formData)
            }
            promis
        },
    },
    mounted() {
        if (this.orderProp.id) {
            this.order = { ...this.orderProp }
            if (this.order.products.length < 1) {
                this.addNewRow(this.order.products)
            }
            this.order.orderlodge_set = this.orderProp.order_lodge_set
            // this.$set(this.order, 'orderlodge_set', this.orderProp.order_lodge_set)
            for (let i = 0; i < this.orderProp.order_lodge_set.length; i++) {
                this.order.orderlodge_set[i].lodge = this.orderProp.order_lodge_set[i].lodge.id
            }
            if (this.orderProp.products[0].id) {
                this.$set(this.order, 'products', this.orderProp.products)
                for (let i = 0; i < this.orderProp.products.length; i++) {
                    this.order.products[i].product = this.orderProp.products[i].product.id
                }
            }
            this.order.services = this.orderProp.services
            // this.$set(this.order, 'services', this.orderProp.services)
            for (let i = 0; i < this.order.services.length; i++) {
                if (this.order.services[i].name == 'SN') {
                    this.IsSauna = true
                }
                if (this.order.services[i].name == 'CH') {
                    this.IsChan = true
                }
            }
            // this.getOrderProduct(this.orderProp.id)
        }
        this.getLodgeList()
        // this.getOrderServices()
        this.getAllServices()
    },
}
</script>
<style scoped>
.w-30px {
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

.modal-body {
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
