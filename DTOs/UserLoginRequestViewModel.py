

from application import ma


class UserLoginRequestViewModel(ma.ModelSchema):
    class Meta:
        fields = ('email', 'password')