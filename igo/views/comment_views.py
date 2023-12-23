from django.utils import timezone
from pyexpat.errors import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from igo.forms import CommentForm,CommentForm1,CommentForm2,CommentForm3,CommentForm4,CommentForm5, CommentForm7
from igo.models import Review, Review1, Review2, Review3, Review4, Review5,Review7, Comment,Comment1,Comment2,Comment3, Comment4, Comment5,Comment7


@login_required(login_url='common:login')
def comment_create_review(request, review_id):
    """
    igo 질문댓글등록
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('igo:detail', review_id=review.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'igo/comment_form.html', context)



@login_required(login_url='common:login')
def comment_modify_review(request, comment_id):
    """
    pybo 질문댓글수정
    """
    comment1 = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment1.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('igo:detail', review_id=comment1.review.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment1)
        if form.is_valid():
            comment1 = form.save(commit=False)
            comment1.author = request.user
            comment1.modify_date = timezone.now()
            comment1.save()
            return redirect('igo:detail', review_id=comment1.review.id)
    else:
        form = CommentForm(instance=comment1)
    context = {'form': form}
    return render(request, 'igo/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_review(request, comment_id):
    """
    igo 질문댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('igo:detail', review_id=comment.review.id)
    else:
        comment.delete()
    return redirect('igo:detail', review_id=comment.review.id)


#2
@login_required(login_url='common:login')
def comment_create_review1(request, review_id1):
    """
    igo 질문댓글등록
    """
    review = get_object_or_404(Review1, pk=review_id1)
    if request.method == "POST":
        form = CommentForm1(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('igo:detail1', review_id1=review.id)
    else:
        form = CommentForm1()
    context = {'form': form}
    return render(request, 'igo/comment_form1.html', context)


@login_required(login_url='common:login')
def comment_modify_review1(request, comment_id1):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment1, pk=comment_id1)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('igo:detail1', review_id1=comment.review.id)

    if request.method == "POST":
        form = CommentForm1(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('igo:detail1', review_id1=comment.review.id)
    else:
        form = CommentForm1(instance=comment)
    context = {'form': form}
    return render(request, 'igo/comment_form1.html', context)


@login_required(login_url='common:login')
def comment_delete_review1(request, comment_id1):
    """
    igo 질문댓글삭제
    """
    comment = get_object_or_404(Comment1, pk=comment_id1)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('igo:detail1', review_id1=comment.review.id)
    else:
        comment.delete()
    return redirect('igo:detail1', review_id1=comment.review.id)


#3
@login_required(login_url='common:login')
def comment_create_review2(request, review_id2):
    """
    igo 질문댓글등록
    """
    review = get_object_or_404(Review2, pk=review_id2)
    if request.method == "POST":
        form = CommentForm2(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('igo:detail2', review_id2=review.id)
    else:
        form = CommentForm2()
    context = {'form': form}
    return render(request, 'igo/comment_form2.html', context)



@login_required(login_url='common:login')
def comment_modify_review2(request, comment_id2):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment2, pk=comment_id2)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('igo:detail2', review_id2=comment.review.id)

    if request.method == "POST":
        form = CommentForm2(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('igo:detail2', review_id2=comment.review.id)
    else:
        form = CommentForm2(instance=comment)
    context = {'form': form}
    return render(request, 'igo/comment_form2.html', context)


@login_required(login_url='common:login')
def comment_delete_review2(request, comment_id2):
    """
    igo 질문댓글삭제
    """
    comment = get_object_or_404(Comment2, pk=comment_id2)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('igo:detail2', review_id2=comment.review.id)
    else:
        comment.delete()
    return redirect('igo:detail2', review_id2=comment.review.id)


#4
@login_required(login_url='common:login')
def comment_create_review3(request, review_id3):
    """
    igo 질문댓글등록
    """
    review = get_object_or_404(Review3, pk=review_id3)
    if request.method == "POST":
        form = CommentForm3(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('igo:detail3', review_id3=review.id)
    else:
        form = CommentForm3()
    context = {'form': form}
    return render(request, 'igo/comment_form3.html', context)



@login_required(login_url='common:login')
def comment_modify_review3(request, comment_id3):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment3, pk=comment_id3)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('igo:detail3', review_id3=comment.review.id)

    if request.method == "POST":
        form = CommentForm3(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('igo:detail3', review_id3=comment.review.id)
    else:
        form = CommentForm3(instance=comment)
    context = {'form': form}
    return render(request, 'igo/comment_form3.html', context)


@login_required(login_url='common:login')
def comment_delete_review3(request, comment_id3):
    """
    igo 질문댓글삭제
    """
    comment = get_object_or_404(Comment3, pk=comment_id3)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('igo:detail3', review_id3=comment.review.id)
    else:
        comment.delete()
    return redirect('igo:detail3', review_id3=comment.review.id)



#5
@login_required(login_url='common:login')
def comment_create_review4(request, review_id4):
    """
    igo 질문댓글등록
    """
    review = get_object_or_404(Review4, pk=review_id4)
    if request.method == "POST":
        form = CommentForm4(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('igo:detail4', review_id4=review.id)
    else:
        form = CommentForm4()
    context = {'form': form}
    return render(request, 'igo/comment_form4.html', context)


@login_required(login_url='common:login')
def comment_modify_review4(request, comment_id4):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment4, pk=comment_id4)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('igo:detail4', review_id4=comment.review.id)

    if request.method == "POST":
        form = CommentForm4(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('igo:detail4', review_id4=comment.review.id)
    else:
        form = CommentForm4(instance=comment)
    context = {'form': form}
    return render(request, 'igo/comment_form4.html', context)


@login_required(login_url='common:login')
def comment_delete_review4(request, comment_id4):
    """
    igo 질문댓글삭제
    """
    comment = get_object_or_404(Comment4, pk=comment_id4)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('igo:detail4', review_id4=comment.review.id)
    else:
        comment.delete()
    return redirect('igo:detail4', review_id4=comment.review.id)


#6
@login_required(login_url='common:login')
def comment_create_review5(request, review_id5):
    """
    igo 질문댓글등록
    """
    review = get_object_or_404(Review5, pk=review_id5)
    if request.method == "POST":
        form = CommentForm5(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('igo:detail5', review_id5=review.id)
    else:
        form = CommentForm5()
    context = {'form': form}
    return render(request, 'igo/comment_form5.html', context)


@login_required(login_url='common:login')
def comment_modify_review5(request, comment_id5):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment5, pk=comment_id5)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('igo:detail5', review_id5=comment.review.id)

    if request.method == "POST":
        form = CommentForm5(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('igo:detail5', review_id5=comment.review.id)
    else:
        form = CommentForm5(instance=comment)
    context = {'form': form}
    return render(request, 'igo/comment_form5.html', context)


@login_required(login_url='common:login')
def comment_delete_review5(request, comment_id5):
    """
    igo 질문댓글삭제
    """
    comment = get_object_or_404(Comment5, pk=comment_id5)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('igo:detail5', review_id5=comment.review.id)
    else:
        comment.delete()
    return redirect('igo:detail5', review_id5=comment.review.id)


# 공지(notion)
#2
@login_required(login_url='common:login')
def comment_create_review7(request, review_id7):
    """
    igo 질문댓글등록
    """
    review = get_object_or_404(Review7, pk=review_id7)
    if request.method == "POST":
        form = CommentForm7(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('igo:detail7', review_id7=review.id)
    else:
        form = CommentForm7()
    context = {'form': form}
    return render(request, 'igo/comment_form7.html', context)


@login_required(login_url='common:login')
def comment_modify_review7(request, comment_id7):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(Comment7, pk=comment_id7)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('igo:detail7', review_id7=comment.review.id)

    if request.method == "POST":
        form = CommentForm7(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('igo:detail7', review_id7=comment.review.id)
    else:
        form = CommentForm7(instance=comment)
    context = {'form': form}
    return render(request, 'igo/comment_form7.html', context)


@login_required(login_url='common:login')
def comment_delete_review7(request, comment_id7):
    """
    igo 질문댓글삭제
    """
    comment = get_object_or_404(Comment7, pk=comment_id7)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('igo:detail7', review_id7=comment.review.id)
    else:
        comment.delete()
    return redirect('igo:detail7', review_id7=comment.review.id)