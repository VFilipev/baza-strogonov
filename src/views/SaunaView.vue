<template lang="pug">
.row
    .col-md-2
        .card
            .card-body
                h2 Фильтр
                label(for="exampleFormControlInput1" class="form-label") Начало
                input(v-model="dateStart" class="form-control" type="date" name="" id="")
                br
                label(for="exampleFormControlInput1" class="form-label") Конец
                input(v-model="dateEnd" class="form-control" type="date" name="" id="")
    .col-md-10
        h2 Баня
        div(class="container-table d-flex")
            div(class="table1")
                div(class="gantt-row") 
                    div(class="order-cell gantt-name" ) День
                div(class="gantt-row")
                    div(class="order-cell gantt-name") Часы 
                div(v-for="header in lodgeList" class="gantt-row")
                    div(class="order-cell gantt-name") {{ header.name }}
            div(class="table2")
                div(class="gantt-row")
                    div(class="gantt-cell gantt-cell-month" v-for="cell in dataRange1" :style="{width:cell[1]}")   {{cell[0]}}
                div(class="day-row")
                    div(class="gantt-cell gantt-cell-day" v-for="cell in hourRange" :class="cell.weekend?'gantt-cell__weekend':''")   {{cell.hour}}

                div(class="row-row" v-for="lodge in lodgeList")                    
                    div(class="gantt-row employee-row")
                        div(class="gantt-cell gantt-cell-day gantt-" v-for="(cell,index) in hourRange"  :class="{'gantt-cell__weekend':cell.weekend}") 
                    template(v-for="l in lodge.order_set")
                        div(v-for="service in l.services" :class="[{'gantt-sauna': service.name == 'SN'}, {'gantt-tub': service.name == 'CH'}]" :style="service.style" @click="select(l)") 
                            div(class="lh-1" v-if="service.style") 
                                span() {{ getChoice(service.name) }}                
                
    modalDetailVue(:value="value" v-if="showDetails" @close="close()" @editing="editing()" @deleteOrder="deleteOrder()")
    modalCreateOrder(:orderProp="value ? value : ''" v-if="showCreateOrder" @close="closeCreateModal()" @closeModal="closeModal()")
</template>

<script>
import moment from 'moment'
import modalDetailVue from '../components/modalDetailOrder.vue'
import modalCreateOrder from '../components/modalCreateOrder.vue'
import { Order,Lodge } from '@/api'

const COL_WIDTH=48;
const TABLE_WIDTH=0;
function getStyle(dateStart, start_date, duration, top, height) {
    let d = duration;
    let start = moment(start_date, 'YYYY-MM-DDTHH:mm');
    let shift = start.diff(dateStart, 'hours')
    if (shift < 0) {
        d = duration + shift
        shift = 0;
    }
    if (d > 0) {
        return {
            width: d * COL_WIDTH + 'px',
            height: height ? height : '20px',
            left: TABLE_WIDTH + shift * COL_WIDTH + 'px',
            top: top + 'px',
            background: ''
        }
    } else {
        return {
            width: '0px',
            height: '0px',
            left: 0 + 'px',
            top: top + 'px',
            background: ''
        }
    }
}
export default {
    name: 'sauna-view',
    data: function () {
        return {
            dismissSecs: 3,
            dismissCountDown: 0,
            showDetails: false,
            showCreateOrder: false,
            value: null,
            dataRange:[],
            dataRange1:[],
            hourRange:[],
            monthRange:[],
            dateStart: "",
            dateEnd: "",
            gantt_start: "2017-11-04",
            lodgeList: [],            
            ganttStyle:{},
            planList:[],
            
            choice: [
                { choice:'SN', text:'Баня'},
                { choice:'CH', text:'Чан'},
            ]
            
        }
    },
    components: {
        modalDetailVue,
        modalCreateOrder
    },
    mounted() {
        this.dateStart = moment().startOf('week').format('YYYY-MM-DD')
        this.dateEnd = moment().endOf('week').format('YYYY-MM-DD')
        this.update()
    },
    watch: {
        dateStart(){
            this.update()
        },
        dateEnd(){
            this.update()
        }
    },
    methods: {
        closeCreateModal(){
            this.showCreateOrder = false
            this.update()
            this.value = {}
        },
        async deleteOrder(){
            await Order.objects.delete(this.value)
            this.value = {}
            this.showDetails = false
            this.showAlert('Заказ удален')
            this.update()
        },
        editing(){
            this.showDetails = false
            this.showCreateOrder = true
        },
        async getLodge(){
            let lodgeList = (await Lodge.getList()).results            
            for(let x of lodgeList){
                let filter = {
                    lodges: x.id,
                    service_start: moment(this.dateStart, 'YYYY-MM-DD').subtract(7, 'days').format('YYYY-MM-DD'),
                    service_end: this.dateEnd
                }
                x.order_set = (await Order.getList(filter)).results
                this.getPlan(x.order_set, 10)
            }
            this.lodgeList = lodgeList
    
        },
        close(){
            this.showDetails = false
            this.value = {}
        },
        select(l){
            this.value = l
            this.showDetails = true
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
        getPlan(list, top){
            for(let i = 0; i < list.length; i++){
                for(let index = 0; index < list[i].services.length; index++){
                    if(list[i].services[index]){
                    let start  = moment(list[i].services[index].start_date);
                    
                    if (list[i].services[index].end_date){
                        const end = moment(list[i].services[index].end_date)
                        let duration = end.diff(start,'hours') 
                        let style =getStyle(this.dateStart,list[i].services[index].start_date,duration,top)
                        list[i].services[index].style = style
                        if(list[i].services[index].name == 'SN'){
                            list[i].services[index].style.top = '10px'            
                        }
                        else{
                            list[i].services[index].style.top = '40px'
                        }
                        }        
                    }    
                }
                
            }
        
        },
        async getSaunaListBlackSmith(){
            
            const url = "/api/order/?"
            let params = new URLSearchParams({
                lodges__lodge_id: '2',  
                service_start: moment(this.dateStart, 'YYYY-MM-DD').format('YYYY-MM-DD'),
                service_end: this.dateEnd               
            })
            const response = await (
                await fetch(
                    url + params
                )
            ).json();
            this.saunaListBlackSmith = response
            this.getPlan(this.saunaListBlackSmith,10)
        },
        update(){
            this.get_date_row()
            this.ganttStyle={width:this.dataRange.length*30+400+'px'}            
            this.getLodge()
            
        },
        get_date_row(){
            moment.locale('ru')
            let dateRang1 = []
            let hourRange = []
            let start  = moment(this.dateStart,'YYYY-MM-DD').toDate();
            let start1  = moment(this.dateStart,'YYYY-MM-DD');
            let end =  moment(this.dateEnd,'YYYY-MM-DD').toDate();                                   
            while(start <= end){
                for(let i = 0; i < 24; i++){
                const hour = {
                    hour: moment(start1).format('HH') + ':00'
                }
                hourRange.push(hour)
                let NewDate = moment(start1).add(1, 'h')
                start1 = NewDate
            }
            dateRang1.push([moment(start).format('DD.MM.YYYY'),24*COL_WIDTH+'px'])
            let newDate =(new Date(start))
                newDate.setDate(start.getDate() + 1);
                start = newDate; 
            }
            
            this.dataRange1 = dateRang1
            this.hourRange = hourRange                                              
        },
    }
}
</script>

<style scoped>
.alert-success{
    position: absolute;
    width: 1327px;
    top: 0;
}
.day-row{
    display: flex;
}
.table2{
    width: 1485px;
    overflow-x: auto;
    overflow-y: hidden;
    -ms-overflow-style: none;
    scrollbar-width: none;
}
.table2::-webkit-scrollbar {
    width: 0;
    height: 0;
}
.row-row{
    position: relative;
}
.container-table{
    width: 1485px;
}
.lh-1{
    line-height: 1;
}
.gantt-head {
    position: sticky;
    top: 0px;
    z-index: 100;
    background: white;
}
.gantt-cell-day{
    width:30px;

    padding: 0.15rem 0.1rem;
    text-align: center;
}
.gantt-cell-month{
    text-align:center;
    border:2px solid black
}
.gantt-cell{
    display: inline-block;
    border-left:1px solid #7b7a7a;
    border-top:1px solid;
    border-bottom:1px solid #7b7a7a;
    height:70px;
    min-width: 48px;

}
.order-cell{
    display: inline-block;
    border-left:1px solid #7b7a7a;
    border-top:1px solid;
    border-bottom:1px solid #7b7a7a;
    border-right: 1px solid #7b7a7a;
    height:70px;
    min-width: 48px;
}

.gantt-name.group{
    
    font-weight:500;
    padding:0.3rem;

    border-top:2px solid #7b7a7a;
}
.gantt-name.vehicle{
    padding-left:15px;
}
.gantt-row{
    white-space: nowrap;
    height:70px;
    position:relative
}
.gantt-name{
    padding-top: 20px;
    width:200px;
    float:left;
    overflow:hidden;
    font-size:1rem;
    font-weight: 600;
    padding-left: 10px;
}
.gantt-body{
    position:relative;
float: left;
}
.gantt-table{
    float:left;
}
.gantt-sauna{
    cursor: pointer;
    position:absolute;
    background: #f6bd5099;
    border:solid 1px;
    border-radius:5px;
    overflow: hidden;
}
.gantt-tub{
    cursor: pointer;
    position:absolute;
    background: #a5ccff99;
    border:solid 1px;
    border-radius:5px;
    overflow: hidden;
}
.gantt-task.gantt-tiket{
    background:#ffff00;
    border-radius:15px;
}

.gantt-task.gantt-memo{
    background:#12fff4;
    height:14px!important;
    border-radius:0px;
    opacity:0.2;
}




.gantt-task__task-name{
    position:absolute;
}
.gantt-task__progress{
    position:absolute;
    background-color:green;
    height:20px

}
.gantt-cell__weekend{
    background-color:#ffffca;
}
.gantt-head{
position: sticky;
top: 0px;
z-index:100;
background:white;
}

.workday-color-y{
    background:rgb(235, 244, 255) ;
}

.workday-color-mv{
    background: rgba(255,239,0,1);
}

.workday-color-k{
    background:rgb(156, 232, 165);
}

.workday-legend{
    display:flex
}
.workday-color-ot{
    background: rgb(255, 155, 0);
}

.workday-color-d{
    background: rgb(184, 184, 184)
}
.gantt-cell-day.group{
    background:#e3f8ff
}
.workday-box{
    height:20px;
    width:20px
}
</style>