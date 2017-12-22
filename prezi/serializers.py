from rest_framework import serializers

from prezi.models import Creator, Prezi

class CreatorSerializer(serializers.ModelSerializer):
    profileUrl = serializers.URLField(max_length=200, min_length=None, allow_blank=False)

    class Meta:
        model = Creator
        fields = ('name', 'profile_url')


class PreziSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(input_formats=['iso-8601', '%B %d, %Y'])
    thumbnail = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    #creator = CreatorSerializer(read_only=True)

    class Meta:
        model = Prezi
        fields = ('id', 'title', 'created_on', 'thumbnail', 'creator')
