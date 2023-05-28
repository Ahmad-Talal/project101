import {
   

    PLACE_ORDER_REQUEST,
    PLACE_ORDER_SUCCESS,
    PLACE_ORDER_FAIL,
    ORDER_RESET,
    
    ORDER_DETAILS_REQUEST,
    ORDER_DETAILS_SUCCESS,
    ORDER_DETAILS_FAIL,

    ORDER_PAY_REQUEST,
    ORDER_PAY_SUCCESS,
    ORDER_PAY_FAIL,
    ORDER_PAY_RESET,

    ORDER_SHIP_REQUEST,
    ORDER_SHIP_SUCCESS,
    ORDER_SHIP_FAIL,
    ORDER_SHIP_RESET,

    ALL_ORDERS_REQUEST,
    ALL_ORDERS_SUCCESS,
    ALL_ORDERS_FAIL,
    ALL_ORDERS_RESET,

} from '../constants/orderConstants'

export const orderPlaceReducer= (state={},action)=>{
    switch(action.type){
    case PLACE_ORDER_REQUEST:
    
    return {
        loading:true
    }
    
    case PLACE_ORDER_SUCCESS:
        return{
            loading:false,
            success:true,
             order:action.payload
            }
    
    case PLACE_ORDER_FAIL:
        return{
            loading:false, 
            error:action.payload
        } 
    case ORDER_RESET:
        return{}         
    
    default:
    return state

}
}


export const orderDetailsReducer= (state={loading:true, orderItems:[],shippingAddress:{}},action)=>{
    switch(action.type){
    case ORDER_DETAILS_REQUEST:
    
    return {
        ...state,
        loading:true
    }
    
    case ORDER_DETAILS_SUCCESS:
        return{
            loading:false,
            order:action.payload
            }
    
    case ORDER_DETAILS_FAIL:
        return{
            loading:false, 
            error:action.payload
        }      
    
    default:
    return state

}
}

export const orderPayReducer= (state={loading:true, orderItems:[],shippingAddress:{}},action)=>{
    switch(action.type){
    case ORDER_PAY_REQUEST:
    
    return {
        loading:true
    }
    
    case ORDER_PAY_SUCCESS:
        return{
            loading:false,
            success:true
            }
    
    case ORDER_PAY_FAIL:
        return{
            loading:false, 
            error:action.payload
        }      
    
    case ORDER_PAY_RESET:
        return{
              }  

    default:
    return state

}
}

export const orderShipReducer= (state={loading:true, orderItems:[],shippingAddress:{}},action)=>{
    switch(action.type){
    case ORDER_SHIP_REQUEST:
    
    return {
        loading:true
    }
    
    case ORDER_SHIP_SUCCESS:
        return{
            loading:false,
            success:true
            }
    
    case ORDER_SHIP_FAIL:
        return{
            loading:false, 
            error:action.payload
        }      
    
    case ORDER_SHIP_RESET:
        return{
              }  

    default:
    return state

}
}

export const allOrdersReducer= (state={orders:[]},action)=>{
    switch(action.type){
    case ALL_ORDERS_REQUEST:
    
    return {
        loading:true
    }
    
    case ALL_ORDERS_SUCCESS:
        return{
            loading:false,
            orders:action.payload
            }
    
    case ALL_ORDERS_FAIL:
        return{
            loading:false, 
            error:action.payload
        }      
    
    case ALL_ORDERS_RESET:
        return{
            orders:[]
}  

    default:
    return state

}
}