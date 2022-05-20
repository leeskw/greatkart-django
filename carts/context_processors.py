from accounts.views import activate
from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user) # not working
                """solution: https://stackoverflow.com/questions/42934970/django-error-cannot-resolve-keyword-user-into-field-choices-are
                Django Error: Cannot resolve keyword 'user' into field. choices are
                ===================================================================
                """
                # cart_items = CartItem.objects.all().filter(pk=request.user.pk)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
