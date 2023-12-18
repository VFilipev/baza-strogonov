import { defineStore } from 'pinia'

export const useOrderStore = defineStore('orderStore', {
  state: () => ({
    customer: '',
    cost:'',
    email: '',
    phone: '',
    orderlodge_set: [],
    services_set: [],
    products_set: [],
    start_date: '',
    end_date: ''
  }),
  actions:{
    changeCustomer(newName){
      this.customer = newName
    }
  },
  // persist: true,
  
})
