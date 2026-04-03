from django.db import models
from users.models import User
# Create your models here.

def upload_path(instance, filename):
    return f"documents/user_{instance.user.id}/{filename}"

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=upload_path)
    file_type = models.CharField(max_length=10)
    file_size = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.title[:20]}'