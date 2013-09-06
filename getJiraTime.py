import requests, json, string

outfile = open('out.tmp', 'w')

headers = {
	'content-type': 'application/json',
	'content-encoding' : 'utf-8'
}

SSIEs = [
	"afrankiv",
	"anabok",
	"asenyk",
	"aturkevych",
	"gkochiashvili",
	"ileskiv",
	"iromanenko",
	"miskiv",
	"mmartyniuk",
	"mskrypets",
	"okomar",
	"oleontieva",
	"ovoziv",
	"pkuklin",
	"rgrytsyuk",
	"rmaleryk",
	"sbagriantsev",
	"sliuskov",
	"vpatsay",
	"vtsarevych"
]

SSQA = [
	"opanchyshyn",
	"ikarpova",
	"vprystash",
	"okolodiy",
	"akozyuta"

]
GAPIEs = [
]
GAPQA = [
	"lrojas"
]

for ie in SSIEs: 
	data = {
		"user": ie,
	#	"group": "TS-SS-Implementation",
		"startDate": "2013-02-01",
		"project": "BVC"
	}

	r = requests.get('https://bits.bazaarvoice.com/jira/rest/jira-worklog-query/1.0.0/findWorklogs', params=data, auth=('bitsbuilder', 'bitsbuilder'), headers=headers)

	timeEntries = r.json()

	for response in timeEntries:
		for entry in response:
			outfile.write(str(entry['startDate']) + '\t' + str(entry['duration']) + '\t' + str(entry['userId']) + '\n')

