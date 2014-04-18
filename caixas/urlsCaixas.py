from django.conf.urls import patterns, include, url

urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'inserirCaixa'),
    url(r'^editar/(?P<pk>\d+)/$', 'editarCaixa'),
    url(r'^salvar/$', 'salvarCaixa'),
    url(r'^pesquisar/$', 'pesquisarCaixa'),
    url(r'^excluir/(?P<pk>\d+)/$', 'excluirCaixa'),
    url(r'^$', 'listarCaixas'),
)