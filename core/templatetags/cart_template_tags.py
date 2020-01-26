from django import template
from core.models import Order
from core.models import UserProfile

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0


@register.filter
def total_amount(user):
    if user.is_authenticated:
        qs = UserProfile.objects.filter(user=user)
        # print(qs)
        if qs.exists():
            return qs[0].total_amt
    return 0


@register.filter
def tweet(user):
    if user.is_authenticated:
        qs = UserProfile.objects.filter(user=user)
        # print(qs)
        if qs.exists():
            return qs[0].twitter
    return 0
