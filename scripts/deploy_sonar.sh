docker pull sonarqube
docker run -d --name sonarqube -p 9000:9000 sonarqube:latest
echo "The sonar server is active now . Please wait while it loads"
echo "The server will be accessible on localhost:9000 in few moments"