#!/usr/bin/env python

import time, sys, csv, xml, re, subprocess
import xml.etree.ElementTree as ET

######################################
# Review Remover 
######################################

# file definitions
scf_input_file = 'bv_avon.xml'
review_id_file = 'Review.csv'
output_file = 'meet_mark_import.xml'

#namespace declaration
namespace = 'http://www.bazaarvoice.com/PRR/SyndicationFeed/1.3'
namespaces = {'', namespace}
ET.register_namespace('', namespace)

# parse the standard client or syndication feed
tree = ET.parse(scf_input_file)
root = tree.getroot()

# get the list of review ids you want to keep from the above input file
review_ids = [line.strip() for line in open(review_id_file)]

# go through each product review and remove the review if it is *not* in the list of review_ids
for product in root.findall('{' + namespace + '}Product'):
	for reviews in product.findall('{' + namespace + '}Reviews'):
		for review in reviews.findall('{' + namespace + '}Review'):
			if review.get('id') not in review_ids:
				reviews.remove(review)

tree.write(output_file, encoding="utf-8", xml_declaration=True, default_namespace='')