from cart.cart import Cart


def username(request):
    user = str(request.user)
    if user == 'AnonymousUser':
        user = 'Аноним'
    return {'cont_username': user}


def count_goods_in_cart(request):
    cart = Cart(request).cart
    count_of_goods = len(cart)
    return {'count_of_goods': count_of_goods}
