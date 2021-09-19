from rest_framework import serializers

from collect.models import Collect
from user_info.serializers import UserDescSerializer


class CollectSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')
    author = UserDescSerializer(read_only=True)

    article = serializers.HyperlinkedRelatedField(view_name='article-detail', read_only=True)
    article_id = serializers.IntegerField(write_only=True, allow_null=False, required=True)

    class Meta:
        model = Collect
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}
