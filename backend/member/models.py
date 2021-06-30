from django.db import models


class MemberV0(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()

    class Meta:
        managed = True
        db_table = 'members'

    def __str__(self):
        return f'[{self.pk}]{self.username}'