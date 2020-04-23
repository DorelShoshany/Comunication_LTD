

from application import ma


class PackagesSectorViewModel(ma.ModelSchema):
    class Meta:
        fields = ('packageid', 'sectorId', 'price')
