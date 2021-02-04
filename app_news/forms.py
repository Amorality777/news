from .models import News, Comments
from django.forms import ModelForm


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'status']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['username', 'comment']