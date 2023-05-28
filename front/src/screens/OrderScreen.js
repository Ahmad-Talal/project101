import React, {useEffect} from 'react'
import {ListGroup,Card,Col,Row,Button} from 'react-bootstrap';
import { useDispatch,useSelector} from 'react-redux'

import Message from '../components/Message'
import {getOrderDetails, payOrder,shipOrder} from '../actions/orderActions'
import { ORDER_PAY_RESET, ORDER_SHIP_RESET } from '../constants/orderConstants';
import Loader from '../components/Loader';

const OrderScreen = ({match,history})=> {
    const orderId = match.params.unique

    const dispatch = useDispatch()

    const orderDetails = useSelector(state=>state.orderDetails)
    const {order,error,loading} = orderDetails
    
    const orderPay = useSelector(state=>state.orderPay)
    const {success} = orderPay
    const orderShip = useSelector(state=>state.orderShip)
    const {success:successC} = orderShip

    const userLogin = useSelector(state=>state.userLogin)
    const {userInfo} = userLogin

    if(!loading && !error){
        order.itemsPrice = order.orderItems.reduce((sum,val) => 
        sum + val.price*val.qty,0).toFixed(2)
    }
    
   
useEffect(() => {
    if (userInfo){
        if(!order ||success||successC||order._id !==Number(orderId)){
            dispatch(
                getOrderDetails(orderId)
            )}
            if(success)
            {
                dispatch({type:ORDER_PAY_RESET})
            }
            if(successC)
            {
                dispatch({type:ORDER_SHIP_RESET})
            }
    }
    else{
        history.push("/login")
    }
    
    }, [history,dispatch,order,success,successC,orderId,userInfo])


    const PayByCard = () =>{
        history.push('/stripe')
    }

    const Pay = () =>{
        dispatch(payOrder(orderId))
    }
    
    const Ship = () =>{
        dispatch(shipOrder(orderId))
    }
    return (
        <div>
        
        {loading && <Loader />}
        {error && <Message>{error}</Message>}
        
        {!loading && !error &&
        <div>
        <h1>ORDER:</h1>

        <Row>
            <Col md={8}>
            <ListGroup variant="flush">
                <ListGroup.Item>
                    <h2>Shipping</h2>
                    <p>
                        <strong>Name: </strong>{` ${order.user.name}`} <br></br>
                        <strong>Email: </strong>
                        <a href={`mailto:${order.user.email}`} >{order.user.email}</a>
                        <br></br>
                        <strong>Shipping: </strong>
                        {order.shippingAddress.address}{' '},
                        {order.shippingAddress.postalCode}{' '},
                        {order.shippingAddress.city}{' '},
                        {order.shippingAddress.country}
                    </p>
                </ListGroup.Item>
                
                
                {order.isDelivered ?(
                    <ListGroup.Item>
                    <Message variant='success'>Delivered on {order.deliveredAt.substring(0,10)}</Message>
                    </ListGroup.Item>)
                    :
                    (
                        <ListGroup.Item>
                    <Message variant='warning'>Not Delivered</Message>
                    </ListGroup.Item>)
                }
                    
                

                <ListGroup.Item>
                    <h2>Payment Method</h2>
                    <p>
                        <strong>Method: </strong>
                        {order.paymentMethod}{' '}
                    </p>
                </ListGroup.Item>

                <ListGroup.Item>
                {order.isPaid ?(
                    <Message variant='success'>Paid on {order.paidAt.substring(0,10)}</Message>)
                    :
                    (
                    <Message variant='warning'>Not Paid</Message>)
                }
                    
                </ListGroup.Item>
            </ListGroup>  
            </Col>

            <Col md={4}>
                <Card>
                    <h2 style={{textAlign:'center'}}>Order Summary</h2>
                    { order.orderItems.length === 0 ? 
                    <Message variant = 'dark'>Your cart is empty</Message> 
                    : <ListGroup vaiant='flush'>
                        <ListGroup.Item>
                            <Row>
                                <Col>
                                   <h>Items:</h> 
                                </Col>
                                <Col>${order.itemsPrice}</Col>
                            </Row>
                        </ListGroup.Item>

                        <ListGroup.Item>
                            <Row>
                                <Col>
                                   <h>Shipping:</h> 
                                </Col>
                                <Col>${order.shippingPrice}</Col>
                            </Row>
                        </ListGroup.Item>

                        <ListGroup.Item>
                            <Row>
                                <Col>
                                   <h>Tax:</h> 
                                </Col>
                                <Col>${order.taxPrice}</Col>
                            </Row>
                        </ListGroup.Item>

                        <ListGroup.Item>
                            <Row>
                                <Col>
                                   <h>Total:</h> 
                                </Col>
                                <Col>${order.totalPrice}</Col>
                            </Row>
                        </ListGroup.Item>
                    
                        {
                            error &&(
                                <ListGroup.Item>
                                 <Message variant='danger'>{error}</Message>
                                 </ListGroup.Item>)
                        }  
                        
                         {
                            order.seller_id !== userInfo.id && 
                            !order.isPaid &&

                            <Button 
                            type ='button' 
                            className='btn-block' 
                            onClick ={PayByCard}
                            >Pay it with credit card!!
                            </Button>
                        }  
                        {
                            order.seller_id !== userInfo.id &&(
                                <>
                                <br/><br/>
                                <Button 
                                type ='button' 
                                className='btn-block' 
                                >cash on delivery!!
                                </Button></>
                            )    
                            
                        }  
                        {
                            order.seller_id === userInfo.id &&    
                            <Button 
                            type ='button' 
                            className='btn-block' 
                            onClick ={Pay}
                            >click if the order has been paid!!
                            </Button>
                        }   
                        {
                        order.seller_id === userInfo.id &&(
                            <>
                            <br/><br/>
                            <Button 
                            type ='button' 
                            className='btn-block' 
                            onClick ={Ship}
                            >click if the order has been shipped!!
                            </Button></>
                        )    
                        
                        }  
                        
                    </ListGroup>
                 }  
                </Card>
            </Col>

        </Row>
        </div>
        }       
        </div>
    )
}

export default OrderScreen
