from .models import Artist
from rest_framework import viewsets, generics
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from users.serializers import ArtistSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def artists_list(request):
    try:
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({"error":f"Something went wrong!! Erro --{e}"}, status=400)

    
@api_view(['GET','PUT','DELETE','OPTIONS'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def artist_detail(request, pk):
    try:
        artis = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return JsonResponse({"error": "Erro -- No Artist found"}, status=404)

    if request.method == 'GET':
        try:
            serializer = ArtistSerializer(artis)
            return JsonResponse(serializer.data)
        except Exception as e:
            return JsonResponse({"error":f"Something went wrong!! Erro --{e}"}, status=400)

    elif request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            serializer = ArtistSerializer(artis, data=data)
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
        

class UserViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['DELETE','OPTIONS'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def delet_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return JsonResponse({"data" : f"user - {user.username} delete successful"}, status=400)
    except Exception as e:
        return JsonResponse({"error" : f"Something went wrong!! Erro --{e}"}, status=400)


# User Registration
@api_view(['POST','OPTIONS'])
def register_artist(request):
    try:
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    except Exception as e:
        return JsonResponse({"error" : f"Something went wrong!! Erro --{e}"}, status=400)