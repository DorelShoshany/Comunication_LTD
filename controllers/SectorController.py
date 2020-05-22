from DTOs.SectorViewModel import SectorViewModel
from entities.Sectors import Sectors
from services.DAL import DAL, SectorProivder
from services.Validators import form_is_full


class SectorController():

    def create_sector(self, request):
        sector_form = request.json if request.is_json else request.form
        sector_dict = dict(sector_form)
        sector_fields = ['name', 'description']
        sector_res = form_is_full(sector_dict, sector_fields)
        if sector_res.isSuccess:
            sector = Sectors(name=sector_dict['name'], description=sector_dict['description'])
            DAL.save_new_sector_to_db(sector)
            return True
        else:
            sector_res.isSuccess


    def get_all_sectors(self):
        sectors = SectorProivder.get_sectors_from_db()
        sectorViewModel = SectorViewModel(many=True)
        return sectorViewModel.dump(sectors)
