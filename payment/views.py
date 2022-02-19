import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket

stripe.api_key = "sk_test_51KT2Q7SGWWpTwqWDyc9jCgnVygntbKBgrD3Hh8LayH2H2toyJwkLUDdYUik7aDKFV0DtQpshpjSYJYtAIVtFSJnJ00Nv3uCI9K"


@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace(".", "")
    total = int(total)

    intent = stripe.PaymentIntent.create(
        amount=total, currency="gbp", metadata={"userid": request.user.id}
    )

    return render(request, "payment/home.html", {"client_secret": intent.client_secret})
