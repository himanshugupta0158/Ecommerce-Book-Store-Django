from django.urls import path
from . import views

# matching up with namespace in core.urls path of this urls.py
app_name = 'store'

urlpatterns = [
    path("", views.all_products, name="all_products"),
# <datatype : nameofreference(variable)>
    path("item/<slug:slug>", views.product_detail, name="product_detail"),
]
