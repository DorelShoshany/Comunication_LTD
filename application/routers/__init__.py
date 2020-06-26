from controllers.AuthorizationController import AuthorizationController
from controllers.PackagesController import PackagesController
from controllers.PackagesSectorController import PackagesSectorController
from controllers.RegistrationController import RegistrationController
from controllers.SectorController import SectorController


# init all controllers once:

packagesSectorController = PackagesSectorController()
authorizationController = AuthorizationController()
registrationController = RegistrationController()
packagesSectorController = PackagesSectorController()
packagesController = PackagesController()
sectorController = SectorController()