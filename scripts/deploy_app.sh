docker build -t flask-web-app:latest web-app/
docker run -d -p 8080:8080 flask-web-app:latest