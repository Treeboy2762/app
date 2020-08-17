from rest_framework.viewsets import ModelViewSet

from .models import Movie
from .serializers import MovieSerializer


class MoviesViewSet(ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer