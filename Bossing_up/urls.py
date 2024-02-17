"""Bossing_up URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.urls import path, include, re_path

from django.conf.urls.static import static

from django.views.generic import TemplateView

from django_filters.views import FilterView
from bossing_up.filters import BusinessFilter

from bossing_up import views

import comment.views as comment_views

app_name = 'bossing_up'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('bizs/', views.business_list),

    path('categories/clothing', views.CategoryClothingListView.as_view(), name='clothes'),
    path('categories/accessories', views.CategoryAccessoriesListView.as_view(), name='accessories'),
    path('categories/restaurants', views.CategoryRestaurantsListView.as_view(), name='restaurants'),
    path('categories/clubs_bars_lounges', views.CategoryClubsListView.as_view(), name='bars_lounges'),
    path('categories/beauty_services', views.CategoryBeautyListView.as_view(), name='beauty_services'),
    path('categories/home_cleaning', views.CategoryCleaningListView.as_view(), name='home_cleaning'),
    path('categories/professional_services', views.CategoryProfessionalListView.as_view(), name='professional_services'),
    path('categories/construction_services', views.CategoryConstructionListView.as_view(), name='construction'),
    path('categories/coffee_tea_joints', views.CategoryCoffeeListView.as_view(), name='coffee_tea_joints'),
    path('categories/grocery_store', views.CategoryGroceryListView.as_view(), name='grocery_store'),
    path('categories/childcare', views.CategoryChildCareListView.as_view(), name='child_care'),
    path('categories/health_and_wellness', views.CategoryHealthListView.as_view(), name='health_wellness'),
    path('categories/beauty_supplies', views.CategoryBeautySuppliesListView.as_view(), name='beauty_supplies'),
    path('categories/other', views.CategoryOtherListView.as_view(), name='other'),

    #COMMENTS URLS
    path('comment/<int:pk>/approve/', comment_views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_views.comment_remove, name='comment_remove'),


    # API URLS
    path('api/', include('rest_framework.urls')),
    url(r'^business/(?P<pk>\d+)/$', views.BusinessDetailAPIView.as_view(), name='business-detail'),
    path('business/list/', views.ApiAllListView.as_view(), name='business-list'),

    #REVIEW CONFIRMATION VIEW
    path('activate/<uidb64>/<token>', views.ReviewVerificationView.as_view(), name='review-activate'),


    path('site/', TemplateView.as_view(template_name="index_old.html")),
    path('blog/', TemplateView.as_view(template_name="blog/blog.html")),

    path('blog/a-seat-at-the-table', TemplateView.as_view(template_name="blog/a-seat-at-the-table.html")),
    path('blog/black-hair-korean-industry', TemplateView.as_view(template_name="blog/black-hair-korean-industry.html")),
    path('blog/fresh-to-death-exploration-of-fashion-and-black-culture-part-two', TemplateView.as_view(template_name="blog/fresh-to-death-exploration-of-fashion-and-black-culture-part-two.html")),
    path('blog/fresh-to-death-exploration-of-fashion-and-black-culture', TemplateView.as_view(template_name="blog/fresh-to-death-exploration-of-fashion-and-black-culture.html")),
    path('blog/mental-health-and-black-communities', TemplateView.as_view(template_name="blog/mental-health-and-black-communities.html")),
    path('blog/no-customer-no-business', TemplateView.as_view(template_name="blog/no-customer-no-business.html")),
    path('blog/the-economy-of-black-hair', TemplateView.as_view(template_name="blog/the-economy-of-black-hair.html")),
    path('blog/wealth-in-the-community', TemplateView.as_view(template_name="blog/wealth-in-the-community.html")),


    #PRIVACY POLICY AND TERMS OF USE
    path('privacy_policy', TemplateView.as_view(template_name="privacy_policy.html")),
    path('terms_of_use', TemplateView.as_view(template_name="terms_of_use.html")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
