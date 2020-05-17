from entities.Sectors import Sectors
from services.DAL import DAL, SectorProivder


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

    def get_all_sectors(self):
        return SectorProivder.get_sectors_from_db()