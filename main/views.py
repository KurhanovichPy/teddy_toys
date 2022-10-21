import datetime

from django.shortcuts import render
from .forms import ReviewForm
from .models import Gallery, Goods, Review
from django.views.generic import ListView
from cart.forms import CartAddProductForm


def good_details(request, good_id):
    goods = Goods.objects.filter(id_good=good_id)
    photos = Gallery.objects.filter(good=good_id)
    counter = range(1, len(photos) + 1)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/good_info.html', {'goods': goods,
                                                   'photos': photos,
                                                   'counter': counter,
                                                   'cart_product_form': cart_product_form})


def review_add(request):
    reviews = Review.objects.all()
    user = str(request.user)
    errors = None
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print('if')
        if form.is_valid():

            if user == 'AnonymousUser':
                user = 'Aноним'
                error = 'Необходимо зарегистрироваться'
                errors = {"error": error}
            else:
                mark = request.POST.get('rating', 0)
                text = form.cleaned_data
                date = datetime.datetime.now()
                review = Review.objects.create(user=user, body=text['body'], mark=mark, date=date)
                review.save()
    else:
        form = ReviewForm()
        if user == 'AnonymousUser':
            user = 'Aноним'
    datas = {'errors': errors,
             'reviews': reviews,
             'form': form,
             'user': user
             }
    return render(request, 'main/review.html', datas)


class ShowGoodsView(ListView):
    model = Goods
    template_name = 'main/index.html'
    context_object_name = 'goods'
    paginate_by = 4


def about_us(request):
    return render(request, 'main/about.html')
