from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

from habbits.models import Habbit
from habbits.serializers import HabbitSerializer
from users.permissions import IsOwner

from .paginators import MyPagination


class HabbitCreateApiView(CreateAPIView):
    """Класс контроллера для создания привычки"""

    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serialazer):
        """метод автоматического сохранения пользователя в поле владельца"""
        wont = serialazer.save()
        wont.owner = self.request.user
        wont.save()


class HabbitListApiView(ListAPIView):
    """Класс контроллера для вывода списка привычек"""

    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        """метод отображения привычек заданного пользователя"""
        return Habbit.objects.filter(owner=self.request.user)


class HabbitRetrieveApiView(RetrieveAPIView):
    """Класс контроллера для вывода экземпляра привычки"""

    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = (IsOwner,)


class HabbitUpdateApiView(UpdateAPIView):
    """Класс контроллера для изменения экземпляра привычки"""

    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = (IsOwner,)


class HabbitDestroyApiView(DestroyAPIView):
    """Класс контроллера для удаления экземпляра привычки"""

    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = (IsOwner,)


class PublishedHabbitListView(ListAPIView):
    """Класс контроллера для списка публичных привычек"""

    queryset = Habbit.objects.filter(is_published=True)
    serializer_class = HabbitSerializer
    permission_classes = [
        AllowAny
    ]  # Любой пользователь может видеть публичные привычки

