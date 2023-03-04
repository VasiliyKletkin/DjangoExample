from django.db import models
from django.urls import reverse

class New(models.Model):
    title = models.CharField("Название", max_length=50)     # перевод полей модели
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    
    class Meta:
        verbose_name = "Новость"            # Для русского название в админ панели
        verbose_name_plural = "Новости"     # Для русского название в админ панели множественное число

    def __str__(self):
        return f"{self.id} {self.title}"
    
    def get_absolute_url(self):
        return reverse("new-detail", kwargs={"pk": self.pk})
    