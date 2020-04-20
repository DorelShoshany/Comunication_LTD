

from application import ma


class UserLoginRequestViewModel(ma.ModelSchema):
    class Meta:
        fields = ('id', 'email', 'passwordChangedDate', 'firstName', 'lastName', 'creationDate', 'sectorId')
