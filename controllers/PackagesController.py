from entities.Packages import Packages
from services.DAL import DAL
from services.Validators import form_is_full


class PackagesController():

    def create_packages(self, request):
        package_form = request.json if request.is_json else request.form
        package_dict = dict(package_form)
        package_fields = ['name']
        package_res = form_is_full(package_dict, package_fields)
        if package_res.isSuccess:
            package = Packages(name=package_dict['name'])
            if DAL.save_new_package_to_db(package):
                return True
        return package_res.isSuccess