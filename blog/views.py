from django.shortcuts import render, redirect
from blog.models import Post, Comment

# Create your views here.
def post_list(request):
    
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "post_list.html", context)

# post_id를 인자로 받는것이 첫번째
def post_detail(request, post_id):
    
    # post_id인자로 받아온 id 값에 해당하는 포스트자체를 가져온다.
    # 표시는 해당 포스트의 제목만 표시한다. (가져오는 것은 해당 포스트의 모든 것이라, context로 html에 인자 넘겨주면
    # models.py에 설정해두었던 해당 모델의 ORM을 모두 사용 가능함)
    post = Post.objects.get(id=post_id)    
    
    if request.method == "POST":
        comment_content = request.POST['comment']
        
        Comment.objects.create(
            post=post,
            content = comment_content
        )
    context = {
        "post": post
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    # html로 넘어온 form의 POST 확인 프린트
    # print(request.POST)
    if request.method == "POST":
        print("method POST")
        print(request.FILES)
        title = request.POST['title']
        content = request.POST['content']
        # 여기서 그냥 request.FILES만 하게 되면, 작성 자체도, 쏘는것도 가능하지만,
        # 속성 에러가 나오게된다. 반드시 뒤에 ["thumbnail"]을 붙여줘야한다.
        thumbnail = request.FILES["thumbnail"]
        post= Post.objects.create(
            title=title,
            content=content,
            thumbnail = thumbnail
        )
        return redirect(f"/posts/{post.id}/") # 생성된 post id값
    return render(request, "post_add.html")