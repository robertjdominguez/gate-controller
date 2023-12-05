FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

RUN echo "source activate my_env" > ~/.bashrc

ENV PATH /opt/conda/envs/my_env/bin:$PATH


ENTRYPOINT ["python3"]
CMD ["app.py"]