from .models import Restaurant

def restaurant_info(request):
    if request.user.is_authenticated:
        restaurant = Restaurant.objects.filter(User=request.user).first()
        return {
            'my_restaurant': restaurant
        }
    return {'my_restaurant': None}
