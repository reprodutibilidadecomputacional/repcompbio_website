from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .forms import ContactForm
from .models import News
from .models import People


# Create your views here.
def index(request):
    return render(request=request,
                  template_name='projectupdates/overview.html')

def blog(request):
    #post_list = News.objects.all().order_by('-published_date')

    # Set up pagination
    p = Paginator(News.objects.all().order_by('-published_date'), 5)
    page = request.GET.get('page')
    posts = p.get_page(page)
    nums = "a" * posts.paginator.num_pages


    return render(request=request,
                  template_name='projectupdates/blog.html',
                  context={"posts": posts,
                           "nums": nums})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message_content = f"Nome: {name}\nE-mail: {email}\n\n**********\n\nMensagem:\n{message}"

            send_mail(f"E-mail from {name}",
                      message_content,
                      settings.EMAIL_HOST_USER,
                      [settings.RECIPIENT_ADDRESS])
            return render(request,
                          'projectupdates/contato.html',
                          {'message_name': name})
    else:
        form = ContactForm()
    return render(request,
                  'projectupdates/contato.html',
                  {'form': form})

def ebook(request):
    return render(request=request,
                  template_name='projectupdates/ebook.html')

def apoio(request):
    return render(request=request,
                  template_name='projectupdates/apoio.html')

def participe(request):
    return render(request=request,
                  template_name='projectupdates/participe.html')

def quemsomos(request):
    template = loader.get_template('projectupdates/quemsomos.html')
    
    people_qs = People.objects.all()

    context = {}
    context['people'] = {}

    for person in people_qs: 
        context['people'][person.id] = {}
        context['people'][person.id]['public_name'] = person.public_name
        context['people'][person.id]['pronoums'] = person.pronoums
        context['people'][person.id]['short_bio'] = person.short_bio
        context['people'][person.id]['institution_name'] = person.institution_name
        context['people'][person.id]['email_address'] = person.email_address
        context['people'][person.id]['country'] = person.country
        context['people'][person.id]['state'] = person.state
        context['people'][person.id]['lattes'] = person.lattes
        context['people'][person.id]['google_scholar'] = person.google_scholar
        context['people'][person.id]['twitter'] = person.twitter
        context['people'][person.id]['instagram'] = person.instagram
        context['people'][person.id]['facebook'] = person.facebook
        context['people'][person.id]['linkedin'] = person.linkedin

    return HttpResponse(template.render(context, request))