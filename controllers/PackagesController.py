from entities.Packages import Packages
from services.DAL import DAL


class PackagesController():
    def createPackages(self, request):
        if request.is_json:
            name = request.json['name']
        else:
            name = request.form['name']
        package = Packages(name=name)
        DAL.save_new_package_to_db(package)