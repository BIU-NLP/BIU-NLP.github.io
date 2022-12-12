# Lab Website (biu-nlp.github.io)
This repo contains the source code for the lab's website

## Development
```shell script
npm install
npm start
```

### Adding Photos
Add people photos to the root directory `people`.

For local development, run `python extra/images/people_photos.py` to convert formats and image sizes.
Images are cropped to a square around a detected face, so all faces are centered and in a similar size
(This happens automatically during deployment)

### Adding Publications
To refresh the publications list, clone the repo, and run:
```bash
python3 extra/publications.py
python3 extra/publications_json.py
```
If your publications don't show, add the `scholarId` to your person in `people.json`.

To ignore a publication, add the publication ID to the `pubs_ignore` set in `extra/publications_json.py`.



## Deployment
Automatic deployment using github pages.

Don't forget to push new files in the `extra/publications/` directory.
