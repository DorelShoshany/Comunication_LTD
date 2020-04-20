from entities.Sectors import Sectors
from services.DAL import DAL


class SectorController():
    def createSector(self, request):
        if request.is_json:
            name = request.json['name']
            description = request.json['description']
        else:
            name = request.form['name']
            description = request.form['description']
        sector = Sectors(name=name, description=description)
        DAL.save_new_sector_to_db(sector)