from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50, unique= True)
    email = models.EmailField(max_length=50, unique = True)


class EmotionText(models.Model):
    emotion_name = models.CharField(max_length=50, unique=True)


class DataText(models.Model):
    data_name = models.CharField(max_length=50, unique= True)
    text = models.TextField()
    emotion_primary = models.ForeignKey(EmotionText, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='primary')
    emotion_secondary = models.ManyToManyField(EmotionText, blank=True, related_name='secondary')
    class Meta:
        verbose_name_plural = "Data"


