FROM python:3.12.7
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn aiohttp
EXPOSE 3500
CMD ["uvicorn", "socialapi:app", "--host", "0.0.0.0", "--port", "3500"]
