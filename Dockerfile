FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install pipenv 
RUN pipenv install --system --deploy --ignore-pipfile
RUN useradd -U -u 1000 appuser && \
    chown -R 1000:1000 /app
USER 1000
CMD ["python", "main.py"]
