from django import forms


class CommentForm(forms.Form):
    user_name = forms.CharField(max_length=30, label='Your Name')
    comment = forms.CharField(label='Your Comment for this Book', widget=forms.Textarea, max_length=200)
