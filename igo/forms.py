from django import forms
from .models import Review, Comment, Comment1, Comment2, Comment3, Comment4, Comment5, Comment7
from .models import Review1, Review2, Review3, Review4, Review5, Review6, Review7


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ['subject', 'shop_name', 'address', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'shop_name': '가게이름',
            'address': '주소',
            'image': '사진',
            'contents': '내용',
        }


class ReviewForm1(forms.ModelForm):
    class Meta:
        model = Review1
        # fields = '__all__'
        fields = ['subject', 'shop_name', 'address', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'shop_name': '가게이름',
            'address': '주소',
            'image': '사진',
            'contents': '내용',
        }


class ReviewForm2(forms.ModelForm):
    class Meta:
        model = Review2
        # fields = '__all__'
        fields = ['subject', 'shop_name', 'address', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'shop_name': '가게이름',
            'address': '주소',
            'image': '사진',
            'contents': '내용',
        }

class ReviewForm3(forms.ModelForm):
    class Meta:
        model = Review3
        # fields = '__all__'
        fields = ['subject', 'shop_name', 'address', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'shop_name': '가게이름',
            'address': '주소',
            'image': '사진',
            'contents': '내용',
        }

class ReviewForm4(forms.ModelForm):
    class Meta:
        model = Review4
        # fields = '__all__'
        fields = ['subject', 'shop_name', 'address', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'shop_name': '가게이름',
            'address': '주소',
            'image': '사진',
            'contents': '내용',
        }

class ReviewForm5(forms.ModelForm):
    class Meta:
        model = Review5
        # fields = '__all__'
        fields = ['subject', 'shop_name', 'address', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'shop_name': '가게이름',
            'address': '주소',
            'image': '사진',
            'contents': '내용',
        }

class ReviewForm6(forms.ModelForm):
    class Meta:
        model = Review6
        # fields = '__all__'
        fields = ['subject', 'shop_name', 'address', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'shop_name': '가게이름',
            'address': '주소',
            'image': '사진',
            'contents': '내용',
        }


class ReviewForm7(forms.ModelForm):
    class Meta:
        model = Review7
        # fields = '__all__'
        fields = ['subject', 'image', 'contents']

        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(blank=True, upload_to="image", null=True),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """

        labels = {
            'subject': '제목',
            'image': '사진',
            'contents': '내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

class CommentForm1(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

class CommentForm3(forms.ModelForm):
    class Meta:
        model = Comment3
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

class CommentForm4(forms.ModelForm):
    class Meta:
        model = Comment4
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }


class CommentForm5(forms.ModelForm):
    class Meta:
        model = Comment5
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }


class CommentForm7(forms.ModelForm):
    class Meta:
        model = Comment7
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }