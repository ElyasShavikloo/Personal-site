from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    father_name = models.CharField(max_length=30, verbose_name="نام پدر")
    national_code = models.CharField(max_length=10, verbose_name="کد ملی")
    user_image = models.ImageField(upload_to='profiles/img', blank=True, null=True, verbose_name="تصویر کاربر")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'




