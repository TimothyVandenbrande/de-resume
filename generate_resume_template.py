#!/usr/bin/env python

from docxtpl import DocxTemplate
import yaml
import json
import os

def generate_cv(resumedir, outputdir, filename, templateLocation):
    template = DocxTemplate(templateLocation)
    if filename.lower().endswith(('.yml', '.yaml')):
        context = yaml.load(open(resumedir + "/" + filename, 'r'), Loader=yaml.SafeLoader)
    elif filename.lower().endswith('.json'):
        context = json.loads(open(resumedir + "/" + filename, 'r').read())
    template.render(context)
    template.save(outputdir + "/" + os.path.splitext(filename)[0] + ".docx")
    context = None


templateLocation = "templates/de_cv_template.docx.j2"
outputdir = os.getcwd() + "/output"
resumedir = os.getcwd() + "/resume"

for r, d, filenames in os.walk(resumedir):
    for filename in filenames:
        if filename.lower().endswith(('.yml', '.yaml', '.json')):
            generate_cv(resumedir, outputdir, filename, templateLocation)
