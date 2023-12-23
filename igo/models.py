from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

# < 화면 구성 >
# 관리자 글
# - 가족모임 맛집 BEST TOP 5
# - 친구끼리 갈만한 맛집 BEST TOP 5
# - 충북 청주시 맛집 BEST TOP 5
# - 유명인이 운영하는 맛집 BEST TOP 5
# - 개인 리뷰에서 평점이 높은 BEST TOP 5
# * 관리자가 올린 글에 고객들이 리뷰를 쓸 수 있다. *
# 관리자 글 모델 - 가게이름(제목), 사진, 주소, 리뷰올리기 버튼

# 개인 리뷰
# 음식 카테고리별로 맛집 나누기(스플릿), 평점이 높은 BEST TOP 3 만 뽑는다
# 개인 리뷰 모델 -  카테고리, 가게이름, 제목, 주소, 사진, 내용, 날짜(최신순 기능), 별점, 평점


# * 지도 *


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review',default='')
    subject = models.CharField(max_length=30)  # 제목
    shop_name = models.CharField(max_length=20)  # 가게이름
    address = models.CharField(max_length=50)  # 주소
    image = models.ImageField(blank=True, upload_to="", null=True)  #
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review')

class Photo(models.Model):
    post = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    Review = models.ImageField(upload_to='images/', blank=True, null=True)


class Review1(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review1',default='')
    subject = models.CharField(max_length=30)  # 제목
    shop_name = models.CharField(max_length=20)  # 가게이름
    address = models.CharField(max_length=50)  # 주소
    image = models.ImageField(blank=True, upload_to="", null=True)  # 이미지
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review1')

class Photo1(models.Model):
    post = models.ForeignKey(Review1, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Review2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review2',default='')
    subject = models.CharField(max_length=30)  # 제목
    shop_name = models.CharField(max_length=20)  # 가게이름
    address = models.CharField(max_length=50)  # 주소
    image = models.ImageField(blank=True, upload_to="", null=True)  # 이미지
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review2')


class Photo2(models.Model):
    post = models.ForeignKey(Review2, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Review3(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review3',default='')
    subject = models.CharField(max_length=30)  # 제목
    shop_name = models.CharField(max_length=20)  # 가게이름
    address = models.CharField(max_length=50)  # 주소
    image = models.ImageField(blank=True, upload_to="", null=True)  # 이미지
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review3')


class Photo3(models.Model):
    post = models.ForeignKey(Review2, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Review4(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review4',default='')
    subject = models.CharField(max_length=30)  # 제목
    shop_name = models.CharField(max_length=20)  # 가게이름
    address = models.CharField(max_length=50)  # 주소
    image = models.ImageField(blank=True, upload_to="", null=True)  # 이미지
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review4')


class Photo4(models.Model):
    post = models.ForeignKey(Review2, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Review5(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review5',default='')
    subject = models.CharField(max_length=30)  # 제목
    shop_name = models.CharField(max_length=20)  # 가게이름
    address = models.CharField(max_length=50)  # 주소
    image = models.ImageField(blank=True, upload_to="", null=True)  # 이미지
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review5')

class Photo5(models.Model):
    post = models.ForeignKey(Review2, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Review6(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)  # 제목
    shop_name = models.CharField(max_length=20)  # 가게이름
    address = models.CharField(max_length=50)  # 주소
    image = models.ImageField(blank=True, upload_to="", null=True)  # 이미지
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.CASCADE)

class Comment1(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review1, null=True, blank=True, on_delete=models.CASCADE)

class Comment2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review2, null=True, blank=True, on_delete=models.CASCADE)

class Comment3(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review3, null=True, blank=True, on_delete=models.CASCADE)

class Comment4(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review4, null=True, blank=True, on_delete=models.CASCADE)

class Comment5(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review5, null=True, blank=True, on_delete=models.CASCADE)


# 공지(notion)
class Review7(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review7',default='')
    subject = models.CharField(max_length=30)  # 제목
    image = models.ImageField(blank=True, upload_to="", null=True)  #
    contents = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 날짜
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_review7')


class Comment7(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    review = models.ForeignKey(Review7, null=True, blank=True, on_delete=models.CASCADE)