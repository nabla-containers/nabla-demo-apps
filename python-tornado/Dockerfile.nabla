FROM python:3.5.2-alpine

ENV PYTHONHOME=/usr/local
RUN pip install tornado==4.5.3 six perf

# First stage installs dependencies

FROM nablact/nabla-python3-base:v0.3

# nabla-python3-base has a PYTHONHOME of /usr/local

COPY --from=0 /usr/local/lib /usr/local/lib
COPY tornado_main.py /usr/local/tornado_main.py
CMD ["/usr/local/tornado_main.py"]
