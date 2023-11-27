from django.db import models

class chat_id1(models.Model):
    id=models.AutoField(primary_key=True)
    chat_idname=models.CharField(max_length=100)
