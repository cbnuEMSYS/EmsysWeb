from django.conf import settings
from django.db import models
from django.utils import timezone

class Board(models.Model):
    """
        title: 제목
        content: 내용
        author: 작성자
        like_count: 좋아요 카운트
        pub_date: 배포일
    """
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    like_count = models.PositiveIntegerField(default=0) # 양수입력 필드
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Reply(models.Model):
    """
        reply: Reply -> Board 연결관계
        comment: 댓글내용
        rep_date: 작성일
    """
    reply = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment