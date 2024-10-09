import json
from json import JSONDecodeError
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from .models import MenuItems
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def menu_items(request):
    match request.method:
        case 'GET':
            items = MenuItems.objects.all().values()
            return Response({"books": list(items)})

        case 'POST':
            try:
                post_dict = json.loads(request.body)
                title = post_dict["title"]
                price = post_dict["price"]
                featured = post_dict["featured"]
                item = MenuItems(title=title, price=price, featured=featured)
                item.save()
            except JSONDecodeError as e:
                return Response({"JSONDecodeError": str(e)})
            except KeyError:
                return Response(
                    data={'KeyError': f'Json payload must have all fields'})
            except ValidationError as e:
                return Response({'ValidationError': f'{e}'})

            return Response(model_to_dict(item), status=201)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def menu_item(request, pk):
    match request.method:
        case 'GET':
            try:
                item = MenuItems.objects.get(pk=pk)
                dict_items = model_to_dict(item)
            except MenuItems.DoesNotExist as e:
                return Response({'message': f'{e}'}, status=500)

            return Response(dict_items, status=200)
        case 'PUT':
            try:
                item = MenuItems.objects.get(pk=pk)
                dict_put = json.loads(request.body)
                for key in model_to_dict(item):
                    if key != 'id':
                        setattr(item, key, dict_put[key])
                item.save()
            except MenuItems.DoesNotExist as e:
                return Response({'message': f'{e}'}, status=500)
            except JSONDecodeError as e:
                return Response({"JSONDecodeError": str(e)})
            except KeyError:
                return Response(
                    data={'KeyError': f'Json payload must have all fields'})
            except ValidationError as e:
                return Response({'ValidationError': f'{e}'})

            return Response(
                {f"Successfully update id {pk}": model_to_dict(item)},
                status=201)

        case 'PATCH':
            try:
                item = MenuItems.objects.get(pk=pk)
                dict_patch = json.loads(request.body)
                for key, value in dict_patch.items():
                    setattr(item, key, value)
                item.save()
            except MenuItems.DoesNotExist as e:
                return Response({'message': f'{e}'}, status=500)
            except JSONDecodeError as e:
                return Response({"JSONDecodeError": str(e)})
            except ValidationError as e:
                return Response({'ValidationError': f'{e}'})

            return Response(
                {f"Successfully partial update id {pk}": model_to_dict(item)},
                status=201)

        case 'DELETE':
            try:
                item = MenuItems.objects.get(pk=pk)
                item.delete()
                item.pk = pk
            except MenuItems.DoesNotExist as e:
                return Response({'DoesNotExist': f'{e}'}, status=404)

            return Response(
                {f"Successfully delete id {pk}": model_to_dict(item)},
                status=200)
