from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from .models import Makaleler, Contact


# Create your views here.
def index(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/anasayfa.html', {'ucmakale': ucmakale})

def about(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/hakkimizda.html', {'ucmakale': ucmakale})

def practices(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/uzmanliklar.html', {'ucmakale': ucmakale})

def ailehukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/ailehukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def arabuluculuk(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/arabuluculuk.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def cezahukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/cezahukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def idarehukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/idarehukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def ishukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/ishukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def fikrimulkiyethukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/fikrimulkiyethukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def icrahukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/icrahukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def ticarethukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/ticarethukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def sozlesmelerhukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/sozlesmelerhukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def yabancilarhukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/yabancilarhukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def mirashukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/mirashukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def tuketicihukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/tuketicihukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})



def hukukiyayinlar(request):
    if request.GET.get('hukuki-alan'):

        alan = request.GET.get('hukuki-alan')

        makale_list = Makaleler.objects.filter(makale_kategori=alan)

        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)
        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/hukukiyayinlar.html', {'articles' : articles, 'ucmakale' : ucmakale})

    elif request.GET.get('makale-ara'):

        arama = request.GET.get('makale-ara')

        makale_list = Makaleler.objects.filter(makale_baslik__icontains=arama)

        paginator = Paginator(makale_list, 4)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/hukukiyayinlar.html', {'articles': articles, 'ucmakale': ucmakale})

    else:
        makale_list = Makaleler.objects.all()
        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)

        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/hukukiyayinlar.html', {'articles': articles, 'ucmakale' : ucmakale})


def makaledetay(request, makaleslug):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    oncekimakale = Makaleler.objects.all().order_by('?').first()
    sonrakimakale = Makaleler.objects.all().order_by('?').first()

    makale = Makaleler.objects.get(makale_slug=makaleslug)

    return render(request, 'websitesi/makaledetay.html', {'makale' : makale,'ucmakale' : ucmakale, 'oncekimakale' : oncekimakale, 'sonrakimakale' : sonrakimakale})



def bizeulasin(request):

    if request.method == 'POST':

        adsoyad = request.POST.get('isim')
        email = request.POST.get('email')

        telefon = request.POST.get('telefon')
        mesaj = request.POST.get('mesaj')

        iletisim = Contact(iletisim_adsoyad=adsoyad, iletisim_telefon=telefon, iletisim_mail=email,
                             iletisim_mesaj=mesaj)
        iletisim.save()
        return redirect('anasayfa')

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/bizeulasin.html', {'ucmakale' : ucmakale})
