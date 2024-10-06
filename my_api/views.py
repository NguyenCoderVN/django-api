from django.db import IntegrityError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MenuItems


# Create your views here.
@csrf_exempt
def menu_items(request):
    if request.method == 'GET':
        list_book = MenuItems.objects.all().values()
        return JsonResponse({"books": list(list_book)})
    elif request.method == 'POST':
        title = request.POST.getlist('title')
        price = request.POST.getlist('price')
        featured = request.POST.getlist('featured')
        menu_item = MenuItems(title=title, price=price, featured=featured)
        try:
            menu_item.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        return JsonResponse(model_to_dict(menu_item), status=201)
