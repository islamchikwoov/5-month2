from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Reviews
from movie_app.serializer import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorCreateUpdateSerializer,\
    MovieCreteUpdateSerializer, ReviewCreateUpdateSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        """LIST"""
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        """CREATE"""
        serializer = DirectorCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'message': 'director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = DirectorCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieCreteUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        directors_id = request.data.get('directors_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration,
                                     directors_id=directors_id)
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'message': 'Movie is not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = MovieCreteUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.directors_id = request.data.get('directors_id')
        movie.save()
        return Response(data=MovieSerializer(movie).data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars =request.data.get('stars')
        review = Reviews.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Reviews.objects.get(id=id)
    except Reviews.DoesNotExist:
        return Response(data={'message': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewCreateUpdateSerializer
        serializer.is_valid(raise_exception=True)
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def movie_reviews_api_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_movie_api_view(request):
    director = Director.objects.all()
    movies = director.movie_director.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)








