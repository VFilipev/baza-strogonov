export const lodgeUrl= '/api/lodge/'
export const serviceUrl= '/api/services/'
export const orderUrl= '/api/order/'
export const specialPriceUrl= '/api/specialPrice/'
export const priceUrl= '/api/price/'
export const commentUrl= '/api/comment/'

import axios from 'axios'

function toURLParams(filters){
    let params = new URLSearchParams();
    for (let f in filters){
        if (Array.isArray(filters[f])){
            for (let p of filters[f]){
                if (p){
                    if(p.id){
                        params.append(f,p.id);
                    }else{
                        params.append(f,p);
                    }
                }
            }
        }else if (filters[f] && filters[f].id){
            params.append(f,filters[f]['id'])

        }else{
                if (filters[f] !=undefined){
            params.append(f,filters[f]);
                }

        }
    }
    return params
}

async function _save(url,obj){
    let response 
    if (obj.id){
         response = await axios.patch(url+obj.id+'/',obj)
    }else{
         response = await axios.post(url,obj)
    }
    return response.data
}

async function _delete(url,obj){
    let response 
    if (obj.id){
        response = await axios.delete(url+obj.id+'/',obj)
    }
    
    return response
}
async function _getList(url,filter,params={}){
    const response = await axios.get(url+'?'+toURLParams(filter),params)
    return response.data
}
async function _getById(url,id){
    const response = await axios.get(url+id+'/')
    return response.data
}

export async function getOrderList(filter){
    return _getList(orderUrl,filter)
}

function apiConstructor(apiUrl){
    return {
        async save(obj){
            return _save(apiUrl,obj)
        },
        async getById(obj){
            return _getById(apiUrl,obj)
        },
        async getList(filter,params={}){
            return _getList(apiUrl,filter,params)
        },
        async delete(obj){
            return _delete(apiUrl,obj)   
        }
    
    }
}

export let Lodge = apiConstructor(lodgeUrl)
Lodge.get_available_house = async function(filter){
    return (await axios.get(lodgeUrl + "get_free_lodge/?" + toURLParams(filter)))
}
export let Order = apiConstructor(orderUrl)
Order.last = async()=>{
    const response = await axios.get(orderUrl+'last/')
    return response
}

export let Service = apiConstructor(serviceUrl)
export let SpecialPrice = apiConstructor(specialPriceUrl)
export let Price = apiConstructor(priceUrl)
export let Comment = apiConstructor(commentUrl)