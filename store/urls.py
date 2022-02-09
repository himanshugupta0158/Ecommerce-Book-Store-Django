from django.urls import path

from . import views

# matching up with namespace in core.urls path of this urls.py
app_name = 'store'

urlpatterns = [
    path("", views.product_all, name="product_all"),
    # <datatype : NameOfReference(variable)>
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("search/<slug:category_slug>/", views.category_list, name="category_list"),
]
