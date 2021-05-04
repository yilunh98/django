from django.urls import path, reverse_lazy
from . import views
from . import models
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name = 'all'),
    # path('ad/<int:pk>',
    #     OwnerDetailView.as_view(
    #         model = models.Ad,
    #         template_name = app_name+"/ad_detail.html"),
    #     name='ad_detail'),

    # path('ad/create',
    #     OwnerCreateView.as_view(
    #         success_url=reverse_lazy(app_name+':all'),
    #         model = models.Ad,
    #         template_name = app_name+"/ad_form.html",
    #         fields = ['title', 'text']
    #      ), name='ad_create'),

    # path('ad/<int:pk>/update',
    #     OwnerUpdateView.as_view(
    #         success_url=reverse_lazy(app_name+':all'),
    #         model = models.Ad,
    #         fields = ['title', 'text'],
    #         template_name = app_name+"/ad_form.html"
    #     ), name='ad_update'),

    # path('ad/<int:pk>/delete',
    #     OwnerDeleteView.as_view(
    #         success_url=reverse_lazy(app_name+':all'),
    #         model = models.Ad,
    #         template_name = app_name+"/ad_confirm_delete.html"
    #     ), name='ad_delete'),

    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),

    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('ads')), name='ad_comment_delete'),
    path('ad/<int:pk>/favorite',
        views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite',
        views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]