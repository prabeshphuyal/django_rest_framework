from rest_framework import serializers
from snippets.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICE
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer ):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name = 'snippet-highlight',format='html')

    class Meta: 
        model = Snippet #it specifies that the serializer should be associated with the Snippet model
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']#it specifies that fields should be included when serializing Snippet objects.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name = 'snippet-detail',ready_only=True)
    class Meta:
        model = User
        fields = ['id','username','snippets']