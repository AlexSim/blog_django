from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 사용자를 지우면 모든 Post를 지우겠다는 것
    body = models.TextField() 

    def __str__(self):
        return self.title