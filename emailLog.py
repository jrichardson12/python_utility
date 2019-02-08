#!/opt/local/bin/python3
# authon: John Richardson
#   desc: Send an email.

import os


def email(subject, body, emailAddress):
	if '@' in emailAddress:
		string = 'echo ' + body + ' | mutt -s "' + subject + '" ' + emailAddress
		os.system(string)
	else:
		print('email is not valid')
