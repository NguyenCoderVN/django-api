import json
from json import JSONDecodeError
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from .models import MenuItems
from rest_framework.response import Response
from rest_framework.decorators import APIView


class MenuItemList(APIView):

    @staticmethod
    def get(request):
        items = MenuItems.objects.all().values()

        return Response({"books": list(items)})

    @staticmethod
    def post(request):
        try:
            post_dict = json.loads(request.body)
            title = post_dict["title"]
            price = post_dict["price"]
            featured = post_dict["featured"]
            item = MenuItems(title=title, price=price, featured=featured)
            item.save()
        except JSONDecodeError as e:
            return Response({"Json payload error": str(e)})
        except KeyError:
            return Response(
                data={'message': f'Json payload must have all fields'})
        except ValidationError as e:
            return Response({e.code: f'{e}'})

        return Response(model_to_dict(item), status=201)


class MenuItem(APIView):

    @staticmethod
    def get(request, pk):
        try:
            item = MenuItems.objects.get(pk=pk)
            dict_items = model_to_dict(item)
        except MenuItems.DoesNotExist as e:
            return Response({'message': f'{e}'}, status=500)

        return Response(dict_items, status=200)

    @staticmethod
    def put(request, pk):
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
            return Response({str(e)}, status=500)
        except KeyError:
            return Response(
                data={'message': f'Json payload must have all fields'},
                status=500)
        except ValidationError as e:
            return Response(
                data={'message': f'{e}'},
                status=500)

        return Response(
            {f"Successfully update id {pk}": model_to_dict(item)},
            status=201)

    @staticmethod
    def patch(request, pk):
        try:
            item = MenuItems.objects.get(pk=pk)
            dict_patch = json.loads(request.body)
            for key, value in dict_patch.items():
                setattr(item, key, value)
            item.save()
        except MenuItems.DoesNotExist as e:
            return Response({'message': f'{e}'}, status=500)
        except JSONDecodeError as e:
            return Response({str(e)}, status=500)

        return Response(
            {f"Successfully partial update id {pk}": model_to_dict(item)},
            status=201)

    @staticmethod
    def delete(request, pk):
        try:
            item = MenuItems.objects.get(pk=pk)
            item.delete()
            item.pk = pk
        except MenuItems.DoesNotExist as e:
            return Response({'message': f'{e}'}, status=500)

        return Response(
            {f"Successfully delete id {pk}": model_to_dict(item)},
            status=200)
