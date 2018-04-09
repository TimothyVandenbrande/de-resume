FROM python:3 as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM python:3
COPY --from=builder /install /usr
RUN mkdir -p /app/resume
COPY generate_resume_template.py /app
COPY de_cv_template.docx /app
WORKDIR /app
VOLUME /app/resume
CMD ["python", "./generate_resume_template.py"]
