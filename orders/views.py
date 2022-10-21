import datetime

from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            username = str(request.user)
            order = Order(username=username,
                          first_name=cd['first_name'],
                          last_name=cd['last_name'],
                          email=cd['email'],
                          address=cd['address'],
                          postal_code=cd['postal_code'],
                          city=cd['city'],
                          created=datetime.datetime.now(),
                          updated=datetime.datetime.now())
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})
