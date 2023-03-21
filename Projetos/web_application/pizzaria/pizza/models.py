from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A topic about the user are learning]"""
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Return a string representation of model"""
        return self.name
    
class Topping(models.Model):
    """Especified something learned about a topic"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self) -> str:
        """Return a string representation of model"""
        if len(self.name) > 50:
            return self.name[:50] + "..."
        else:
            return self.name
