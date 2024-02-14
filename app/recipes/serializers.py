"""
Serializers for recipes API.
"""
from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create and return recipe."""
        auth_user = self.context['request'].user
        recipe = Recipe.objects.create(user=auth_user, **validated_data)
        return recipe


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
