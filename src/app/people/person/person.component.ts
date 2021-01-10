import {Component, OnInit} from '@angular/core';
import {people, Person} from '../../../data/people';
import {ActivatedRoute, Router} from '@angular/router';
import {publications} from '../../../data/publications';

@Component({
  selector: 'app-person',
  templateUrl: './person.component.html',
  styleUrls: ['./person.component.scss']
})
export class PersonComponent implements OnInit {

  person?: Person;
  publications: any[] = [];

  constructor(private route: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      const id = params.id;
      const person = people.find(p => p.id === id);
      if (!person) {
        this.router.navigate(['/people']);
      } else {
        this.person = person;
        const names = [this.person.name].concat(this.person.aliases || [])
        this.publications = publications.filter(p => names.some(n => p.authors.indexOf(n) > -1));
      }
    });
  }

}
