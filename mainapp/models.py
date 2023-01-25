from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50, unique= True)
    email = models.EmailField(max_length=50, unique = True)


class EmotionText(models.Model):
    emotion_name = models.CharField(max_length=50, unique=True)


class DataText(models.Model):
    text = models.TextField()
    emotion_primary = models.ForeignKey(EmotionText, on_delete=models.DO_NOTHING, null=True, blank=True)
    emotion_secondary = models.ManyToManyField(EmotionText, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Data"


