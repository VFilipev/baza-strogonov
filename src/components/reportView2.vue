<script>
import toURLParams from '@/assets/toURLParams'
import TransportNav from '../components/TransportNav'
import axios from 'axios'
import BillListMain from '@/supply/components/BillListMain'
import FuelMonthRecordList from '@/transport/components/FuelMonthRecord'
import Loading from 'vue-loading-overlay';
import {MonthRecord, VehicleTyp} from "@/api"
import moment from 'moment'

import { Plotly } from 'vue-plotly'

export default{
    name: 'tabel-report',
    data: function() {return {
        apiUrl:'/api/transport/month_record/finance_report/',
        filters:{'billing_period':undefined},
        isLoading:false,
        selectedVehicle:{},
        month:'',
        pieData:[],
        dataUp:{},
        showOpertion:false,
        showBillList:false,
        data:{},
        vehicleTable:[],
        fuel_recor:{},
        fuel_cost:50,
        'filterField':[
            {'name':'billing_period', 'verbose_name':'Месяц',component:'month-date-picker'},
            ]
    }},
    components:{
        TransportNav,
        BillListMain,
        Loading,
        FuelMonthRecordList,
        Plotly,
    },
    watch:{
        filters:{
            deep:true,
            handler(){
                this.getData()
                
                this.getData2()
            }
        }
    },

    methods: {
        filterUpdate:function(filter){
            this.filters=filter
            this.getData()
            
            this.getData2()
        },
        ExportExcel(type, fn, dl) {
        let XLSX = require("xlsx");    
        let elt = this.$refs.exportable_table;
        let wb = XLSX.utils.table_to_book(elt, {sheet:"Sheet JS"});
        return dl ?
        XLSX.write(wb, {bookType:type, bookSST:true, type: 'base64'}) :
        XLSX.writeFile(wb, fn || ((this.name + '.'|| 'SheetJSTableExport.') + (type || 'xlsx')));
        },
        async getData2(){

            let params = {...this.filter}

            params.date_start =moment(this.filters.billing_period,'MM.YYYY').startOf('month').format("DD.MM.YYYY")
            params.date_end=moment(this.filters.billing_period,'MM.YYYY').endOf('month').format("DD.MM.YYYY")
          //  params.vehicle =this.vehicle.vehicle__id
            const response = await axios.get('/api/transport/month_record/year_finance_report_per_month_json/',{params})
            this.month  =response.data.data.month
            this.vehicleTable = response.data.data;
            this.vehicleTable.month=undefined
            let pieValue = [
                this.vehicleTable['salary_total'][0],
                this.vehicleTable['bill_leasing'][0],
                this.vehicleTable['bill_invest'][0],
                this.vehicleTable['bill_total'][0] - this.vehicleTable['bill_invest'][0] -this.vehicleTable['bill_leasing'][0] ,
                this.vehicleTable['fuel_money_total'][0],
            ]
            let pieLabel = [
                'Зарплата',  
                'Лизинг',  
                'Инвестиции ',  
                'Прочие счета',  
                'Топливо',  
            ]
            this.pieData = [{
                values: pieValue,
                labels: pieLabel,
                type: 'pie',
                automargi:true,
                showlegend: false,
                textinfo:"label+percent",
                margin:{t:0}
            }];
 
        }, 
        updateList(){
            let dataUp = []
            let current_category 
            for (let x of this.vehicleGroup){
                
                x.total=0
                x.market=0
                x.delta = 0
                if (current_category != x.get_category_display){
                    current_category = x.get_category_display
                    dataUp.push({name:current_category,is_category:true})
                }
                dataUp.push(x)
                    let veh_list = this.data.filter(e => e.vehicle.typ2==x.id)
                    for (let y  of veh_list) {
                        x.total+=+y.total
                        x.market+= +y.get_market_cost_total
                        x.delta += +y.get_renta_total
                if (x.is_active){
                        dataUp.push(y)
                }
                    }

            }


            this.dataUp = dataUp



        },
        async getData(){
            if (this.filters.billing_period){
            this.isLoading=true
            this.vehicleGroup = (await VehicleTyp.getList()).results
            this.vehicleGroup.forEach((e) => {e.is_group=true;e.is_active=true})
            this.data =(await MonthRecord.getList(this.filters)).results
            //this.fuel_cost =(await FuelMonthRecord.month_cost(this.filters))
            this.updateList()
            this.isLoading=false
            }
        },
        showOps(veh){
            this.showOpertion=true
            this.selectedVehicle=veh
        },
        showBill(veh){
            this.showBillList=true
            this.selectedVehicle=veh
        },
        calc_pforit(veh){

            if (veh.vehicle&& veh.vehicle.market_price){
                if (veh['vehicle']['tarif_typ']=='H'){
                    return (veh['cost_per_hour'] -veh.vehicle.market_price)/veh.vehicle.market_price*100
                }

                if (veh['vehicle']['tarif_typ']=='K'){
                    return (veh['cost_per_km'] -veh.vehicle.market_price)/veh.vehicle.market_price*100
                }
            }

        }
    },         
    computed:{
        url(){
            return this.apiUrl+'?' +toURLParams(this.filters)
        },
        filterOp(){
            if (this.selectedVehicle){
                return{...this.filters,vehicle:this.selectedVehicle.id}
            }else{
                return{...this.filters,vehicle_isnull:true}

            }
        }
    }
}
</script>
<template lang="pug">
div
    .row
        .col-md-2
            .card
                transport-nav
        .col-md-10
            filters-panel( :groupRow="true" :fields="filterField", v-model="filters" name="transport_report")
            a(class="btn btn-primary" :href="url")  Скачать
            .card
                .card-body
                    .row
                        .col-6
                            plotly( :data="pieData",:layout="{margin:{'t':50,b:100}}" )
                        .col-6
                            table(class="table table-hover table-bordered table-small") 
                                thead
                                    tr
                                        th 
                                        th(v-for="m in month")  {{m}}
                                tbody(v-if="vehicleTable")
                                    tr
                                        td(class=" text-left") 
                                            b Всего часов
                                        td(v-for="d in vehicleTable['hours']" class="text-right") {{d|formatNumber}}
                                    tr
                                        td(class=" text-left")  
                                            b Стоимость часа
                                        td(v-for="d in vehicleTable['cost_per_hour_avg']" class="text-right") {{d|formatNumber}}

                                    tr
                                        td(class=" text-left")   
                                            b Зарплата 
                                        td(v-for="d in vehicleTable['salary_total']" class="text-right") 
                                            b {{d|formatNumber}}
                                    tr.small-row
                                        td(class=" text-left")  На технике
                                        td(v-for="d in vehicleTable['salary']" class="text-right") {{d|formatNumber}}

                                    tr.small-row(v-if="vehicleTable['salary_no_vehicle']")
                                        td(class=" text-left")    Без технике
                                        td(v-for="d in vehicleTable['salary_no_vehicle']" class="text-right") {{d|formatNumber}}

                                    tr.small-row(v-if="vehicleTable['salary_no_vehicle_km']")
                                        td(class=" text-left")    Коммандировочные, больничные
                                        td(v-for="d in vehicleTable['salary_no_vehicle_km']" class="text-right") {{d|formatNumber}}


                                    tr
                                        td(class=" text-left")  
                                            b Топливо
                                        td(v-for="d in vehicleTable['fuel_money_total']"  class="text-right")  
                                            b {{d|formatNumber}}
                                    tr.small-row
                                        td(class=" text-left")   На технике, л 
                                        td(v-for="d in vehicleTable['fuel_l']"  class="text-right") {{d|formatNumber}}
                                    tr.small-row
                                        td(class=" text-left")   На технике, Р
                                        td(v-for="d in vehicleTable['fuel_money']" class="text-right") {{d|formatNumber}}

                                    tr.small-row(v-if="vehicleTable['fuel_employee']")
                                        td(class=" text-left")   Топливо сотрудники, Р
                                        td(v-for="d in vehicleTable['fuel_employee']" class="text-right") {{d|formatNumber}}
                                    
                                    tr.small-row(v-if="vehicleTable['fuel_project']")
                                        td(class=" text-left")   Топливо объекты, Р
                                        td(v-for="d in vehicleTable['fuel_project']" class="text-right") {{d|formatNumber}}

                                    tr
                                        td(class=" text-left")  
                                            b Выставлено счетов 
                                        td(v-for="d in vehicleTable['bill_total']" class="text-right") 
                                            b {{d|formatNumber}}
                                    tr.small-row
                                        td(class=" text-left small-row")  Из них по технике  
                                        td(v-for="d,index in vehicleTable['bill_vehicle']" class="text-right")  {{d-vehicleTable['bill_leasing'][index]|formatNumber}}
                                    tr.small-row(v-if="vehicleTable['bill_no_vehicle']")
                                        td(class=" text-left")  Из них без техники
                                        td(v-for="d in vehicleTable['bill_no_vehicle']" class="text-right") {{d|formatNumber}}
                                    tr.small-row(v-if="vehicleTable['bill_no_vehicle']")
                                        td(class=" text-left")  Лизинг
                                        td(v-for="d in vehicleTable['bill_leasing']" class="text-right") {{d|formatNumber}}

                                    tr
                                        td(class=" text-left")  
                                            b Расходные материалы
                                        td(v-for="d in vehicleTable['expendable_materials']" class="text-right") {{d|formatNumber}}



                                    tr
                                        td(class=" text-left")  
                                            b Всего
                                        td(v-for="d in vehicleTable['total_spend']" class="text-right")  
                                            b {{d|formatNumber}}
                        


            .card(v-if='filters.billing_period')
                .card-body
                    loading(:active.sync="isLoading", 
                        :can-cancel="true", 
                        :is-full-page="false",)
                    table(ref="exportable_table" class="transport-payrol table-sm  table-bordered table-hover ")
                        thead
                            tr 
                                th Название
                                th Номер
                                th Рыночная цена
                                th Доходность
                                th Стоимость 1ч
                                th Прошлый м. 
                                th Себестоимость 1км
                                th Оплата труда
                                th Топливо,Р
                                th Расходные материалы,Р
                                th Пройдено по одоменту
                                th Часов отработано
                                th Выставлено Счетов
                                th Расходы за месяц
                        tbody
                        template(v-for="(veh,index) in dataUp" :class="veh.id?'':'status-warning'")
                            tr(v-if="veh.is_group || veh.is_category" 
                                :class="{'collaps-row__active':veh.is_active,'category-row':veh.is_category}")
                                td(colspan="14" class="text-left") {{veh.name}}
                            tr(v-else)
                                td {{veh.vehicle? veh.vehicle.full_name : 'Без Транспортного средства'}}
                                td {{veh.vehicle? veh.vehicle.number: '' }}
                                td {{veh.vehicle? veh.vehicle.market_price: '' }}
                                td
                                    div(v-if='veh.vehicle' :class="calc_pforit(veh,'H')<0?'money_out':'money_in'") {{calc_pforit(veh,'H')| formatNumber}}
                                td(@click="showBill(veh.vehicle)") {{(+veh['cost_per_hour'])| formatNumber}}
                                td
                                td(@click="showBill(veh.vehicle)") {{(+veh['cost_per_km'])| formatNumber}}
                                td(@click="showOps(veh)") {{veh['salary']| formatNumber}}
                                td {{veh.fuel_money|formatNumber}}
                                td {{veh.expendable_materials| formatNumber}} 
                                td {{veh['passed_km']| formatNumber}}
                                td {{veh['hours']| formatNumber}}
                                td(@click="showBill(veh.vehicle)") {{veh['bill_total']| formatNumber}}
                                td(@click="showBill(veh.vehicle)") {{veh['total']| formatNumber}}
                    <button style="width: 60px; height: 60px" class="d-flex btn" @click="ExportExcel('xlsx')">save</button>


    modal-che(v-model="showOpertion" )
        operation-list(:selectable="false" :filter="filterOp" ) 

    modal-che(v-model="showBillList" )
        bill-list-main( :filters="filterOp" ) 




            
</template>
<style>
.transport-payrol td{
    padding: 0.1rem  0.1rem;
    font-size:0.75rem;
    text-align:right;
    

}


.transport-payrol .category-row td{
    font-size:1rem 
}
.transport-payrol tr.category-row {
    background-color:#fff9da
}
</style>
