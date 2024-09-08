from .models import PostImage
from users.models import Artist
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from art.serializers import PostSerilizer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .utils.utils import upload_image

class PostViewSet(generics.ListCreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostSerilizer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
            image_file = self.request.data['post_image']
            post_data = serializer.validated_data.copy()
            post_data['uploaded_by'] = Artist.objects.get(id=self.request.data['uploaded_by'])
            uploaded, post_data['image_url'] = upload_image(image_file)
            if not uploaded:
                return JsonResponse({"error": post_data['image_url']}, status=400)
            serializer.save(**post_data)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_detail(request, pk):
    try:
        artis = PostImage.objects.get(pk=pk)
    except PostImage.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        try:
            serializer = PostSerilizer(artis)
            return JsonResponse(serializer.data)
        except Exception as e:
            return JsonResponse({"error":f"Something went wrong!! Erro --{e}"}, status=400)  

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            serializer = PostSerilizer(artis, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error":f"Something went wrong!! Erro --{e}"}, status=400)  

    elif request.method == 'DELETE':
        try:
            artis.delete()
            return HttpResponse(status=204)
        except Exception as e:
            return JsonResponse({"error":f"Something went wrong!! Erro --{e}"}, status=400)  