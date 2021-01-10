import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {MainComponent} from './main/main.component';
import {PeopleComponent} from './people/people.component';
import {PublicationsComponent} from './publications/publications.component';
import {ResourcesComponent} from './resources/resources.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {PersonComponent} from './people/person/person.component';
import {PersonCardComponent} from './people/person-card/person-card.component';
import {PublicationsListComponent} from './publications/publications-list/publications-list.component';
import {MatTooltipModule} from '@angular/material/tooltip';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    PeopleComponent,
    PublicationsComponent,
    ResourcesComponent,
    PersonComponent,
    PersonCardComponent,
    PublicationsListComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatTooltipModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
