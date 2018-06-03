from django.shortcuts import render,reverse

# add generic class views as needed, CRUD
from django.views.generic import (CreateView,ListView,DetailView)

# project imports
from .models import Floor,Room
from .forms import FloorForm,RoomForm

# Create your views here.

#########################
####  Floor views    ####
#########################

# create
class FloorCreateView(CreateView):
    model = Floor
    form_class = FloorForm

    def get_success_url(self):
        return reverse('floors')

# review
class FloorListView(ListView):
    model = Floor


#########################
####   Room views    ####
#########################

# create
class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm

    def get_success_url(self):
        return reverse('rooms')

class RoomListView(ListView):
    model = Room

def room_detail_view(request,**kwargs):
    print(request.roomid)
    args = dict(roomid=request.roomid)
    return render(request,'room_detail.html',args)

class RoomDetailView(DetailView):
    model = Room
