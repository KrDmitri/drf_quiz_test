from django.urls import path, include
from .views import helloAPI, randomQuiz, ImageViewSet

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
    path("upload/", ImageViewSet.as_view(), name='upload'),
]
