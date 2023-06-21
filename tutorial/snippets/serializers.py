from rest_framework import serializers
from snippets.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICE
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet #it specifies that the serializer should be associated with the Snippet model
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner'] #it specifies that fields should be included when serializing Snippet objects.
        owner = serializers.ReadOnlyField(source = 'owner.username')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset = Snippet.objects.all())
    class Meta:
        model = User
        fields = ['id','username','snippets']