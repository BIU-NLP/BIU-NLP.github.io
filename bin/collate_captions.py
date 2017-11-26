import csv
import re

# load the info about the documents
doc_info = {}
with open('captions.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	headers = {}

	for i, header in enumerate(reader.next()):
		headers[header] = i
	for row in reader:
		num_items = int(row[headers['Input.num_items']])
		for i in range(0, num_items):
			id = row[headers['Input.id_' + str(i)]]
			if not id in doc_info:
				doc_info[id] = {}
			type = row[headers['Input.type_' + str(i)]]
			num = row[headers['Input.num_' + str(i)]]
			caption = row[headers['Answer.caption_' + str(i)]]

			if caption != '{}':
				#print id, type, num, caption
				doc_info[id][type + " " + num] = caption


publications_data = list(open("/Users/ccb/Sites/callison-burch.github.io/_data/publications.yaml-backup"))

path_to_publications = "/Users/ccb/Sites/callison-burch.github.io/publications/"

for line in publications_data:
	print line,
	if line.startswith("   id: "):
		id = line[7:len(line)-1]
		if id in doc_info:
			print "   figures:"
			full_text = " ".join(list(open(path_to_publications + id + ".txt")))

			uniq_items = set()
			ordered_items = []
			results = re.findall("Table \d+|Figure \d+", full_text)
			for item in results:
				if item not in uniq_items:
					uniq_items.add(item)
					ordered_items.append(item)
			for item in ordered_items:
		       		if item in doc_info[id]:
		       			caption = doc_info[id][item]
					pattern = re.compile(r'\s+')
					caption = re.sub(pattern, ' ', caption)
					print "      -"
		       			print "         img: figures/" + id + "/" + id + "-" + item.lower().replace(" ", "-") + ".jpg"
		       			print "         label: " + item
		       			print "         caption: " + caption.replace(":", "&colon;")




