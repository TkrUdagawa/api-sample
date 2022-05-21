FROM python:3.8
COPY requirements.txt /tmp/
COPY dist/apisample-0.1.0-py3-none-any.whl /tmp/
RUN pip install -r /tmp/requirements.txt
RUN pip install /tmp/apisample-0.1.0-py3-none-any.whl
CMD gunicorn apisample.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
