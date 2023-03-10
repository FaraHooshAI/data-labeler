from django.db import models
from django.db.models import F

class User(models.Model):
    user_name = models.CharField(max_length=50, unique= True)
    email = models.EmailField(max_length=50, unique = True)


class EmotionText(models.Model):
    emotion_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.emotion_name}"

class DataName(models.Model):
    data_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.data_name}"

class DataText(models.Model):
    data_name = models.ForeignKey(DataName, on_delete=models.CASCADE)
    text = models.TextField()
    emotion_primary = models.ForeignKey(EmotionText, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='primary')
    emotion_secondary = models.ManyToManyField(EmotionText, blank=True, related_name='secondary')
    deleted = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Data"
        #ordering = [F('emotion_primary').asc(nulls_last=True)]


