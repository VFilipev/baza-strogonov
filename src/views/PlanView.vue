<template lang="pug">
div(class="container-xxl")
    .row        
        .card.col-md-6
            .card-body.d-flex.align-items-center.justify-content-between
                div
                    h2 Фильтр
                div(class="d-flex align-items-center")
                    label(for="exampleFormControlInput1") Начало:
                    div(class="col-form-label")
                        input(v-model="dateStart" class="form-control" type="date" name="" id="")
                div(class="d-flex align-items-center")
                    label(for="exampleFormControlInput1") Конец:
                    div(class="col-form-label")
                        input(v-model="dateEnd" class="form-control" type="date" name="" id="")
    .row
        
            h2 Разнарядка 
            table(ref="exportable_table" class="table table-bordered")
                thead
                    tr
                        th() № 
                        th(style="width: 10%") Дата/Время
                        th() Дом/Номер 
                        th() ФИО ответственного 
                        th() Баня
                        th() Чан
                        th() Товар/Кол-во
                        th() Комментарии
                        th() Примечания 
                tbody(v-if="orderList")                                
                    template(v-for="order in orderList")
                        template(v-if="order.order_lodge_set.length > 1")    
                            tr
                                td(:rowspan="order.order_lodge_set.length") {{ order.id}} 
                                td() {{ renderDateDMY(order.order_lodge_set[0].start_date) }} <br> {{ renderDateDMY(order.order_lodge_set[0].end_date) }}
                                td {{ order.order_lodge_set[0].lodge.name }}
                                td(:rowspan="order.order_lodge_set.length") {{ order.customer }}
                                td(:rowspan="order.order_lodge_set.length") 
                                    template(v-for="service in order.services")
                                        div(v-if="service.name == 'SN'") {{ renderDateDMY(service.start_date)}}<br>{{ renderDateDMY(service.end_date) }}
                                td(:rowspan="order.order_lodge_set.length") 
                                    template(v-for="service in order.services")
                                        div(v-if="service.name == 'CH'") {{ renderDateDMY(service.start_date) }}<br>{{renderDateDMY(service.end_date)}}
                                td(:rowspan="order.order_lodge_set.length") 
                                    template(v-for="product in order.products")
                                        div(:class="product.pay === true ? 'paid' : ''") {{ product.product.name + '-' + product.value}}
                                td(:rowspan="order.order_lodge_set.length") {{ order.comment }}
                                td(:rowspan="order.order_lodge_set.length") {{ order.comment }}
                            tr(v-for="n in order.order_lodge_set.length - 1")
                                td {{ renderDateDMY(order.order_lodge_set[n].start_date) }} <br> {{ renderDateDMY(order.order_lodge_set[n].end_date) }}
                                td {{ order.order_lodge_set[n].lodge.name }}
                        template(v-else)
                            tr
                                td() {{ order.id}}    
                                td()
                                    template(v-for="date in order.order_lodge_set") 
                                        div {{ renderDateDMY(date.start_date)}} <br> {{ renderDateDMY(date.end_date) }} 

                                td
                                    template(v-for="name in order.order_lodge_set") 
                                        div  {{ name.lodge.name }}
                                td() {{ order.customer ? order.customer : '--'}}
                                td() 
                                    template(v-for="service in order.services")
                                        div(v-if="service.name == 'SN'") {{ renderDateDMY(service.start_date)}}<br> {{ renderDateDMY(service.end_date) }}
                                            tr(style="border-bottom:1px solid #dee2e6")
                                                td(colspan="100%" style="width: 104px")
  
                                td() 
                                    template(v-for="service in order.services")
                                        div(v-if="service.name == 'CH'") {{ renderDateDMY(service.start_date) }}<br>{{renderDateDMY(service.end_date)}}                                        
                                td()
                                    template(v-for="product in order.products")
                                        div(:class="product.pay === true ? 'paid' : ''") {{ product.product.name + '-' + product.value }}
                                td ---
                                td(v-if="order.dogovor_status") {{ order.dogovor_status ? getChoice(order.dogovor_status) : ''}}                                        
            button(style="width: 60px; height: 60px" class="d-flex btn" @click="ExportExcel('xlsx')")
                img(src="../assets/excel-svgrepo-com.svg" alt="")
  
</template>

<script>
import { Order } from '@/api'
import moment from 'moment'
export default {
    name: 'plan-view',
    data: function () {
        return {
            orderList:[],
            dateStart: "",
            dateEnd: "",            
            choice: [
                { choice:'HC', text:'Есть договоры'},
                { choice:'NC', text:'Нет договоров'},
                { choice:'WS', text:'Есть договоры(один без подписи)'},
                { choice:'WP', text:'Есть договоры(один без печати)'},
                { choice:'SP', text:'Есть два договора без печати и без подписи'},
            ]
        }
    },
    components: {
        
    },
    mounted() {
        this.dateStart = moment().startOf('week').format('YYYY-MM-DD')
        this.dateEnd = moment().endOf('week').format('YYYY-MM-DD')        
        this.getOrderList()
    },
    watch: {
        dateStart(){
            this.getOrderList()
        },
        dateEnd(){
            this.getOrderList()
        }
    },
    methods: {
        userProvidedHtml(index){
            return this.renderDateDMY(this.orderList[index].lodges[0].start_date) + '\r\n' + 'new'
        },
        getChoice(ch){
            let text = ''
            this.choice.forEach(function(item) {
                if(item.choice === ch){
                    text = item.text
                }
            });
            return text    
        },
        ExportExcel(type, fn, dl) {
        let XLSX = require("xlsx");    
        let elt = this.$refs.exportable_table;
        let wb = XLSX.utils.table_to_book(elt, {sheet:"plan"});
        
        let wscols = [
            {wpx:40},
            {wpx:67},
            {wpx:150},
            {wpx:150},
            {wpx:68},
            {wpx:68},
            {wpx:150},
        ];
        wb.Sheets.plan['!cols'] = wscols;
        
        wb.Sheets.plan['B2'].s = {alignment: { wrapText: true, horizontal: 'right'} },
        
        console.log(wb);
        return dl ?
        XLSX.write(wb, {bookType:type, bookSST:true,cellStyles: true, type: 'base64'}) :
        XLSX.writeFile(wb, fn || ((this.dateStart + '-' + this.dateEnd + '.'|| 'SheetJSTableExport.') + (type || 'xlsx')));
        },
        renderDate(date){
            let a =  moment(date).format('DD-MM-YY HH:mm')
            return a
        },
        renderDateDMY(date){
            let dat = moment(date).subtract(2, 'hours')
            let a =  moment(dat).format('DD-MM/HH:mm')
            return a
        },
        async getOrderList() {
            let filter = {
                search_start: moment(this.dateStart, 'YYYY-MM-DD').format('YYYY-MM-DD'),
                search_end: this.dateEnd,                
            }
            this.orderList = (await Order.objects.getList(filter)).results
            
            
        },
    }
}
</script>

<style scoped>
.pre-formatted {
  white-space: pre;
}
.container-plan{
    width: 1320px;
}
.paid{
    border-radius: 4px;
    background-color: #8dff8d;
}
</style>