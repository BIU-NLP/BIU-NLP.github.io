import {Component, Input} from '@angular/core';
import {Publication} from '../../../data/publications';
import {peopleMap} from '../../../data/people';

@Component({
  selector: 'app-publications-list',
  templateUrl: './publications-list.component.html',
  styleUrls: ['./publications-list.component.scss']
})
export class PublicationsListComponent {

  @Input() publications: Publication[] = [];

  peopleMap = peopleMap;
}
