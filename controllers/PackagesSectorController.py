from entities.PackagesSectors import PackagesSectors
from services.DAL import DAL


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

