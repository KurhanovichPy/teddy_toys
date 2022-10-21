from django.forms import ModelForm, CharField, Textarea, Form


class ReviewForm(Form):
    body = CharField(widget=Textarea(attrs={'class': 'text-review',
                                            'placeholder': 'Введите комментарий',
                                            'rows': 5}))
