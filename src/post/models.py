from django.db import models


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    text = models.TextField(max_length=280)

    def __str__(self):
        return self.id
