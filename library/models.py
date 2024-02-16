from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name

    def next(self):
        try:
            return Author.objects.filter(id__gt=self.id).order_by('id').first()
        except Author.DoesNotExist:
            return None

    def previous(self):
        try:
            return Author.objects.filter(id__lt=self.id).order_by('-id').first()
        except Author.DoesNotExist:
            return None

    @staticmethod
    def first():
        return Author.objects.order_by('id').first()

    @staticmethod
    def last():
        return Author.objects.order_by('-id').first()


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default='')
    remarks = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.title
