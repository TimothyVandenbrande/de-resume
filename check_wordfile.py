#!/usr/bin/env python

from docx import Document

import textract
text = textract.process('resume/default-resume.json.docx', extension='docx')

for line in str(text).split('\n'):
    if "{{" in line or "}}" in line:
        raise "Not all template variables have been resolved"
    #print line

