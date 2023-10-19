from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def upload(request, format=None):
    return Response({}, status=status.HTTP_201_CREATED)
