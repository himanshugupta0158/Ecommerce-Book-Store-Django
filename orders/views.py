from account.models import Address
from basket.basket import Basket
from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":

        order_key = request.POST.get("order_key")
        user_id = request.user.id
        baskettotal = basket.get_total_price()
        address = Address.objects.get(customer=user_id)
        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user_id=user_id,
                full_name=request.user.name,
                address1=address.address_line,
                address2=address.address_line2,
                total_paid=baskettotal,
                order_key=order_key,
            )
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"]
                )

        response = JsonResponse({"success": "Return something"})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
