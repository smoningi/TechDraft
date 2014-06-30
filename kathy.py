import urllib2
from BeautifulSoup import BeautifulSoup
import json

page = urllib2.urlopen('http://www.linkedin.com/in/kdhir').read()
soup = BeautifulSoup(page)
soup.prettify()

education = []
for edu in soup.findAll("div", {"id":"profile-education"}):
    edu_obj = {}
    for univ in edu.findAll("a"):
        # print univ.contents[0]
        edu_obj["University"] = univ.contents[0].strip()
    # Degree and Major
    for deg in edu.findAll("span"):
        # print deg.contents[0]
        edu_obj["degree"] = deg.contents[0].strip()
    # print edu.find("span", class_="major").contents
    for grad_date in edu.findAll("abbr"):
        # print grad_date.contents[0]
        edu_obj["graduation"] = grad_date.contents[0].strip()
    education.append(edu_obj)

url = 'http://www.linkedin.com/in/kdhir'
dict={}
for job in soup.findAll("div", class_="position   experience vevent vcard summary-current"):
    try:
        dict["location"] = job.find("span", class_="location").contents[0]
    except:
        dict["descr"] = job.find("p", class_=" description current-position").contents[0]
    else:
        dict["title"] = job.find("span", class_="title").contents[0]
    print dict


o = open("outfile.json", "wb")
o.write(json.dumps(education))