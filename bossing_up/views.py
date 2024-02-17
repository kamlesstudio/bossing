import json
import django_filters

from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import get_object_or_404, redirect

from django.db.models import Q

from django.contrib import messages

from django.core.mail import EmailMessage

from django.urls import reverse 
from .utils import token_generator

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .forms import LocationCoods

from django.views.generic import TemplateView

from comment.forms import CommentForm

from comment.models import Comment

from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from .serializers import BlackBusinessSerializer, BlackBusinessDetailSerializer
from .models import BlackBusiness

from .filters import BusinessFilter

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site


class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"

class TermsOfUseView(TemplateView):
    template_name = "terms_of_use.html"

class IndexOldView(TemplateView):
    template_name = "index_old.html"

class BlogView(TemplateView):
    template_name = "blog/blog.html"

class Blog1View(TemplateView):
    template_name = "blog/a-seat-at-the-table.html"

class Blog2View(TemplateView):
    template_name = "blog/black-hair-korean-industry.html"

class Blog3View(TemplateView):
    template_name = "blog/fresh-to-death-exploration-of-fashion-and-black-culture.html"

class Blog3View(TemplateView):
    template_name = "blog/fresh-to-death-exploration-of-fashion-and-black-culture-part-two.html"

class Blog4View(TemplateView):
    template_name = "blog/mental-health-and-black-communities.html"

class Blog5View(TemplateView):
    template_name = "blog/no-customer-no-business.html"

class Blog6View(TemplateView):
    template_name = "blog/the-economy-of-black-hair.html"

class Blog7View(TemplateView):
    template_name = "blog/wealth-in-the-community.html"

@csrf_exempt
def business_list(request):
    """
    List all businesses, or create a new business record.
    """
    if request.method == 'GET':
        businesses = BlackBusiness.valid_cleaned('self')
        serializer = BlackBusinessSerializer(businesses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlackBusinessSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class HomePageView(ListAPIView):
    queryset = BlackBusiness.valid_cleaned('self')
    serializer_class = BlackBusinessSerializer
    renderer_classes = [TemplateHTMLRenderer]
    filter_backends = [DjangoFilterBackend]
    template_name = 'index_bu.html'

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='resta').order_by('?')
        businessFilter = BusinessFilter()
        form = LocationCoods()
        context = {'businesses':queryset, 'businessFilter':businessFilter, 'form':form}

        return Response(context)

def search(request):
    businesses = BlackBusiness.valid_cleaned('self')

    businessFilter = BusinessFilter()

    business_filter = BusinessFilter(request.GET, queryset=businesses)
    
    form = LocationCoods(request.GET) or None
    if form.is_valid():
        lat = form.cleaned_data.get('lat') 
        lng = form.cleaned_data.get('lng')
        points = []
        all_points = business_filter.qs
        result_list = []
        selected_location = (lat, lng)

        for point in all_points:
            if isinstance(point.latitude, str) == True:
                break
            elif isinstance(point.longitude, str) == True:
                break
            elif point.latitude is None:
                break
            elif point.longitude is None:
                break

            points = (point.latitude, point.longitude)

            from haversine import haversine, Unit
            result = haversine(selected_location, points)
            if result < 5.5: # check for distance in km
                result_list.append(point.id)
        
        business_filter = all_points.filter(id__in=result_list).all()
        
        filter_count = business_filter.count()
        
        return render(request, 'search_view.html', {'businesses': business_filter, 'filter_count':filter_count, 'businessFilter':businessFilter, 'form': form})
    else:
        lat = 40.730610 
        lng = -73.935242
        points = []
        all_points = business_filter.qs
        result_list = []
        selected_location = (lat, lng)

        for point in all_points:
            if isinstance(point.latitude, str) == True:
                break
            elif isinstance(point.longitude, str) == True:
                break
            elif point.latitude is None:
                break
            elif point.longitude is None:
                break

            points = (point.latitude, point.longitude)

            from haversine import haversine, Unit
            result = haversine(selected_location, points)
            if result < 2000: # check for distance in km
                result_list.append(point.id)
        
        business_filter = all_points.filter(id__in=result_list).all()
            
        filter_count = business_filter.count()
        return render(request, 'search_view.html', {'businesses': business_filter, 'filter_count':filter_count, 'businessFilter':businessFilter, 'form': form})


class CategoryClothingListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='clot')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

    # def testgmap(self, request):
    #     data = BlackBusiness.valid_cleaned('self').values('title', 'latitude', 'longitude')
    #     json_data = json.dumps(list(data))
    #     return Response({'locations': json_data}) 

class CategoryAccessoriesListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='acce')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryRestaurantsListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='rest')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryClubsListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='club')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryBeautyListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='beau')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryCleaningListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='clean')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryProfessionalListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='prof')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryConstructionListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(category__icontains='const')
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryCoffeeListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(Q(category__icontains='coffe') | Q(category__icontains='tea'))
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})


class CategoryGroceryListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(Q(category__icontains='groce') | Q(tags__icontains='groce'))
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})


class CategoryChildCareListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(Q(category__icontains='child') | Q(tags__icontains='child'))
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryHealthListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(Q(category__icontains='health') | Q(tags__icontains='health'))
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})

class CategoryBeautySuppliesListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(Q(category__icontains='beauty supplies') | Q(tags__icontains='beauty supplies'))
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})



class CategoryOtherListView(ListAPIView):
    template_name = 'category.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self').filter(Q(category__icontains='other') | Q(tags__icontains='other'))
        count = queryset.count()
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset, 'count': count})



class BusinessDetailAPIView(RetrieveAPIView):
    queryset = BlackBusiness.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        form = CommentForm()
        self.object = self.get_object()
        return Response({'business': self.object, 'form':form}, template_name='detail_view.html')
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            email_subject = 'Confirm your email to publish your review'

            uidb64 = urlsafe_base64_encode(force_bytes(comment.pk))
            domain = 'https://www.bossingup.net'
            link = reverse('review-activate', kwargs={'uidb64':uidb64, 'token':token_generator.generate_token()})
            activate_url = domain+link


            email_body = 'Hi '+comment.email+ '\n\nPlease click this confirmation link to publish your review on Bossing Up. We value your feedback.\n\n' + activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply.bossingup@gmail.com',
                [comment.email],
            )
            email.send(fail_silently=False)
            messages.success(request, 'Your review submission  was successfully. Please check your email address to activate your review!!!', extra_tags='check')
            return Response({'business': self.object, 'form':form}, template_name='detail_view.html')


class ReviewVerificationView(RetrieveAPIView):
    
    def get(self, request, uidb64, token, *args, **kwargs):
        comment_id = force_text(urlsafe_base64_decode(uidb64))
        comment = Comment.objects.get(pk=comment_id)

        if comment and comment.approved_comment:
            messages.info(request, 'Your review has already been published and you can view it from here.', extra_tags='exists')
            return redirect('business-detail', pk=comment.post.id)
        elif comment:
            comment.approved_comment = True

            if comment.rating == None:
                comment.rating = 0
                comment.post.rating_total += comment.rating
                comment.post.save()
                comment.save()

            else:
                comment.post.rating_total += comment.rating
                comment.post.rating_count +=1
                comment.post.save()
                comment.save()
                
            messages.success(request, 'Your review has successfully been published. We value your feedback!!!', extra_tags='successfully')
            return redirect('business-detail', pk=comment.post.id)
        else:
            messages.error(request, 'Invalid Request!!!', extra_tags='failed')
            return redirect('home')



class ApiAllListView(ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('county', 'category')
    template_name='search_view.html'

    def get(self, request):
        queryset = BlackBusiness.valid_cleaned('self')
        page = request.GET.get('page', 1)

        paginator = Paginator(queryset, 10)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return Response({'businesses': queryset})
