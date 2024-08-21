from django.conf import settings
from django.db import models
from django.utils import timezone

# https://velog.io/@charmull/Django-%EC%97%B0%EC%8A%B5-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-app-%EC%83%9D%EC%84%B1-%EB%B0%8F-%EB%AA%A8%EB%8D%B8-%EC%9E%91%EC%84%B1
class Post(models.Model):   # 모델 클래스 정의
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(verbose_name="제목", max_length=200)
    content = models.TextField(verbose_name="내용")
    created_date = models.DateTimeField(
        verbose_name="작성일", default=timezone.now)

    def __str__(self):
        return self.title