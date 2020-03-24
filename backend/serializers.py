from rest_framework import serializers
from backend.models import Snippet,Simple

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = [
        'created','name','url','location','about_description',
        'company_name','professional_description'
                 ]

class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simple
        fields = [
                    'name'
                 ]
