<template lang="pug">
div(class="container-xxl")
    .row        
        .card.col-md-10
            .card-body.d-flex.align-items-center.justify-content-between
                div
                    h4 Фильтр
                div(class="d-flex align-items-center")
                    label(for="exampleFormControlInput1") Начало:
                    div(class="col-form-label")
                        input(v-model="dateStart" class="form-control" type="date" name="" id="")
                div(class="d-flex align-items-center")
                    label(for="exampleFormControlInput1") Конец:
                    div(class="col-form-label")
                        input(v-model="dateEnd" class="form-control" type="date" name="" id="")
                div(class="d-flex align-items-center")
                    label(for="exampleFormControlInput1") Дом:
                    select(v-model="filterLodge" class="form-select")                
                        option(value="") Не выбран
                        option(v-if="lodgeList" v-for="lodge in lodgeList" :value="lodge.id") {{lodge.name}}
                div(class="d-flex align-items-center")
                    label(for="exampleFormControlInput1") Поиск:
                    div(class="col-form-label")
                        input(v-model="orderId" class="form-control" @keyup.enter="getOrderList()")

                        
    .row        
        h2 Реестр
        table(ref="exportable_table" class="table table-bordered")
            thead
                tr
                    th() № 
                    th(style="width: 10%") Дата заезда
                    th(style="width: 10%") Дата выезда
                    th() Дом/Номер 
                    th() ФИО ответственного                     
                    th() Комментарии
                    th() Стоимость
                    th() Примечания 
            tbody(v-if="orderList")                                
                template(v-for="order in orderList")
                    template(v-if="order.order_lodge_set.length > 1")    
                        tr
                            td()
                                a(class="btn btn-link" @click="select(order)") {{ order.id}} 
                            td() {{ renderDateDMY(order.order_lodge_set[0].start_date) }} 
                            td() {{ renderDateDMY(order.order_lodge_set[0].end_date) }}
                            td {{ order.order_lodge_set[0].lodge.name }}
                            td() {{ order.customer }}                            
                            td() {{ order.comment }}
                            td() {{ order.order_lodge_set[0].cost }}
                            td() {{ order.dogovor_status ? order.dogovor_status : '---'}}
                        tr(v-for="n in order.order_lodge_set.length - 1")
                            td() 
                                a(class="btn btn-link" @click="select(order)") {{ order.id}} 
                            td {{ renderDateDMY(order.order_lodge_set[n].start_date) }} 
                            td {{ renderDateDMY(order.order_lodge_set[n].end_date) }}
                            td {{ order.order_lodge_set[n].lodge.name }}
                            td() {{ order.customer }}                            
                            td() {{ order.comment }}
                            td() {{ order.order_lodge_set[n].cost }}
                            td() {{ order.dogovor_status ? order.dogovor_status : '---'}}
                    template(v-else)
                        tr
                            td()
                                a(class="btn btn-link" @click="select(order)") {{ order.id}} 
                            td()
                                template(v-for="date in order.order_lodge_set") 
                                    div {{ renderDateDMY(date.start_date)}} 
                            td()
                                template(v-for="date in order.order_lodge_set") 
                                    div {{ renderDateDMY(date.end_date) }} 
                            td
                                template(v-for="name in order.order_lodge_set") 
                                    div  {{ name.lodge.name }}
                            td() {{ order.customer ? order.customer : '--'}}                                                                                
                            td {{ order.comment }}
                            td {{ order.order_lodge_set[0].cost }}
                            td() {{ order.dogovor_status ? getChoice(order.dogovor_status) : '---'}}                                        
        button(style="width: 60px; height: 60px" class="d-flex btn" @click="ExportExcel('xlsx')")
            img(src="../assets/excel-svgrepo-com.svg" alt="")
    modalDetailVue(:value="value" v-if="showDetails" @close="close()" @editing="editing()" @deleteOrder="deleteOrder()")
</template>
<script>
import modalDetailVue from '../components/modalDetailOrder.vue'
import { Order, Lodge } from '@/api'
import moment from 'moment'
export default {
    name: 'registry-view',
    data: function () {
        return {
            orderList:[],                     
            choice: [
                { choice:'HC', text:'Есть договоры'},
                { choice:'NC', text:'Нет договоров'},
                { choice:'WS', text:'Есть договоры(один без подписи)'},
                { choice:'WP', text:'Есть договоры(один без печати)'},
                { choice:'SP', text:'Есть два договора без печати и без подписи'},
            ],
            dateStart: moment().startOf('month').format('YYYY-MM-DD'),
            dateEnd: moment().endOf('month').format('YYYY-MM-DD'),
            filterLodge: '',            
            showDetails: false,            
            value: null,
            lodgeList:[],
            orderId:'',
        }
    },
    components: {
        modalDetailVue
    },
    mounted() {                 
        this.getLodgeList()    
        this.getOrderList()
    },
    watch: {
        dateStart(){
            this.getOrderList()
        },
        dateEnd(){
            this.getOrderList()
        },
        filterLodge(){
            this.getOrderList()
        },
    },
    methods: {
        async getLodgeList(){
            this.lodgeList = (await Lodge.objects.getList()).results 
        },
        close(){
            this.showDetails = false
            this.value = {}
        },
        select(l){
            this.value = l
            this.showDetails = true
        },
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
            {wpx:67},
            {wpx:150},
            {wpx:150},
            {wpx:150},
            {wpx:68},
            
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
            let a =  moment(dat).format('DD.MM.YYYY')
            return a
        },
        async getOrderList() {
            let filter = {
                lodges: this.filterLodge,
                search_start: this.dateStart,
                search_end: this.dateEnd,    
                id: this.orderId,            
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