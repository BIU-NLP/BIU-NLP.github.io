// @ts-ignore
import PEOPLE_GROUPS from './people.json';

export interface Person {
  id: string;
  name: string;
  endYear?: number;
  aliases?: string[];
  degree: string;
  group: string;
  role?: string;
  homepage?: string;
  advisors?: string[];
  image?: boolean;
  imagePath: string;
  interests?: string;
  current?: {
    position: string;
    employer: string;
  }
}

export const peopleGroups = PEOPLE_GROUPS as { [key: string]: Person[] };

export const peopleMap: { [key: string]: Person } = {};

export const people: Person[] = [];

for (const group of Object.values(peopleGroups)) {
  for (const person of group) {
    peopleMap[person.name] = person;
    person.id = person.name.toLowerCase().replace(/ /g, '_');
    person.imagePath = ('image' in person && !person.image) ? 'unknown' : person.id;

    if (person.aliases) {
      for (const alias of person.aliases) {
        peopleMap[alias] = person
      }
    }
    people.push(person);
  }
}
