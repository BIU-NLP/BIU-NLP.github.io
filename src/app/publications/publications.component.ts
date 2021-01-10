import {Component} from '@angular/core';
import {publicationsMap} from '../../data/publications';

@Component({
  selector: 'app-publications',
  templateUrl: './publications.component.html',
  styleUrls: ['./publications.component.scss']
})
export class PublicationsComponent {

  publicationsMap = publicationsMap;
  years: string[] = Object.keys(this.publicationsMap).sort().reverse();

}
