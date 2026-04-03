from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source = "user.username", read_only=True)
    class Meta:
        model = Document
        fields = ['id','user','title','file']

    def create(self, validated_data):
        file = validated_data.get('file')
        file_type = file.name.split('.')[-1]
        file_size = file.size

        return Document.objects.create(**validated_data, file_size=file_size, file_type=file_type)

