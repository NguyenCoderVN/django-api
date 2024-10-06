import json

from django.db import IntegrityError
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MenuItems


# Create your views here.
@csrf_exempt
def menu_items(request):
    if request.method == 'GET':
        list_book = MenuItems.objects.all().values()
        return JsonResponse({"books": list(list_book)})
    elif request.method == 'POST':
        post_dict = json.loads(request.body)
        title = post_dict["title"]
        price = post_dict["price"]
        featured = post_dict["featured"]
        menu_item = MenuItems(title=title, price=price, featured=featured)
        try:
            menu_item.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        return JsonResponse(model_to_dict(menu_item), status=201)
