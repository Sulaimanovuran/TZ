from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from sample.models import Scroll, Date
from sample.serializers import ScrollSerializer, DateSerializer, DateSerializer2


class ScrollView(ModelViewSet):
    queryset = Scroll.objects.all()
    serializer_class = ScrollSerializer


class DateView(ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer2

@api_view(['GET'])
def get_employee(request):
    try:
        task = Date.objects.filter(date=request.data['date'])
        serializer = DateSerializer(task, many=True)
        return Response(serializer.data)
    except KeyError:
        return Response('Введите дату!')