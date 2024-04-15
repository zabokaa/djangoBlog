from django import forms
from .models import Comment



# We created a class called CommentForm that inherited from Django's forms.ModelForm class. Because this class is inherited from a built-in Django class, we can simply use the Meta class to tell the ModelForm class what models and fields we want in our form. form.ModelForm will then build this for us.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
# We included the body field for the user to complete. This field was imported from the Comment model . We didn't need to include the other fields because the post, user and created_on fields in our model are filled in automatically, and the approved field is managed by the superuser.
        fields = ('body',)

