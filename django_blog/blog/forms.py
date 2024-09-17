from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post, Tag, Comment
from django.forms.widgets import CheckboxSelectMultiple

class TagWidget():
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter tags separated by commas'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def format_value(self, value):
        if value is None:
            return ''
        if isinstance(value, list):
            return ', '.join([str(v) for v in value])
        return value

# User Registration Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Post Form with Tags
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Custom form validation for PostForm
def form_valid(self, form):
    form.instance.author = self.request.user
    tags = form.cleaned_data['tags']
    form.instance.save()
    form.instance.tags.set(tags)
    return super().form_valid(form)
