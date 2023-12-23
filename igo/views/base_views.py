from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from igo.models import Review, Review1, Review2, Review3, Review4, Review5, Review6, Review7


def realindex(request):
    return render(request, 'igo/review_reallist.html')


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'igo/review_list.html', context)


def index1(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review1.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'igo/review_list_snack_bar.html', context)


def index2(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review2.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'igo/review_list_korea_food.html', context)


def index3(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review3.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'igo/review_list_japan.html', context)


def index4(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review4.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'igo/review_list_china.html', context)


def index5(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review5.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'igo/review_list_cafe.html', context)


def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'igo/review_detail.html', context)


def detail1(request, review_id1):
    review = get_object_or_404(Review1, pk=review_id1)
    context = {'review': review}
    return render(request, 'igo/review_detail_snack_bar.html', context)


def detail2(request, review_id2):
    review = get_object_or_404(Review2, pk=review_id2)
    context = {'review': review}
    return render(request, 'igo/review_detail_korea_food.html', context)


def detail3(request, review_id3):
    review = get_object_or_404(Review3, pk=review_id3)
    context = {'review': review}
    return render(request, 'igo/review_detail_japan.html', context)


def detail4(request, review_id4):
    review = get_object_or_404(Review4, pk=review_id4)
    context = {'review': review}
    return render(request, 'igo/review_detail_china.html', context)


def detail5(request, review_id5):
    review = get_object_or_404(Review5, pk=review_id5)
    context = {'review': review}
    return render(request, 'igo/review_detail_cafe.html', context)


def index_best(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review6.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'igo/family_list_detail.html', context)


def detail_best(request, review_id6):
    review = get_object_or_404(Review6, pk=review_id6)
    context = {'review': review}
    return render(request, 'igo/family_list_detail.html', context)

# 공지(notion)
def index7(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review7.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(review_list, 6)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj, 'page': page}
    return render(request, 'igo/notion_list.html', context)


def detail7(request, review_id7):
    review = get_object_or_404(Review7, pk=review_id7)
    context = {'review': review}
    return render(request, 'igo/notion_detail.html', context)