from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')



    # commenting 字段记录评论数
    commenting = models.PositiveIntegerField(default=0)

    def increase_commenting(self):
        self.commenting += 1
        self.save(update_fields=['commenting'])





    def __str__(self):
        return self.text[:20]



