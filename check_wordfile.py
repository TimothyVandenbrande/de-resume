#!/usr/bin/env python3

from docx import Document
import textract

text = textract.process('output/default-resume.docx', extension='docx')

faulty = False
for line in str(text).split('\n'):
    if "{{" in line or "}}" in line:
        faulty = True
        print(line)

if faulty:
    print("Not all template variables have been resolved")
    raise ValueError

filepath = 'output/default-resume.md'
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        if "{{" in line or "}}" in line:
            faulty = True
            print(line)

if faulty:
    print("Not all template variables have been resolved")
    raise ValueError
