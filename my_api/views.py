import json
from django.db import IntegrityError
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
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
            return JsonResponse({model_to_dict(item)}, status=200)

        case 'PUT':
            try:
                post_dict = json.loads(request.body)
                for key, value in post_dict.items():
                    setattr(item, key, value)
                item.save()
            except Exception as e:
                return JsonResponse({'message': f'Must have all fields {e}'},
                                    status=401)

            return JsonResponse({f"Successfully update id {pk}": model_to_dict(item)}, status=201)

        case 'PATCH':
            post_dict = json.loads(request.body)
            item.title = post_dict.get("title", item.title)
            item.price = post_dict.get("price", item.price)
            item.featured = post_dict.get("featured", item.featured)
            item.save()

            return JsonResponse({f"Successfully partial update id {pk}": model_to_dict(item)}, status=201)

        case 'DELETE':
            item.delete()
            item.pk = pk
            return JsonResponse({f"Successfully delete id {pk}": model_to_dict(item)}, status=200)
