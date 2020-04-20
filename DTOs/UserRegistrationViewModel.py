from application import ma

# This might be a view model that we will use to send the new user data to the server


class UserRegistrationViewModel(ma.ModelSchema):
    class Meta:
        fields = ('name', 'email', 'password', 'sectorId' )
