from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Post
from .forms import PostForms


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context =  {
                'post' : post
               }
    return render(request, 'post/detail.html', context)


def post_create(request):
    #if request.method == "POST":
    #   print("Request post")

    # iki senaryo var birinde boş form istemesi diğerindde dolu  formu submit etmesi
    """if request.method == "POST":
        # Formdan gelen bilgileri kaydet
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        # Formu kullanıcılara göster.
        form = PostForms()"""

    form = PostForms(request.POST or None)  # Eğer requestçpost varsa al yoksa boş bir post oluştur. Yukarıki if le aynı
    if form.is_valid():
        form.save()

    context = {
        "form": form,
    }

    return render(request, 'post/form.html', context)





def post_update(request):
    return HttpResponse('<h>Update Page</h>')

def post_delete(request):
    return HttpResponse('<h>Delete Page</h>')

