from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from shortener import serializers, models as m
from rest_framework.response import Response
from rest_framework.views import APIView
from core.MainVariables import PublishedURL
from core.utils import generate_code

class ShortURLCreate(APIView):
  permission_classes = [permissions.AllowAny]
  def post(self, request):
    serializer = serializers.ShortURLCreate(data=request.data)
    if not serializer.is_valid():
      return Response({"status": False, "error": "validation_error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    validated_data = serializer.validated_data
    full_url = validated_data['url']
    try:
      obj, created = m.ShortURL.objects.get_or_create(full_url=full_url, short_code=generate_code(use_letters=True, use_mixed_case=True))
      return Response({"status": True, "message": "URL shortened successfully.", "short": f"{PublishedURL}/{obj.short_code}", "created": created}, status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({"status": False, "error": "server_error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
