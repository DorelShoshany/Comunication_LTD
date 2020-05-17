import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Sector } from 'src/app/models/sector';


@Component({
  selector: 'app-sector-selection-list',
  templateUrl: './sector-selection-list.component.html',
  styleUrls: ['./sector-selection-list.component.scss']
})
export class SectorSelectionListComponent implements OnInit {
  public sectors: Sector[]
  public selectedSector: Sector;

  @Output()
  public valueChanged = new EventEmitter<Sector>();

  constructor(private httpClient: HttpClient) {
    this.loadSectors();
  }

  ngOnInit(): void {

  }

  private async loadSectors() {
    const url = '/api/getSectors';
    this.sectors = await this.httpClient.get<Sector[]>(url).toPromise();
  }

}
