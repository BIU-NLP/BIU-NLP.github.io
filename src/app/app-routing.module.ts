import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {MainComponent} from './main/main.component';
import {PublicationsComponent} from './publications/publications.component';
import {PeopleComponent} from './people/people.component';
import {ResourcesComponent} from './resources/resources.component';
import {PersonComponent} from './people/person/person.component';

const routes: Routes = [
  {
    path: '',
    component: MainComponent
  }, {
    path: 'people',
    component: PeopleComponent
  }, {
    path: 'people/:id',
    component: PersonComponent
  }, {
    path: 'publications',
    component: PublicationsComponent
  }, {
    path: 'resources',
    component: ResourcesComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
