import json
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .models import UploadImageTest
from .serializers import QuizSerializer
from .serializers import ImageSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)



class ImageViewSet(ListAPIView):
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = UploadImageTest.objects.create(image=file)
        return HttpResponse(json.dumps({'message':"Uploaded"}), status=200)