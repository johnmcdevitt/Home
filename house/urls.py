from django.urls import path
from . import views

# app url patterns
urlpatterns = [

    # floor patterns
    path('floor/',views.FloorListView.as_view(),name='floors'),
    path('floor/create/',views.FloorCreateView.as_view(),name='floor-create'),

    # room patterns
    path('',views.RoomListView.as_view(),name='rooms'), # TODO create index and remove this
    path('room/',views.RoomListView.as_view(),name='rooms'),
    #path('room/<int:roomid>',views.room_detail_view,name='room-detail'),
    path('room/<int:pk>',views.RoomDetailView.as_view(),name='room-detail'),
    path('room/create/',views.RoomCreateView.as_view(),name='room-create'),

    # other model patterns below
]
