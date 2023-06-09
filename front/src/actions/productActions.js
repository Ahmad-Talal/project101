import {
    PRODUCT_LIST_REQUEST,
    PRODUCT_LIST_SUCCESS,
    PRODUCT_LIST_FAIL,

    PRODUCT_DETAILS_REQUEST,
    PRODUCT_DETAILS_SUCCESS,
    PRODUCT_DETAILS_FAIL,

    PRODUCT_DELETE_REQUEST,
    PRODUCT_DELETE_SUCCESS,
    PRODUCT_DELETE_FAIL
} 
from '../constants/productConstants';

import axios from 'axios'

export const listProducts=()=>async (dispatch)=>{

    try{
    dispatch({type:PRODUCT_LIST_REQUEST})
    const {data} =await axios.get('http://127.0.0.1:8000/api/products/')
    dispatch({type:PRODUCT_LIST_SUCCESS,
              payload:data})
        }
        catch(error)
        {   
            dispatch({type:PRODUCT_LIST_FAIL,
            payload:error.response && error.response.data.detail
            ?   error.response.data.detail 
            :   error.message,  
        })
        }
}


export const DetailedProduct=(id)=>async (dispatch)=>{
    try{
    dispatch({type:PRODUCT_DETAILS_REQUEST})
    const {data} =await axios.get(`http://127.0.0.1:8000/api/products/${id}`)
    dispatch({type:PRODUCT_DETAILS_SUCCESS,
              payload:data})
        }
        catch(error)
        {   
            dispatch({type:PRODUCT_DETAILS_FAIL,
            payload:error.response && error.response.data.detail
            ?   error.response.data.detail 
            :   error.message,  
        })
        }
}

export const deleteProduct=(id)=>async (dispatch,getState)=>{
    try{
    
        dispatch(
        {type:PRODUCT_DELETE_REQUEST}
        )

    const {
            userLogin :{userInfo} ,
    } = getState()

    const configuration = {
        headers : {
            'Content-type':'application/json',
            Authorization: `Bearer ${userInfo.token}`
        }
    }

    const {data} =await axios.delete(
        `http://127.0.0.1:8000/api/products/delete/${id}`,
        configuration
    )
    dispatch(
        {type:PRODUCT_DELETE_SUCCESS,
              payload:data}
              )
        }
        catch(error)
        {   
            dispatch({type:PRODUCT_DELETE_FAIL,
            payload:error.response && error.response.data.detail
            ?   error.response.data.detail 
            :   error.message,  
        })
        }
}