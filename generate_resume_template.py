#!/usr/bin/env python

from docxtpl import DocxTemplate
import yaml

doc = DocxTemplate("de_cv_template.docx")
stream = file('resume.yml', 'r')
context = yaml.load(stream)
print yaml.dump(context)
doc.render(context)
doc.save("generated_doc.docx")
