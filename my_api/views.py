import json

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MenuItems


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
        item = MenuItems(title=title, price=price, featured=featured)
        try:
            item.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

        return JsonResponse(model_to_dict(item), status=201)


@csrf_exempt
def menu_item(request, pk):
    try:
        item = MenuItems.objects.get(pk=pk)
        dict_item = model_to_dict(item)
    except Exception as e:
        return JsonResponse({'message': f'{e}'}, status=404)

    match request.method:
        case 'GET':
            return JsonResponse(dict_item, status=200)

        case 'PUT':
            dict_put = json.loads(request.body)
            for key in dict_item:
                if key != 'id':
                    try:
                        setattr(item, key, dict_put[key])
                    except KeyError:
                        return JsonResponse(
                            data={'message': f'Json payload must have all fields'},
                            status=401)
            try:
                item.save()
            except ValidationError as e:
                return JsonResponse(
                    data={'message': f'{e}'},
                    status=400)

            return JsonResponse({f"Successfully update id {pk}": model_to_dict(item)}, status=201)

        case 'PATCH':
            dict_patch = json.loads(request.body)
            try:
                for key, value in dict_patch.items():
                    setattr(item, key, value)
                item.save()
            except Exception as e:
                return JsonResponse({'message': f'{e}'}, status=401)

            return JsonResponse({f"Successfully partial update id {pk}": model_to_dict(item)}, status=201)

        case 'DELETE':
            item.delete()
            item.pk = pk
            return JsonResponse({f"Successfully delete id {pk}": model_to_dict(item)}, status=200)
