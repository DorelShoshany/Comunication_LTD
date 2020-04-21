

from application import ma


class PackagesSectorViewModle(ma.ModelSchema):
    class Meta:
        fields = ('packageid', 'sectorId', 'price')
