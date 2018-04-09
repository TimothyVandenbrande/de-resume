#!/usr/bin/env python

from docxtpl import DocxTemplate
import yaml
import json
import os

def generate_it(i, o, f, t):
    if ".yml" in f or ".yaml" in f:
        context = yaml.load(file(i + "/" + f, 'r'))
    elif ".json" in f:
        context = json.loads(file(i + "/" + f, 'r').read())
    doc.render(context)
    doc.save(o + "/" + f + ".docx")

doc = DocxTemplate("de_cv_template.docx")

resumedir = os.getcwd() + '/resume'
outputdir = os.getcwd() + '/generated'
for r, d, f in os.walk(resumedir):
    for filename in f:
        truefile = os.path.join(r, filename)
        print truefile
        if ".yml" in filename or ".yaml" in filename or ".json" in filename:
            generate_it(resumedir, outputdir, filename, doc)

