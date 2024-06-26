FROM python:alpine
COPY . /app
RUN pip3 install poetry \
    poetry install
WORKDIR app
ENTRYPOINT \[ "flask" \]
CMD \[ "run", "-app", "app.api.create_app()", "--host", "0.0.0.0" \]
