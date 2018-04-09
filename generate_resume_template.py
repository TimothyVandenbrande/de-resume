#!/usr/bin/env python

from docxtpl import DocxTemplate
import yaml
import json
import os

def generate_it(i, f, t):
    if f.lower().endswith(('.yml', '.yaml')):
        context = yaml.load(open(i + "/" + f, 'r'))
    elif f.lower().endswith('.json'):
        context = json.loads(open(i + "/" + f, 'r').read())
    doc.render(context)
    doc.save(i + "/" + f + ".docx")

doc = DocxTemplate("de_cv_template.docx")

resumedir = os.getcwd() + '/resume'
for r, d, f in os.walk(resumedir):
    for filename in f:
        truefile = os.path.join(r, filename)
        if filename.lower().endswith(('.yml', '.yaml', '.json')):
            generate_it(resumedir, filename, doc)

