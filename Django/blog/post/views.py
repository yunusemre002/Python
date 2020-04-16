from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForms
from django.contrib import messages


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
    # if request.method == "POST":
    #    print("Request post")

    # iki senaryo var birinde boş form istemesi diğerindde dolu  formu submit etmesi
    """if request.method == "POST":        # Formdan gelen bilgileri kaydet
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()
    else:                                 # Formu kullanıcılara göster.
        form = PostForms()"""

    form = PostForms(request.POST or None)  # Eğer requestçpost varsa al yoksa boş bir post oluştur. Yukarıki if le aynı
    if form.is_valid():
        post = form.save()                  # eklenen veya güncellenen nesneyi geri döndürür.
        messages.success(request, "Basarili bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())       # ilgili formun detayına gitsin bu yüzden saveden dönen metodun
                                                                    #adresini alıp redirecte gönderdim.
    context = {
        "form": form,
    }
    return render(request, 'post/form.html', context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)                      # Post detailden aldık postun deyatlarını döndürüyor.
    form = PostForms(request.POST or None, instance=post)      # Post create den aldık  içine üsteki postu koyduk.
    if form.is_valid():                                        # İnstance : örnek,durum,istek...
        form.save()                                            # Eklenen veya güncellenen nesneyi geri döndürür.
        messages.success(request, "Basarili bir şekilde düzenlediniz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())   # ilgili formun detayına gitsin bu yüzden saveden dönen metodun

    context = {
                "form": form,
               }
    return render(request, 'post/form.html', context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')

