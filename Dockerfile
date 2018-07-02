FROM python:3 as builder

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir -p /app/resume
COPY generate_resume_template.py /app
COPY de_cv_template.docx /app

WORKDIR /app
VOLUME /app/resume

CMD ["python", "./generate_resume_template.py"]

