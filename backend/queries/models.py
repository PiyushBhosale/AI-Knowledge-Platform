from django.db import models
from users.models import User
from documents.models import Document
from django.contrib import admin
# Create your models here.
class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question[:20]}"

class QueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'question', 'created_at')

class Response(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.query.user.username} , {self.query.id}"