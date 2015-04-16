from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblioteca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/', 'controllers.cadastro.home'),
    url(r'^cadastro/', 'controllers.cadastro.cadastro'),
    url(r'^cadastrar_livro/', 'controllers.cadastro.cadastrar_livro'),
    url(r'^admin/', include(admin.site.urls)),
)
