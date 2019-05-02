from django.urls import path
from .views import index, about, practices, ailehukuku, arabuluculuk, cezahukuku, idarehukuku, \
                    ishukuku, fikrimulkiyethukuku, icrahukuku, ticarethukuku, sozlesmelerhukuku, hukukiyayinlar, \
                    yabancilarhukuku, mirashukuku, tuketicihukuku, bizeulasin, makaledetay

from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name="anasayfa"),
    path('hakkimizda/', about, name="hakkimizda"),
    path('uzmanliklar/', practices, name="uzmanliklar"),

    path('aile-hukuku/', ailehukuku, name="ailehukuku"),
    path('arabuluculuk/', arabuluculuk, name="arabuluculuk"),
    path('ceza-hukuku/', cezahukuku, name="cezahukuku"),
    path('idare-hukuku/', idarehukuku, name="idarehukuku"),
    path('is-ve-sosyal-guvenlik-hukuku/', ishukuku, name="ishukuku"),
    path('fikri-mulkiyet-hukuku/', fikrimulkiyethukuku, name="fikrimulkiyethukuku"),
    path('icra-ve-iflas-hukuku/', icrahukuku,  name="icrahukuku"),
    path('ticaret-hukuku/', ticarethukuku, name="ticarethukuku"),
    path('sozlesmeler-hukuku/', sozlesmelerhukuku, name="sozlesmelerhukuku"),
    path('yabancilar-hukuku/', yabancilarhukuku, name="yabancilarhukuku"),
    path('miras-hukuku/', mirashukuku, name="mirashukuku"),
    path('tuketici-hukuku/', tuketicihukuku, name="tuketicihukuku"),

    path('bize-yazin/', bizeulasin, name="bizeulasin"),

    path('hukukiyayinlar/', hukukiyayinlar, name="hukukiyayinlar"),
    path('sitemap.xml/', TemplateView.as_view(template_name='websitesi/sitemap.xml', content_type='text/plain'), name="sitemap" ),
    path('robots.txt/', TemplateView.as_view(template_name='websitesi/robots.txt', content_type='text/plain')),

    path('<slug:makaleslug>/', makaledetay, name="makaledetay"),  ## Bu regexden dolayı url'in karışmaması için en sona gelecek.
]
