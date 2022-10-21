from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from orders.models import Order, OrderItem
from main.models import Goods


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            errors = user_form.errors
    else:
        user_form = UserRegistrationForm()
        errors = None
    return render(request, 'account/register.html', {'user_form': user_form, 'errors': errors})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:home')
                else:
                    return render(request, 'account/login.html', {'form': form, 'value': 'Disabled account'})
            else:
                return render(request, 'account/login.html', {'form': form, 'value': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('main:home')


def account(request):
    user = str(request.user)
    orders = Order.objects.filter(username=user).values()
    user_info = User.objects.filter(username=user).values()
    orders_items = {}
    total_prices = {}
    for order in orders:
        order_id = order['id_order']
        ordersitems = OrderItem.objects.filter(order_id=order_id).values()
        products = {}
        total_price = 0
        for ordersitem in ordersitems:
            product_id = ordersitem['product_id']
            quantity = ordersitem['quantity']
            goods = Goods.objects.filter(id_good=product_id).values()
            for good in goods:
                good_name = good['name']
                good_price = good['price']
                main_image = good['main_image']
                products[product_id] = {'quantity': quantity,
                                        'price': good_price,
                                        'name': good_name,
                                        'main_image': main_image}
                total_price += quantity * good_price
        total_prices[order_id] = total_price
        orders_items[order_id] = products

    data = {'orders': orders, 'user_info': user_info, 'orders_items': orders_items, 'total_prices': total_prices}
    return render(request, 'account/account.html', data)
