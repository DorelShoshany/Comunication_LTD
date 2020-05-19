from DTOs.PackagesSectorViewModel import PackagesSectorViewModel
from DTOs.UserPurchasesViewModel import UserPurchasesViewModel
from entities.PackagesSectors import PackagesSectors
from flask import  json

from entities.UserPurchases import UserPurchases
from services.DAL import DAL, PackagesSectorsProvider
from services.DAL.DAL import get_packages_sectors_from_db_by_sector_id
from services.DAL.UserProvider import get_user_from_db_by_id




class PackagesSectorController():
    def createPackagesSector(self, request):
        if request.is_json:
            packageId = request.json['packageId']
            sectorId = request.json['sectorId']
            price = request.json['price']
            name = request.json['name']
        else:
            packageId = request.form['packageId']
            sectorId = request.form['sectorId']
            price = request.form['price']
            name = request.form['name']
        packagesSector = PackagesSectors(packageId=packageId, sectorId=sectorId, price=price, name=name)
        DAL.save_new_packages_sectors_to_db(packagesSector)

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


