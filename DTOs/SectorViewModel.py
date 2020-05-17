from application import ma


class SectorViewModel(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'description')
