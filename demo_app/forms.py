from django import forms
from demo_app.models import Article
from demo_app.models import Author

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        # exclude = ('date_posted')
        fields = ('user', 'no_likes','conent', 'author', 'photo')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = ('name', 'dob', 'address', 'photo')
        # fields = "__all__"



    # user = forms.CharField()
    # no_likes = forms.IntegerField()
    # conent = forms.CharField()