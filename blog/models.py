from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)            # 타이틀
    pub_date = models.DateTimeField('date published')   # 날짜
    body = models.TextField()                           # 내용  

    def __str__(self):
        return self.title