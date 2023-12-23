from django.shortcuts import render


def list(request):
    return render(request, 'igo/family_list.html')


def list1(request):
    return render(request, 'igo/friend_list.html')


def list2(request):
    return render(request, 'igo/cj_list.html')


def list3(request):
    return render(request, 'igo/famous_list.html')


def list_detail(request):
    return render(request, 'igo/family_list_detail.html')


def list_detail1(request):
    return render(request, 'igo/friend_list_detail.html')


def list_detail2(request):
    return render(request, 'igo/cj_list_detail.html')


def list_detail3(request):
    return render(request, 'igo/famous_list_detail.html')
