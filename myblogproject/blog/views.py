from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from django.db.models import Q

# Create your views here.
def lista_publicaciones(request):
    query = request.GET.get('q')
    fecha = request.GET.get('fecha')
    categoria = request.GET('categoria')

    posts = Post.objects.all()
    if query:
        posts = posts.filter(Q(titulo__incontains=query) | Q(contenido__icontains=query))
    if fecha:
        posts = posts.filter(fecha_publicacion=fecha)
    if categoria:
        posts = posts.filter(categoria=categoria)

    Paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(page_number)

    return render(request, 'blog/lista_publicaciones.html', {'page_obj': page_obj})

def detalle_publicacion(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'post': post})

def crear_ppublicacion(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PostForm()
    return render(request, 'blog/crear_publicacion.html', {'form': form})