from django.shortcuts import render
from django.views.generic import ListView

from zinzi.restaurants.models import Restaurant


def restaurnt_list_view(request):
    q = request.GET.get('q', None)
    if q:
        restaurant = Restaurant.get_searched_list(q=q)
        return render(request, 'restaurant/list.html', {'restaurant_list': restaurant})

    filter_fileds = {
        'restaurant_type': request.GET.get('type', None),
        'average_price': request.GET.get('price', None),
        'district': request.GET.get('district', None),
    }
    restaurant = Restaurant.get_filtered_list(filter_fields=filter_fileds)
    return render(request, 'restaurant/list.html', {'restaurant_list': restaurant})

