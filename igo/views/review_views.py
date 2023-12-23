
from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from igo.forms import ReviewForm, ReviewForm1, ReviewForm2, ReviewForm3, ReviewForm4, ReviewForm5, ReviewForm6, ReviewForm7
from igo.models import Review, Review1, Review2, Review3, Review4, Review5, Review7


@login_required(login_url='common:login')
def review_create(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'igo/review_form.html', context)


@login_required(login_url='common:login')
def review_create1(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm1(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index1')
    else:
        form = ReviewForm1()
    context = {'form': form}
    return render(request, 'igo/review_form_snack_bar.html', context)


@login_required(login_url='common:login')
def review_create2(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm2(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index2')
    else:
        form = ReviewForm2()
    context = {'form': form}
    return render(request, 'igo/review_form_korea_food.html', context)


@login_required(login_url='common:login')
def review_create3(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm3(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index3')
    else:
        form = ReviewForm3()
    context = {'form': form}
    return render(request, 'igo/review_form_japan.html', context)


@login_required(login_url='common:login')
def review_create4(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm4(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index4')
    else:
        form = ReviewForm4()
    context = {'form': form}
    return render(request, 'igo/review_form_china.html', context)


@login_required(login_url='common:login')
def review_create5(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm5(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index5')
    else:
        form = ReviewForm5()
    context = {'form': form}
    return render(request, 'igo/review_form_cafe.html', context)


@login_required(login_url='common:login')
def review_modify(request, review_id):
    """
    igo 질문수정
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('igo:detail', review_id=review.id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('igo:detail', review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'igo/modify.html', context)


@login_required(login_url='common:login')
def review_modify1(request, review_id1):
    """
    igo 질문수정
    """
    review = get_object_or_404(Review1, pk=review_id1)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('igo:detail1', review_id1=review.id)

    if request.method == "POST":
        form = ReviewForm1(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('igo:detail1', review_id1=review.id)
    else:
        form = ReviewForm1(instance=review)
    context = {'form': form}
    return render(request, 'igo/modify1.html', context)


@login_required(login_url='common:login')
def review_modify2(request, review_id2):
    """
    igo 질문수정
    """
    review = get_object_or_404(Review2, pk=review_id2)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('igo:detail2', review_id2=review.id)

    if request.method == "POST":
        form = ReviewForm2(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('igo:detail2', review_id2=review.id)
    else:
        form = ReviewForm2(instance=review)
    context = {'form': form}
    return render(request, 'igo/modify2.html', context)


@login_required(login_url='common:login')
def review_modify3(request, review_id3):
    """
    igo 질문수정
    """
    review = get_object_or_404(Review3, pk=review_id3)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('igo:detail3', review_id3=review.id)

    if request.method == "POST":
        form = ReviewForm3(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('igo:detail3', review_id3=review.id)
    else:
        form = ReviewForm3(instance=review)
    context = {'form': form}
    return render(request, 'igo/modify3.html', context)


@login_required(login_url='common:login')
def review_modify4(request, review_id4):
    """
    igo 질문수정
    """
    review = get_object_or_404(Review4, pk=review_id4)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('igo:detail4', review_id4=review.id)

    if request.method == "POST":
        form = ReviewForm4(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('igo:detail4', review_id4=review.id)
    else:
        form = ReviewForm4(instance=review)
    context = {'form': form}
    return render(request, 'igo/modify4.html', context)


@login_required(login_url='common:login')
def review_modify5(request, review_id5):
    """
    igo 질문수정
    """
    review = get_object_or_404(Review5, pk=review_id5)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('igo:detail5', review_id5=review.id)

    if request.method == "POST":
        form = ReviewForm5(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('igo:detail5', review_id5=review.id)
    else:
        form = ReviewForm5(instance=review)
    context = {'form': form}
    return render(request, 'igo/modify5.html', context)


@login_required(login_url='common:login')
def review_delete(request, review_id):
    """
    igo 질문삭제
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('igo:detail', review_id=review.id)
    review.delete()
    return redirect('igo:index')


@login_required(login_url='common:login')
def review_delete1(request, review_id1):
    """
    igo 질문삭제
    """
    review = get_object_or_404(Review1, pk=review_id1)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('igo:detail1', review_id1=review.id)
    review.delete()
    return redirect('igo:index1')


@login_required(login_url='common:login')
def review_delete2(request, review_id2):
    """
    igo 질문삭제
    """
    review = get_object_or_404(Review2, pk=review_id2)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('igo:detail2', review_id2=review.id)
    review.delete()
    return redirect('igo:index2')


@login_required(login_url='common:login')
def review_delete3(request, review_id3):
    """
    igo 질문삭제
    """
    review = get_object_or_404(Review3, pk=review_id3)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('igo:detail3', review_id3=review.id)
    review.delete()
    return redirect('igo:index3')


@login_required(login_url='common:login')
def review_delete4(request, review_id4):
    """
    igo 질문삭제
    """
    review = get_object_or_404(Review4, pk=review_id4)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('igo:detail4', review_id4=review.id)
    review.delete()
    return redirect('igo:index4')


@login_required(login_url='common:login')
def review_delete5(request, review_id5):
    """
    igo 질문삭제
    """
    review = get_object_or_404(Review5, pk=review_id5)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('igo:detail5', review_id5=review.id)
    review.delete()
    return redirect('igo:index5')


@login_required(login_url='common:login')
def review_create_best(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm6(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index_best')
    else:
        form = ReviewForm6()
    context = {'form': form}
    return render(request, 'igo/review_form_best.html', context)


# 공지(notion)
@login_required(login_url='common:login')
def review_create7(request):

    """
    form = ReviewForm()
    return render(request, 'igo/review_form.html', {'form': form})
    """

    if request.method == 'POST':
        form = ReviewForm7(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # 추가한 속성 author 적용
            review.create_date = timezone.now()
            review.save()
            return redirect('igo:index7')
    else:
        form = ReviewForm7()
    context = {'form': form}
    return render(request, 'igo/notion_form.html', context)


@login_required(login_url='common:login')
def review_modify7(request, review_id7):
    """
    igo 질문수정
    """
    review = get_object_or_404(Review7, pk=review_id7)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('igo:detail7', review_id7=review.id)

    if request.method == "POST":
        form = ReviewForm7(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('igo:detail7', review_id7=review.id)
    else:
        form = ReviewForm7(instance=review)
    context = {'form': form}
    return render(request, 'igo/modify7.html', context)


@login_required(login_url='common:login')
def review_delete7(request, review_id7):
    """
    igo 질문삭제
    """
    review = get_object_or_404(Review7, pk=review_id7)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('igo:detail7', review_id7=review.id)
    review.delete()
    return redirect('igo:index7')