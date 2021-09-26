from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.id}. {self.title} ({self.tag})'

