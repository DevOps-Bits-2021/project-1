# DevOps Project 1

## Note:
All the features implemented in the project can be run using the exec_project_ci shell script.
Given below are the options that one can use to check out the features.

### The following are the options

1. -d (deploy) -> <br/>
    Options:
    - 'grid' : This option deploys the selenium grid onto localhost:4444. It is essential to run this deployment before running  selenium tests. <br/>
Example: ` ./exec_project_ci.sh -d grid `
    - 'app' : This option deploys the flask web app in the web-app directory using the docker image. The app can be accessed on localhost:8080 <br/>
Example: ` ./exec_project_ci.sh -d app `
    - 'sonar' : To do sonar scan using local sonarqube sever, We need to deploy sonar qube. Once sonar qube is deployed please create a new project and token for the user. The username and password on initial login are admin/admin. Once the new values are obtained please update in sonar-project.properties and in scripts/sonar_scan.sh <br/>
Example: `./exec_project_ci.sh -d sonar`
2. -rt (run tests) -> <br>
   Options:
   - 'sel' : Once the grid and app are deployed execute selenium tests on the UI <br>
Example: `./exec_project_ci.sh -rt sel`
   - 'sonar' Sonar scan on the project. Please note update the sonar token and project key value after fresh deployment <br>
Example: `./exec_project_ci.sh -rt sonar`
