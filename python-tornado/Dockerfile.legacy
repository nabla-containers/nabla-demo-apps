FROM python:3.5.2-alpine
RUN apk update && apk add iproute2 git

ENV PYTHONHOME=/usr/local
RUN pip install tornado==4.5.3 six perf

COPY tornado_main.py /usr/local/tornado_main.py

ENTRYPOINT ["python", "/usr/local/tornado_main.py"]
