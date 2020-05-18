from DTOs.SectorViewModel import SectorViewModel
from entities.Sectors import Sectors


def get_sector_by_id(sectorId):
    sector = Sectors.query.filter_by(id=sectorId).first()
    return Sectors.query.filter_by(id=sectorId).first()


def get_sectors_from_db():
    return Sectors.query.all()
