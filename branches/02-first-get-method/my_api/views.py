from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MenuItems


# Create your views here.
@csrf_exempt
def menu_items(request):
    if request.method == 'GET':
        list_book = MenuItems.objects.all().values()
        return JsonResponse({"books": list(list_book)})
