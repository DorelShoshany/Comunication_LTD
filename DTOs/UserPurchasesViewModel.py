from application import ma


class UserPurchasesViewModel(ma.ModelSchema):
    class Meta:
        fields = ('id','name', 'price')