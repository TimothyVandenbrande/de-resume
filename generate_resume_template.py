#!/usr/bin/env python

from docxtpl import DocxTemplate
import yaml
import json
import os

def generate_it(resumedir, filename, template):
    if filename.lower().endswith(('.yml', '.yaml')):
        context = yaml.load(open(resumedir + "/" + filename, 'r'))
    elif filename.lower().endswith('.json'):
        context = json.loads(open(resumedir + "/" + filename, 'r').read())
    template.render(context)
    template.save(resumedir + "/" + filename + ".docx")

doc = DocxTemplate("de_cv_template.docx")

resumedir = os.getcwd() + '/resume'
for r, d, filenames in os.walk(resumedir):
    for filename in filenames:
        truefile = os.path.join(r, filename)
        if filename.lower().endswith(('.yml', '.yaml', '.json')):
            generate_it(resumedir, filename, doc)
