from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    #질문 고유 id가 필요한지,erd에추가해야하는지 
    id = models.UUIDField(help_text="Unique key", primary_key=True, default=uuid.uuid4, editable=False)
    userid = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField()

class Post(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    likes= models.IntegerField()
    title= models.CharField(max_length=100)
    post = models.TextField()
    created_at=models.DateTimeField()
    
class Comment(models.Model):
    post_id= models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at=models.DateTimeField()
    