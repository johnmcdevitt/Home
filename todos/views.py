from django.shortcuts import render
from django.urls import reverse

# add generic class views as needed, CRUD
from django.views.generic import (CreateView,ListView,DetailView,UpdateView)

# project imports
from .models import ToDo
from .forms import ToDoForm

# Create your views here.
class ToDoCreateView(CreateView):
    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                'request': self.request})
        return kwargs

    model = ToDo
    form_class = ToDoForm

    def get_success_url(self):
        return reverse('todos')

class ToDoUpdateView(UpdateView):
    model = ToDo
    fields = ['description','status','due_date']

    def get_success_url(self):
        return reverse('todos')

    def mark_done(self):
        print("user is %s and creator is %s" % (self.request.user,self.model.created_by))
        return (print("mark_done completed"))

    def form_valid(self,form,request):
        mark_done()
        pass

    # if form.is_valid():
    #     pass

    # TODO add or delete def validate_method(self):
    #     if self.request.method == 'POST':
    #         try:
    #             self.mark_done()
    #         except:
    #             print("mark_done failed")
    #     return

class ToDoDetailView(DetailView):
    model = ToDo



def ToDoLandingView(request):
    model = ToDo


    mytodos = ToDo.objects.all().filter(assigned_to=request.user)
    context = dict(all=ToDo.objects.all(),mytodos=mytodos)

    return render(request, "todo_landing.html", context)
