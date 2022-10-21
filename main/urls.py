from django.urls import path
from .views import (good_details,
                    ShowGoodsView,
                    review_add,
                    about_us)

app_name = 'main'
urlpatterns = [
    path('', ShowGoodsView.as_view(), name='home'),
    path('test/', ShowGoodsView.as_view()),
    path('good/<good_id>', good_details, name='good_info'),
    path('reviews/', review_add, name='reviews'),
    path('about/', about_us, name='about_us')

]
