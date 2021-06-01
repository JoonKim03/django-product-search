from django.db import models

class User(models.Model):
    email = models.EmailField(verbose_name = '이메일')
    password = models.CharField(max_length=64, verbose_name = '비밀번호')
    level = models.CharField(max_length=8, verbose_name='등급',
                             choices=(
                                 ('admin','admin'),
                                 ('user','user')
                             ))
    store = models.CharField(max_length=128, verbose_name='매장명')
    address = models.CharField(max_length=256, verbose_name='주소')
    phone_number = models.CharField(max_length=16, verbose_name='전화번호')
    kakao = models.CharField(max_length=8, verbose_name='카카오톡여부',
                             choices=(
                                 ('kakao','kakao'),
                                 ('none','none')
                             ))
    kakao_store = models.CharField(max_length=128, verbose_name='카카오톡매장명')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user_table'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
