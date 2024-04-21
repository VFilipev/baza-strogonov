<template lang="pug">    
.row
    .col-md-2
        .card
            .card-body
                h4 Фильтр
                label(for="exampleFormControlInput1" class="form-label") Начало
                input(v-model="dateStart" class="form-control" type="date" name="" id="")
                br
                label(for="exampleFormControlInput1" class="form-label") Конец
                input(v-model="dateEnd" class="form-control" type="date" name="" id="")
                br
                h4 Статусы
                div(class="d-flex align-items-center")
                    div(class="line-legend" style="background: #ff0909a3")
                    div - Заказ с сайта
                div(class="d-flex align-items-center")
                    div(class="line-legend" style="background: #f6ff09a3")
                    div - Подтвержден
                div(class="d-flex align-items-center")
                    div(class="line-legend" style="background: #00ffc6d4")
                    div - Внесена предоплата
                div(class="d-flex align-items-center")
                    div(class="line-legend" style="background: #00ff27a3")
                    div - Оплачен 
                div(class="d-flex align-items-center")    
                    div(class="line-legend" style="background: #0984ffa3")
                    div - Завершен

    .col-md-10            
        b-alert(:show="dismissCountDown" variant="success") {{ alertText }}

        h2 Таблица заказов 
        div(class="container-table d-flex")
            div(class="table1")
                div(class="gantt-row")
                    div(class="order-cell gantt-name") Месяц
                div(class="gantt-row")
                    div(class="order-cell gantt-name") Название
                template(v-for="(header, index) in lodgeList")
                    div(v-if="header.avalible == true" class="gantt-row")
                        div(class="order-cell gantt-name" 
                        :style="style(header.name)"
                        @click="adaptingRow(header.name, index)") {{ header.name }}                    
            div(class="table2")
                div(class="gantt-row")
                    div(class="gantt-cell gantt-cell-month" v-for="cell in monthRange" :style="{width:cell[1]}")   {{cell[0]}}
                div(class="day-row")
                    div(class="gantt-cell gantt-cell-day" v-for="cell in dataRange" 
                    :class="cell.weekend?'gantt-cell__weekend':''"                    
                    )   {{cell.day}}
                div(class="row-row" v-for="(lodge, indexLodge) in lodgeList")
                    template(v-if="lodge.avalible == true")
                        div(class="gantt-row employee-row" :style="style(lodge.name)")
                            div(class="gantt-cell gantt-cell-day gantt-" v-for="(cell,index) in dataRange" 
                            :style="style(lodge.name)"                 
                            :class="{'gantt-cell__weekend':cell.weekend}") 
                        div(v-for="l in lodge.order_set" class="gantt-task gantt-plan" :style="l.order_lodge_set[0].style" @click="select(l)") 
                            div(class="lh-1" v-if="l.order_lodge_set[0].style") 
                                span() {{l.id}}


        button(class="btn btn-primary" @click="showCreateOrder = true") создать заказ
    modalDetailVue(:value="value" v-if="showDetails" @close="close()" @editing="editing()" @deleteOrder="deleteOrder()")
    modalCreateOrder(:orderProp="value ? value : ''" v-if="showCreateOrder" @close="closeCreateModal()" @closeModal="closeModal()")
                                                        
          
</template>

<script >
import modalDetailVue from '../components/modalDetailOrder.vue'
import modalCreateOrder from '../components/modalCreateOrder.vue'
import moment from 'moment-with-locales-es6';
// import localization from 'moment/locale/ru'
import { Order, Lodge } from '@/api'
import styleStatus from '../assets/styleStatus'

const COL_WIDTH = 48;
const TABLE_WIDTH = 0;
function getStyle(dateStart, start_date, duration, top, height) {
    let d = duration;
    let start = moment(start_date, 'YYYY-MM-DD');
    let shift = start.diff(dateStart, 'days')

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
    name: 'order-view',
    data: function () {
        return {
            alertText: '',
            dismissSecs: 3,
            dismissCountDown: 0,
            showDetails: false,
            showCreateOrder: false,
            value: null,
            dataRange: [],
            monthRange: [],
            dateStart: "2023-03-01",
            dateEnd: "2023-03-31",
            gantt_start: "2017-11-04",
            lodgeList: [],
            ganttStyle: {},
            planList: [],
            styleStatus,
            adapting_set: {},
            adaptive_list: {
                'Дом Гончара 1 этаж': 0,
                'Дом Кузнеца': 0,
                'Дом Мельника': 0,
                'Дом Охотников': 0,
                'Дом Рыбацкий': 0,
                'Дом Ткачихи': 0,
                'Дом Ямщика': 0,
            },
            count: 0
        }
    },
    components: {
        modalDetailVue,
        modalCreateOrder
    },
    mounted() {
        this.dateStart = moment().startOf('month').format('YYYY-MM-DD')
        this.dateEnd = moment().endOf('month').format('YYYY-MM-DD')        
        this.update()

    },
    computed: {

    },
    watch: {
        dateStart() {
            this.update()
        },
        dateEnd() {
            this.update()
        }
    },
    methods: {
        style(name) {
            if (this.adapting_set[name] == true) {
                return { height: `${35 * this.adaptive_list[name]}` + 'px' }
            }
            else { return {} }
        },
        toNumber(str) {
            if (str) {
                return str.substring(0, str.length - 2)
            }
        },
        calcTotalWidth(obj) {
            let left = this.toNumber(obj.left)
            let width = this.toNumber(obj.width)
            return +left + +width
        },
        calcAdaptive(name, indexLodge) {
            let count = 1
            const top = 10
            for (let i = 0; i < this.lodgeList[indexLodge].order_set.length - 1; i++) {
                if (this.lodgeList[indexLodge].order_set[i].order_lodge_set && this.lodgeList[indexLodge].order_set[i + 1].order_lodge_set) {
                    if (this.lodgeList[indexLodge].order_set[i].order_lodge_set[0].style) {
                        if (this.calcTotalWidth(this.lodgeList[indexLodge].order_set[i].order_lodge_set[0].style) > this.toNumber(this.lodgeList[indexLodge].order_set[i + 1].order_lodge_set[0].style?.left)) {
                            count += 1
                            this.lodgeList[indexLodge].order_set[i + 1].order_lodge_set[0].style.top = `${(count * top + 20) + ((count - 1) * top)}` + 'px'
                        }
                    }
                }
            }
            this.adaptive_list[name] = count
        },
        resetStyle(indexLodge) {
            for (let order of this.lodgeList[indexLodge].order_set) {
                if (order.order_lodge_set[0].style) {
                    order.order_lodge_set[0].style.top = '10px'
                }
            }
        },
        adaptingRow(name, indexLodge) {
            let tmp = !this.adapting_set[name]
            this.$set(this.adapting_set, name, tmp)
            if (this.adapting_set[name] == true) {
                this.calcAdaptive(name, indexLodge)
            }
            else {
                this.resetStyle(indexLodge)
            }
        },
        async deleteOrder() {
            await Order.delete(this.value)
            this.value = {}
            this.showDetails = false
            this.showAlert('Заказ удален')
            this.update()
        },
        async getLodge() {
            let params = { ordering: 'name' }
            let lodgeList = (await Lodge.getList(params)).results
            for (let x of lodgeList) {
                let filter = {
                    lodges: x.id,
                    search_start: moment(this.dateStart, 'YYYY-MM-DD').subtract(7, 'days').format('YYYY-MM-DD'),
                    search_end: this.dateEnd
                }
                x.order_set = (await Order.getList(filter)).results
                this.getPlan(x.order_set, 10)
            }
            this.lodgeList = lodgeList
        },
        closeCreateModal() {
            this.showCreateOrder = false
            this.update()
            this.value = {}
        },
        close() {
            this.showDetails = false
            this.value = {}
        },
        editing() {
            this.showDetails = false
            this.showCreateOrder = true
        },
        showAlert(text) {
            this.alertText = text
            this.dismissCountDown = this.dismissSecs
            this.dismissSecs += 1
        },
        closeModal() {
            this.value = {}
            this.showCreateOrder = false
            this.showAlert('Заказ создан')
            this.update()
        },
        select(l) {
            this.value = l
            this.showDetails = true
        },
        getBackground(item) {
            let bG = ''
            styleStatus.forEach(function (i) {
                if (i.status === item) {
                    bG = i.background
                }
            });
            return bG
        },
        getPlan(list, top) {

            for (let i = 0; i < list.length; i++) {
                for (let index = 0; index < list[i].order_lodge_set.length; index++) {
                    let start = moment(list[i].order_lodge_set[index].start_date);

                    if (list[i].order_lodge_set[index].end_date) {
                        const end = moment(list[i].order_lodge_set[index].end_date)
                        let duration = end.diff(start, 'days') + 1

                        let style = getStyle(this.dateStart, list[i].order_lodge_set[index].start_date, duration, top)
                        if (style) {
                            style.background = this.getBackground(list[i].status)
                        }
                        list[i].order_lodge_set[index].style = style
                    }
                }
            }
        },

        update() {
            this.getLodge()
            this.get_date_row()
            this.ganttStyle = { width: this.dataRange.length * 30 + 400 + 'px' }
        },
        get_date_row() {
            moment.locale('ru')
            let dateRang = []
            let monthRang = []
            let start = moment(this.dateStart, 'YYYY-MM-DD').toDate();
            let end = moment(this.dateEnd, 'YYYY-MM-DD').toDate();
            let daysCount = 0
            while (start <= end) {

                const day = {
                    month: moment(start).format('MM'),
                    day: moment(start).format('DD') + moment(start).format('dd'),
                    weekend: (start.getDay() == 6 || start.getDay() == 0),
                }
                dateRang.push(day)
                daysCount++;
                let newDate = (new Date(start))
                newDate.setDate(start.getDate() + 1);
                if (start.getMonth() != newDate.getMonth()) {
                    monthRang.push([moment(start).format('MMM'), daysCount * COL_WIDTH + 'px'])
                    daysCount = 0

                }

                start = newDate;

            }
            monthRang.push([moment(start).format('MMM'), daysCount * COL_WIDTH + 'px'])
            this.dataRange = dateRang
            this.monthRange = monthRang

        },

    }
}
</script>

<style>
.line-legend {
    width: 45px;
    height: 15px;
    background: #00ffc6d4;
    border: solid 1px;
    border-radius: 5px;
    margin-right: 5px;
}

.row {
    margin-right: 0;
}

.alert-success {
    position: absolute;
    width: 1327px;
    top: 0;
}

.day-row {
    display: flex;
}

.table2 {
    width: 1553px;
    overflow-x: auto;
    overflow-y: hidden;
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.table2::-webkit-scrollbar {
    width: 0;
    height: 0;
}

.row-row {
    position: relative;
}

.container-table {
    width: 1735px;
}

.lh-1 {
    line-height: 1;
}

.gantt-head {
    position: sticky;
    top: 0px;
    z-index: 100;
    background: white;
}

.gantt-cell-day {
    width: 30px;

    padding: 0.15rem 0.1rem;
    text-align: center;
}

.gantt-cell-month {
    text-align: center;
    border: 2px solid black
}

.gantt-cell {
    display: inline-block;
    border-left: 1px solid #7b7a7a;
    border-top: 1px solid;
    border-bottom: 1px solid #7b7a7a;
    height: 35px;
    min-width: 48px;

}

.order-cell {
    display: inline-block;
    border-left: 1px solid #7b7a7a;
    border-top: 1px solid;
    border-bottom: 1px solid #7b7a7a;
    border-right: 1px solid #7b7a7a;
    height: 35px;
    min-width: 48px;
}

.gantt-name.group {

    font-weight: 500;
    padding: 0.3rem;

    border-top: 2px solid #7b7a7a;
}

.gantt-name.vehicle {
    padding-left: 15px;
}

.gantt-row {
    white-space: nowrap;
    height: 35px;
    position: relative
}

.gantt-name {
    padding-top: 5px;
    width: 200px;
    float: left;
    overflow: hidden;
    font-size: 1rem;
    font-weight: 600;
    padding-left: 10px;
}

.gantt-body {
    position: relative;
    float: left;
}

.gantt-table {
    float: left;
}

.gantt-task {
    cursor: pointer;
    position: absolute;
    background: #a5ccff99;
    border: solid 1px;
    border-radius: 5px;
    overflow: hidden;
}

.gantt-task.gantt-tiket {
    background: #ffff00;
    border-radius: 15px;
}

.gantt-task.gantt-memo {
    background: #12fff4;
    height: 14px !important;
    border-radius: 0px;
    opacity: 0.2;
}




.gantt-task__task-name {
    position: absolute;
}

.gantt-task__progress {
    position: absolute;
    background-color: green;
    height: 20px
}

.gantt-cell__weekend {
    background-color: #ffffca;
}

.gantt-head {
    position: sticky;
    top: 0px;
    z-index: 100;
    background: white;
}

.workday-color-y {
    background: rgb(235, 244, 255);
}

.workday-color-mv {
    background: rgba(255, 239, 0, 1);
}

.workday-color-k {
    background: rgb(156, 232, 165);
}

.workday-legend {
    display: flex
}

.workday-color-ot {
    background: rgb(255, 155, 0);
}

.workday-color-d {
    background: rgb(184, 184, 184)
}

.gantt-cell-day.group {
    background: #e3f8ff
}

.workday-box {
    height: 20px;
    width: 20px
}</style>
