from rest_framework import serializers
from .models import Shoe, ShoeSize


class ShoeSizeSerealizer(serializers.ModelSerializer):
    class Meta:
        model = ShoeSize
        fields = "__all__"


class ShoeSerializer(serializers.ModelSerializer):
    sizes = ShoeSizeSerealizer(many=True)

    class Meta:
        model = Shoe
        fields = "__all__"

    def create(self, validated_data):
        sizes_data = validated_data.pop("sizes", [])
        shoe = Shoe.objects.create(**validated_data)

        for size_data in sizes_data:
            ShoeSize.objects.create(shoe=shoe, **size_data)

        return shoe

    def update(self, instance, validated_data):
        sizes_data = validated_data.pop("sizes", [])
        instance.name = validated_data.get("name", instance.name)
        instance.brand = validated_data.get("brand", instance.brand)
        instance.price = validated_data.get("price", instance.price)
        instance.save()

        instance.sizes.all().delete()
        for size_data in sizes_data:
            ShoeSize.objects.create(shoe=instance, **size_data)

        return instance
