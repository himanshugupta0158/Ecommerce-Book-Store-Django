from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = "payment"

urlpatterns = [
    path("", views.BasketView, name="basket"),
    path("orderplaced/", views.order_placed, name="order_placed"),
    path("error/", views.TemplateView.as_view(template_name="payment\error.html"), name="error"),
    path("webhook/", views.stripe_webhook),
]
