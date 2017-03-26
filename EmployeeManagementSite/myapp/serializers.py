from rest_framework import serializers
from myapp.models import Company, User, LANGUAGE_CHOICES, STYLE_CHOICES


class CompanySerializer(serializers.Serializer):
    company_id = serializers.AutoField(primary_key=True)
    company_name = serializers.TextField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.company_name = validated_data.get('name', instance.company_name)

        instance.save()
        return instance
