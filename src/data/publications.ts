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

function decodeEscapeSequence(s: string) {
  try {
    return decodeURIComponent(s.replace(/\\x/g, "%"));
  } catch (e) {
    return s.replace(/\\x([0-9A-Fa-f]{2,4})/g, function () {
      return String.fromCharCode(parseInt(arguments[1], 16));
    });
  }
}

publications.forEach(p => {
  const year = p.date ? p.date.slice(0, 4) : '';
  if (!(year in publicationsMap)) {
    publicationsMap[year] = [];
  }
  publicationsMap[year].push(p);

  p.authors = p.authors.map(decodeEscapeSequence);
});
