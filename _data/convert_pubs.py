import re
def main():
	count = 0
	with open("/Users/roeeaharoni/git/biu-nlp-site/_data/publications_old.html", "r", encoding="utf-8") as f:
	    line = f.readline()
	    year = 0
	    authors = ""
	    title = ""
	    while line:
	        try:
	            if "h3" in line:
	                year = line.replace("<h3>","").replace("</h3>","")
	            if "<li>" in line:
	                authors = line.split(".")[0].replace("<li>","").strip()
	                title = line.split(".")[1].strip().replace("<li> ","").replace("</li> ","")
	                venue = line.split(".")[2].replace("<li> ","").replace("In proceedings of ","").replace("</li>","").replace("in Proceedings of the ","").replace("in Proceedings of The ","")
	                # url = 
	                print("-")
	                print("\tyear: ", year.strip())
	                print("\ttitle: \"{}\"".format(title.strip()))
	                print("\tauthors: \"{}\"".format(authors.strip()))
	                print("\tvenue: \"{}\"".format(venue.strip()))
	                match = re.search(r'href=[\'"]?([^\'" >]+)', line)
	                if match:
	                	url = match.group(1).replace("../.././","http://u.cs.biu.ac.il/~nlp/").replace("../..","http://u.cs.biu.ac.il/~nlp/")
	                	print("\turl: \"{}\"".format(url.strip()))
	                count+=1
	        except Exception as e:
	            print("invalid parse: {}\n{}".format(line, e))
	            return
	        line = f.readline()
	print(count)
if __name__ == "__main__":
	main()