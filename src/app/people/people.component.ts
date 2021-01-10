import {Component} from '@angular/core';
import {peopleGroups, Person} from '../../data/people';


@Component({
  selector: 'app-people',
  templateUrl: './people.component.html',
  styleUrls: ['./people.component.scss']
})
export class PeopleComponent {

  groupsOrder = ['Faculty', 'PhD Student', 'MSc Student', 'Alumni', 'Employee'];
  groups: { [key: string]: Person[] } = peopleGroups;

  constructor() {
    this.groupsOrder.forEach(g => {
      if (g === 'Alumni') {
        this.groups[g] = this.groups[g].sort((a, b) => (a.endYear || 0) < (b.endYear || 0) ? 1 : -1);
      } else {
        this.groups[g] = this.groups[g].sort((a, b) => a.name > b.name ? 1 : -1);
      }
    });
  }

  groupName(group: string) {
    if (group !== 'Faculty' && group !== 'Alumni') {
      return group + 's';
    }
    return group;
  }
}
