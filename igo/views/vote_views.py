from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from igo.models import Review,Review1,Review2,Review3,Review4,Review5,Review7


@login_required(login_url='common:login')
def vote_review(request, review_id):
    """
    pybo 질문추천등록
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        review.voter.add(request.user)
    return redirect('igo:detail', review_id=review.id)

@login_required(login_url='common:login')
def vote_review1(request, review_id1):
    """
    pybo 질문추천등록
    """
    review = get_object_or_404(Review1, pk=review_id1)
    if request.user == review.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        review.voter.add(request.user)
    return redirect('igo:detail1', review_id1=review.id)

@login_required(login_url='common:login')
def vote_review2(request, review_id2):
    """
    pybo 질문추천등록
    """
    review = get_object_or_404(Review2, pk=review_id2)
    if request.user == review.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        review.voter.add(request.user)
    return redirect('igo:detail2', review_id2=review.id)

@login_required(login_url='common:login')
def vote_review3(request, review_id3):
    """
    pybo 질문추천등록
    """
    review = get_object_or_404(Review3, pk=review_id3)
    if request.user == review.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        review.voter.add(request.user)
    return redirect('igo:detail3', review_id3=review.id)

@login_required(login_url='common:login')
def vote_review4(request, review_id4):
    """
    pybo 질문추천등록
    """
    review = get_object_or_404(Review4, pk=review_id4)
    if request.user == review.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        review.voter.add(request.user)
    return redirect('igo:detail4', review_id4=review.id)

@login_required(login_url='common:login')
def vote_review5(request, review_id5):
    """
    pybo 질문추천등록
    """
    review = get_object_or_404(Review5, pk=review_id5)
    if request.user == review.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        review.voter.add(request.user)
    return redirect('igo:detail5', review_id5=review.id)


# 공지(notion)
@login_required(login_url='common:login')
def vote_review7(request, review_id7):
    """
    pybo 질문추천등록
    """
    review = get_object_or_404(Review7, pk=review_id7)
    if request.user == review.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        review.voter.add(request.user)
    return redirect('igo:detail7', review_id7=review.id)
