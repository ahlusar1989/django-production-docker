from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


# Rather than write multiple views we're grouping together all the common behavior 
# into classes called ViewSets.

# We can easily break these down into individual views if we need to, 
# but using viewsets keeps the view logic nicely organized as well as being very concise

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')