FROM python:3.12.7
WORKDIR /app
COPY . /app
RUN pip install aiohttp
EXPOSE 9000
CMD ["python", "authapi.py"]
