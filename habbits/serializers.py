from rest_framework.serializers import ModelSerializer

from habbits.models import Habbit


class HabbitSerializer(ModelSerializer):
    """Класс сериализатора для модели привычки"""

    class Meta:
        model = Habbit
        fields = "__all__"
        read_only_fields = ["id", "owner"]

    def validate(self, attrs):
        """Функция валидации полей модели привычки"""
        habbit = Habbit(**attrs)
        habbit.clean()
