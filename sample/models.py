from django.db import models


class Scroll(models.Model):
    fullname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} -- {self.fullname}'


class Date(models.Model):
    employee = models.ForeignKey(Scroll, on_delete=models.CASCADE, related_name='employees')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} -- {self.employee} -- {self.date}'
