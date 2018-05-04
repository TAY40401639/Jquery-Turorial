import urllib2,json,base64
accesstoken = "ZMTEH2TURH4D4QPVXRCP"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution,course)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+ ":").replace('\n',''))
response = urllib2.urlopen(request)
data = json.load(response)
print json.dumps(data,indent=3)
for c in data:
	if c['Code'] == 'SALARY':
		d = c['Details']
		for a in d:
			if a['Code'] == "MED":
				print "Median salary after 6 months is " + str(a['Value'])

for c in data:
	if c['Code'] == 'SALARY':
		d = c['Details']
		for a in d:
			if a['Code'] == "LDMED":
				print "Median salary after 40 months is " + str(a['Value'])


for c in data:
	if c['Code'] == 'NSS':
		d = c['Details']
		for a in d:
			if a['Code'] == "Q1":
				print "The proportion of software engineering students is " + str(a['Value'])

