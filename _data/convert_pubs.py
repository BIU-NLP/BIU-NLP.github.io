def main():
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
		            title = line.split(".")[1].strip().replace("<li> ","")
		            venue = line.split(".")[2].split("  ")[1].replace("<li> ","")
		            print(year)
		            print(title)
		            print(authors)
		    except Exception as e:
		        print("invalid parse: {}\n{}".format(line, e))
		    line = f.readline()
if __name__ == "__main__":
	main()