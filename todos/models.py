from django.db import models
from webusers.models import WebUser
from house.models import Room
from datetime import date

# Create your models here.
# todo model, should be able to assign dates and users
class ToDo(models.Model):

    priority_choices = (
        ('3', 'High'),
        ('2', 'Medium'),
        ('1', 'Low'),
    )

    status_choices = (
        ('N', 'Not started'),
        ('I', 'In progress'),
        ('C', 'Completed'), # anyone can mark a task as completed
        ('D', 'Done'), # creator will mark items as done
    )

    todoid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True)
    priority = models.CharField(max_length=1,
                                choices=priority_choices,
                                default='2')
    assigned_to = models.ForeignKey(WebUser,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name='%(app_label)s_%(class)s_assigned')
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(WebUser,
                                   on_delete=models.CASCADE,
                                   related_name="%(app_label)s_%(class)s_created")
    due_date = models.DateField()
    status = models.CharField(max_length=1,
                              choices=status_choices,
                              default='N')

    def __str__(self):
        return self.title

    # define overdue or approaching due dates
    def is_overdue(self):
        return self.due_date <= date.today()

    def is_approaching(self):
        return ((self.due_date - date.today()).days < 5)

    # def creator_done(self, request):
    #     print("todo creator_done called")
    #     is_valid = True
    #     if self.status == 'D': # check for Done
    #         if request.user != self.created_by:
    #             is_valid = False
    #     return is_valid
    #
    # def clean(self):
    #     print("todo clean called")
    #     if not self.creator_done(request):
    #         raise django_exceptions.ValidationError("Only %s can mark this item Done" % self.created_by)
    #
    # def save(self, *args, **kwargs):
    #     """
    #     ToDo model custom save method to ensure self.clean is used to validate
    #     model constraints
    #     """
    #     print("todo save called")
    #     self.full_clean()
    #     return super(ToDo, self).save(*args, **kwargs)
