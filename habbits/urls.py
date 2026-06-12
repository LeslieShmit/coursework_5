from django.urls import path

from habbits.apps import HabbitsConfig
from habbits.views import (PublishedHabbitListView, HabbitCreateApiView,
                                HabbitDestroyApiView, HabbitListApiView,
                                HabbitRetrieveApiView, HabbitUpdateApiView)

app_name = HabbitsConfig.name

urlpatterns = [
    path("habbit/create/", HabbitCreateApiView.as_view(), name="habbit-create"),
    path("habbit/", HabbitListApiView.as_view(), name="habbit-list"),
    path("habbit/<int:pk>/", HabbitRetrieveApiView.as_view(), name="habbit-retrieve"),
    path("habbit/<int:pk>/update/", HabbitUpdateApiView.as_view(), name="habbit-update"),
    path("habbit/<int:pk>/delete/", HabbitDestroyApiView.as_view(), name="habbit-delete"),
    path(
        "published-habbit/", PublishedHabbitListView.as_view(), name="published-habbit-list"
    ),
]