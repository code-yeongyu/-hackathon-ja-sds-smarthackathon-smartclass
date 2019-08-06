from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')

    class Meta:
        model = Article
        fields = ('id', 'created_at', 'content', 'writer')