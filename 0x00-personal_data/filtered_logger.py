#!/usr/bin/env python3

""" Data obfuscation """

import re

import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'({})[^{}]*({})'.format('|'.join(fields),
                   separator, separator), r'\1{}{}'.format(redaction, separator), message)

