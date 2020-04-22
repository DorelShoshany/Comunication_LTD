from DTOs.PackagesSectorViewModel import PackagesSectorViewModle
from entities.PackagesSectors import PackagesSectors
from services.DAL import DAL
from services.DAL.DAL import get_packages_sectors_from_db_by_sectorId
from services.DAL.UserProvider import get_user_from_db_by_id


class PackagesSectorController():
    def createPackagesSector(self, request):
        if request.is_json:
            packageId = request.json['packageid']
            sectorId = request.json['sectorid']
            price = request.json['price']
        else:
            packageId = request.form['packageid']
            sectorId = request.form['sectorid']
            price = request.form['price']
        packagesSector = PackagesSectors(packageId=packageId, sectorId=sectorId, price=price)
        DAL.save_new_packages_sectors_to_db(packagesSector)


    def get_all_packages_to_buy_by_sector_id(self, userId):
        user = get_user_from_db_by_id(userId)
        packagesSectorsList = get_packages_sectors_from_db_by_sectorId(user.sectorId)
        packagesSectorViewModel = PackagesSectorViewModle(many=True)
        return packagesSectorViewModel.dump(packagesSectorsList)