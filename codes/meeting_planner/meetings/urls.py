from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.show_room, name="show_room"),
    path("rooms/<int:id>", views.show_room_detail, name="room_detail"),
    path("new", views.new, name="new"),
]