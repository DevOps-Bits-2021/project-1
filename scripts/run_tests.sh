docker run --rm --link sonarqube \
-e SONAR_HOST_URL="http://sonarqube:9000" \
-e SONAR_LOGIN="ad5e59e5bd0cb1e090cb8a38c3618165de693946" \
-v "$(pwd)/web-app:/usr/src" \
sonarsource/sonar-scanner-cli -Dsonar.projectKey=project-demo