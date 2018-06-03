from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(ToDoForm, self).__init__(*args,**kwargs)

    def save(self, *args, **kwargs):
        obj = super(ToDoForm,self).save(commit=False)
        obj.created_by = self.request.user
        obj.save()

    class Meta:
        model = ToDo
        exclude = ['todoid','created_by']

    def is_valid(self):

        # run parent validation first
        valid = super(ToDoForm,self).is_valid()

        # if not valid nothing further needed
        if not valid:
            return valid

        try:
            print(self.object.status)
        except:
            print("self.object.status failed")

        try:
            self.request.user
        except:
            print("self.request.user failed")

        # returning valid to avoid error will need TODO custom code errors later
        return valid
