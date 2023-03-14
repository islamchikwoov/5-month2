from rest_framework import serializers
from .models import Director, Movie, Reviews
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)





class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['text', 'stars', 'movie']




class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    movie_id = serializers.IntegerField(required=True)
    stars = serializers.IntegerField(required=False)


class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)
#    directors = DirectorSerializer()
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'directors', 'movie_reviews']

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = ['id', 'name', 'movie_count']



class MovieCreteUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True, max_length=10000)
    duration = serializers.IntegerField()
    directors = serializers.IntegerField()


    def validate_movie_id(self, movie_reviews):
        try:
            Movie.objects.get(id=movie_reviews)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exists!')
        return movie_reviews




