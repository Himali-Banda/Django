from django.contrib.auth.forms import UserCreationForm
from ..models import UserModel
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=UserModel\
        fields=('username','first_name','last_name','email','userProfile')
