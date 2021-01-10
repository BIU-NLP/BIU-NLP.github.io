// @ts-ignore
import PUBLICATIONS from './publications.json';

export interface Publication {
  title: string;
  url: string;
  authors: string[];
  date: string;
  journal?: string;
  abstract?: string;
}

export const publications = (PUBLICATIONS as Publication[]);

export const publicationsMap: { [key: string]: Publication[] } = {};

publications.forEach(p => {
  const year = p.date ? p.date.slice(0, 4) : '';
  if (!(year in publicationsMap)) {
    publicationsMap[year] = [];
  }
  publicationsMap[year].push(p);
});
