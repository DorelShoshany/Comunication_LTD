from DTOs.PackagesSectorViewModel import PackagesSectorViewModel
from DTOs.UserPurchasesViewModel import UserPurchasesViewModel
from entities.PackagesSectors import PackagesSectors
from flask import  json

from entities.UserPurchases import UserPurchases
from services.DAL import DAL, PackagesSectorsProvider
from services.DAL.DAL import get_packages_sectors_from_db_by_sector_id
from services.DAL.UserProvider import get_user_from_db_by_id
from services.Validators import form_is_full


class PackagesSectorController():

    def create_packages_sector(self, request):
        packages_sector_form = request.json if request.is_json else request.form
        packages_sector_dict = dict(packages_sector_form)
        packages_sector_fields = ['packageId','sectorId','price','name']
        packages_sector_res = form_is_full(packages_sector_dict, packages_sector_fields)
        if packages_sector_res.isSuccess:
            packagesSector = PackagesSectors(
                packageId=packages_sector_dict['packageId'],
                sectorId=packages_sector_dict['sectorId'],
                price=packages_sector_dict['price'],
                name=packages_sector_dict['name'])
            if DAL.save_new_packages_sectors_to_db(packagesSector):
                return True
        return False


    def get_all_packages_to_buy_by_sector_id(self, userId):
        user = get_user_from_db_by_id(userId)
        packagesSectorsList = get_packages_sectors_from_db_by_sector_id(user.sectorId)
        packagesSectorViewModel = PackagesSectorViewModel(many=True)
        return packagesSectorViewModel.dump(packagesSectorsList)

    def get_all_packages_that_user_purchases(self, user_id):
        userPurchasesList = DAL.get_purchases_by_user_id(user_id)
        userPurchasesViewModel = UserPurchasesViewModel(many=True)
        return userPurchasesViewModel.dump(userPurchasesList)


    def add_purchase_to_user(self, user_id, request):
        if request.is_json:
            packagesSectorsId = request.json['id']
        else:
            packagesSectorsId = request.form['id']
        packagesSectors = PackagesSectorsProvider.get_packages_sector_by_id(packagesSectorsId)
        userPurchases = UserPurchases(user_id=(int)(user_id), packagesSectorsId=packagesSectorsId,
                                      price=packagesSectors.price, name=packagesSectors.name)
        if DAL.save_new_purchase_to_db(userPurchases):
            return True
        else:
            return False


