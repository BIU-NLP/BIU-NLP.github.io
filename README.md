# How to compile the website locally:

## Install prerequisites:
~~~~
sudo gem install jekyll
sudo gem install github-pages
~~~~

## Activate locally:
~~~~
cd biu-nlp-site
jekyll build --watch &
jekyll serve
~~~~

## Preview on browser:
Visit http://localhost:4000/

# Other How-to's:

## Add a new student:
Edit _data/phd_students.yaml or _data/master_students.yaml 

The photos should be under assets/img/students/

## Add a new publication:
Edit _data/publications.yaml

## Add a new resource:
Fork your personal github repository to [this repository](https://github.com/BIU-NLP) (ask Yoav or Dudi to add you as a member).


For more tutorial materials on jekyll see: http://jekyllrb.com/docs/usage/

Based on [this website](https://github.com/callison-burch/callison-burch.github.io) by Chris Callison-Burch.
