from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


CustomUser = get_user_model()
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100,unique=True)
    num_of_task = models.IntegerField()
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse("list", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
    

STATUS_CHOICES = (
    ("NOT-STARTED","Not-Started"),
    ("IN PROGRESS","In Progress"),
    ("DONE","Done") )

PRIORITY_CHOICES = (
    ("HIGH","High"),
    ("MEDIUM","Medium"),
    ("LOW","Low")
)
class TodoItem(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="NOT-STARTED")
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default="HIGH")
    assigned_to = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=one_week_hence)
    task_completion = models.DecimalField(max_digits=3,decimal_places=2)
    todo_list = models.ForeignKey(TodoList,on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("item-list", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.title}: due{self.due_date}'
    
    class Meta:
        ordering = ['due_date']
    