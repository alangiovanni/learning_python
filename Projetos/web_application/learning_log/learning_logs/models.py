from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic about the user are learning]"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of model"""
        return self.text
    
class Entry(models.Model):
    """Especified something learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """Return a string representation of model"""
        return self.text[:50] + "..."