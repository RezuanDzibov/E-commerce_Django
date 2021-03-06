from rest_framework import serializers

from src.product import models


class ProductListSerializer(serializers.ModelSerializer):
    """ Serializer for list of products """
    category = serializers.CharField(source="category.name")

    class Meta:
        model = models.Product
        fields = ("name", "slug", "category", "price", "available")


class ProductRetrieveSerializer(serializers.ModelSerializer):
    """ Serializer for retrieve product """
    category = serializers.CharField(source="category.name")
    images = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="product:image-detail")

    class Meta:
        model = models.Product
        fields = (
            "name", 
            "slug", 
            "category", 
            "price", 
            "available", 
            "small_description",
            "created", 
            "updated",
            "images",
        )


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    """ Serializer for create and update product """
    class Meta:
        model = models.Product
        fields = (
            "name", 
            "slug", 
            "category", 
            "small_description",
            "price", 
            "available"
        )


class ImageSerializer(serializers.ModelSerializer):
    """ Image serializer """
    class Meta:
        model = models.Image
        fields = ("image", "alt_text")


class CategoryListSerializer(serializers.ModelSerializer):
    """ Serializer for list of categories """
    url = serializers.HyperlinkedIdentityField(view_name="product:category-detail", lookup_field="slug")

    class Meta:
        model = models.Category
        fields = ("name", "url")


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    """ Serializer for retrieve category """
    products = ProductListSerializer(many=True)

    class Meta:
        model = models.Category
        fields = ("id", "name", "slug", "parent", "products")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.parent:
            data["parent"] = instance.parent.name
        return data


class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    """ Serializer for create and update category """
    class Meta:
        model = models.Category
        fields = ("name", "parent")