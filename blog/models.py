from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("글 제목", max_length=50) # 포스트제목
    content = models.TextField("글 내용")
    # upload_to는 settings.py에 media 루트에 지정된 바로 아랫단계에 지정된 단어가 없으면, 폴더생성 후 이미지 업로드
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)
    
    # 수정시간
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # ForeignKey처럼 파라미터의 인자값 첫번째에 다른 값을 써야할 경우 verbose_name으로 선언함으로 admin에서
    # 어떤 내용인지 명확하게 확인이 가능하다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="연결된 포스트")
    content = models.TextField("댓글 내용")
    
    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"