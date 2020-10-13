import scraper as ps
import sys

title = "Getting Started with Kubernetes"
#path = "https://app.pluralsight.com/paths/skill/using-kubernetes-as-a-developer"
path = sys.argv[1]
course = ps.Plural_Scrapper(path)
course.delay = 5 
course.launchBrowser()
course.getURLS()


