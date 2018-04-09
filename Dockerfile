FROM python:3 as python-base
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3-alpine
COPY --from=python-base /root/.cache /root/.cache
COPY --from=python-base requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache

WORKDIR /usr/src/app

COPY . .

VOLUME /usr/src/app/resume

CMD [ "python", "./generate_resume_template.py" ]