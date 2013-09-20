from django.conf.urls.defaults import patterns, include, url
import usuario
#from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'db_validation.views.home', name='home'),
    # url(r'^db_validation/', include('db_validation.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)



urlpatterns = patterns('',
    url(r'^$', include('usuario.urls')),
    url(r'^usuario/formulario/', 'usuario.views.formulario'),
    url(r'^usuario/lista/', 'usuario.views.lista'),
)