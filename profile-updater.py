#!/usr/bin/env python

import time, sys, csv, xml, re, subprocess
from xml.etree.ElementTree import *
from xml.dom.minidom import parseString
from optparse import OptionParser

old_data = xml.dom.minidom.parse('/Users/javier.hernandez/wip/py-challenge/old_data_formatted.xml')
new_data = xml.dom.minidom.parse('/Users/javier.hernandez/wip/py-challenge/new_data_formatted.xml')
updated_data = open('/Users/javier.hernandez/wip/py-challenge/output.xml', 'wb')

root = new_data.documentElement

#get user ids from old file

old_products = old_data.getElementsByTagName("Product")

old_user_dict = {}
new_user_dict = {}
uniqueId = 999999

for product in old_products: 

	old_reviews = product.getElementsByTagName("Review")

	for review in old_reviews:
		#get the review profile external id and profile name for each
		userProfileNode = review.getElementsByTagName("UserProfileReference")
		profileExternalId = userProfileNode[0].getAttributeNode('id').nodeValue
		profileDisplayName = userProfileNode[0].getElementsByTagName('DisplayName')[0].firstChild.nodeValue

		old_user_dict[profileDisplayName] = {
			'ExternalId': profileExternalId,
			'DisplayName': profileDisplayName
		}

#get all the nicknames from the new file
new_products = new_data.getElementsByTagName("Product")

for product in new_products: 
	new_reviews = product.getElementsByTagName("Review")

	for review in new_reviews:
		#get the review profile external id and profile name for each
		userProfileNode = review.getElementsByTagName("UserProfileReference")
		profileDisplayName = userProfileNode[0].getElementsByTagName('DisplayName')[0].firstChild.nodeValue

		new_user_dict[profileDisplayName] = {
			'ExternalId': '',
			'DisplayName': profileDisplayName
		}

#update the new ids with old ids if they exist. if not, use a unique id

for key in old_user_dict.keys():
	#if there is a matching nickname in the new dict, update its external id with the old dict external id
	new_user_dict[key]['ExternalId'] = old_user_dict[key]['ExternalId']

#now lets update all nicknames in the new dict which weren't found
for key in new_user_dict.keys():
	if new_user_dict[key]['ExternalId'] == '':
		new_user_dict[key]['ExternalId'] = uniqueId
		uniqueId += 1

for product in new_products: 
	new_reviews = product.getElementsByTagName("Review")

	for review in new_reviews:
		#get the review profile external id and profile name for each
		userProfileNode = review.getElementsByTagName("UserProfileReference")
		profileDisplayName = userProfileNode[0].getElementsByTagName('DisplayName')[0].firstChild.nodeValue

		userProfileNode[0].setAttribute('id', str(new_user_dict[profileDisplayName]['ExternalId']))

print root.toxml('utf-8')
#new_data.writexml(updated_data.write(tostring(root)))
#updated_data.write(root.toxml())
#updated_data.close()
