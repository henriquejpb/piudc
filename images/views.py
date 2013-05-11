# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from images.models import Image
from images.remote.picasa import RemoteModel
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def image_view(request, id):
    template = loader.get_template('images/image_view.html')
    try:
        context = RequestContext(request, {
            'image_data' : Image.objects.get(pk=id)
        })
    except ObjectDoesNotExist:
        context = Context({})

    return HttpResponse(template.render(context))

def filter(request, id):
    print request.GET.dict()
    return HttpResponse(request.GET.dict())
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])

def update(request, id):
    image = Image.objects.get(pk=id)
    image.title = request.POST['title']
    image.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def delete(request, id):
    image = Image.objects.get(pk=id)
    image.delete()
    return HttpResponseRedirect(reverse('local_list'))

def local_list(request):
    image_list = Image.objects.all()

    paginator = Paginator(image_list, 12)
    page = request.GET.get('page', 1)

    images = []
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images.paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    print images.has_other_pages()
    
    template = loader.get_template('images/local_list.html')
    context = Context({
        'image_list' : images
    })

    return HttpResponse(template.render(context))

def remote_list(request):
    remote_model = RemoteModel();

    template = loader.get_template('images/remote_list.html')
    context = Context({
        'image_list' : remote_model.get_list()
    })

    return HttpResponse(template.render(context))

def download(request, id):
    remote_file, path = RemoteModel().download(id)

    image = Image()
    image.title = remote_file.title
    image.pathname = path
    image.save()
    
    return HttpResponseRedirect(reverse('local_list'))

def upload(request, id):
    image = Image.objects.get(pk=id)
    remote_file = RemoteModel().upload(image)
    image.delete()

    return HttpResponseRedirect(reverse('remote_list'))

def remote_delete(request, id):
    RemoteModel().delete(id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
def sync_all(request):
    image_list = Image.objects.all()
    remote_model = RemoteModel()
    for image in image_list:
        remote_model.upload(image)
        image.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
