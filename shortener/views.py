from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from .models import Recipe
from .serializers import RecipeSerializer, CreateReportSerializer
from authentication.models import Users   # <-- custom user model

# -----------------------
# Community Recipes API
# -----------------------
class CommunityRecipesAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [JSONParser]

    def get(self, request, format=None):
        qs = Recipe.objects.all()
        serializer = RecipeSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(author=request.user)
            else:
                serializer.save(author=None)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------
# User Reports API (PDF)
# -----------------------
class UserReportAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def post(self, request, id, format=None):
        user = get_object_or_404(Users, pk=id)
        serializer = CreateReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        options = serializer.validated_data

        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        title = options.get("title") or f"Report for {user.username}"
        p.setFont("Helvetica-Bold", 16)
        p.drawString(72, 800, title)

        p.setFont("Helvetica", 12)
        p.drawString(72, 780, f"User: {user.username} (ID {user.id})")
        p.drawString(72, 760, f"Email: {user.email}")

        y = 740
        if options.get("include_recipes"):
            p.drawString(72, y, "Recent Recipes:")
            y -= 20
            for r in Recipe.objects.all()[:5]:
                p.drawString(90, y, f"- {r.title}")
                y -= 15

        p.showPage()
        p.save()
        buffer.seek(0)

        filename = f"user_{user.id}_report.pdf"
        return FileResponse(buffer, as_attachment=True, filename=filename)
    