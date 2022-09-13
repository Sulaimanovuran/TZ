from rest_framework import serializers

from sample.models import Scroll, Date


class ScrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scroll
        fields = '__all__'


class DateSerializer(serializers.Serializer):
    date = serializers.DateField(required=True)
    register = ScrollSerializer(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        id = instance.employee_id
        name = Scroll.objects.filter(id=id)
        representation['employee'] = name.values()
        return representation


class DateSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'