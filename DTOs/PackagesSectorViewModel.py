

from application import ma


class PackagesSectorViewModel(ma.ModelSchema):
    class Meta:
        fields = ('id','name', 'price')

#'packageId', 'sectorId',