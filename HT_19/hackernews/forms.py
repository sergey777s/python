from django import forms


class NewsChooser(forms.Form):
    newsType = forms.ChoiceField(choices=(('ask', 'asknews'), ('show', 'shownews'), ('new', 'newnews'), ('job', 'jobnews'),))