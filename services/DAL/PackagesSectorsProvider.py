from entities.PackagesSectors import PackagesSectors


def get_packages_sector_by_id(packagesSectorsId):
    return PackagesSectors.query.filter_by(id=packagesSectorsId).first()
