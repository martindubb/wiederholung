FROM python:slim

WORKDIR /usr/src/app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app.py .

RUN mkdir -p /var/log/myproject
RUN useradd -M -s /bin/bash myuser && chown -R myuser /var/log/myproject
USER myuser

CMD [ "flask", "run", "--host", "0.0.0.0" ]