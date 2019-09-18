from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JumiaItem, PriceLog
from core.management.commands.run_crawler import run_crawler
# Create your views here.


@api_view(['POST'])
def handle_start_crawler(request):

    run_crawler()

    return Response({'status': 'success'})    


@api_view(['POST'])
def handle_item_post(request):
    item_obj = { k: v for k,v in request.data.items()}
    amount = item_obj.pop('price')
    
    print(item_obj, '\n\n\n')
    queryset = JumiaItem.objects.filter(sku=item_obj['sku'])
    
    
    if (queryset.exists()):
        item_instance = queryset[0]
        item_instance.latest_price = amount
        item_instance.save()

    else:
        item_instance = JumiaItem.objects.create(**item_obj, latest_price=amount)

    PriceLog.objects.create(amount=amount, item=item_instance)    

    # delete other logs asides the 5 most recent
    # price_logs = PriceLog.objects.filter().order_by('-date')[:5]
    # PriceLog.objects.exclude(pk__in=price_logs).delete()

    print(item_obj)
    
    return Response({'status': 'success'})


# use this to limit the number of prices to 5 at most
# https://stackoverflow.com/questions/1851197/django-delete-all-but-last-five-of-queryset
