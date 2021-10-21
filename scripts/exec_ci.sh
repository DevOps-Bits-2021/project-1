#!/bin/bash
############################################################
# Help                                                     #
############################################################
USAGE()
{
   # Display Help
   echo "These are the available functions"
   echo
   echo "Syntax: scriptTemplate [-d|h|v|V]"
   echo "options:"
   echo "d ->    Option to deploy 'grid' or 'app' "
   echo "         'app' : deploys the flask web app                                   "
   echo "         'grid' : deploys the selenium grid                                  "
   echo "         'sonar' : deploys the sonarqube sever                               "
   echo "          Once the server is up please obtain create a new project, and "
   echo "          generate a new token for the project                          "   
   echo "          Example: '-d app -d grid -d sonar'                           "     
   echo "rt ->   Option to run tests 'sel' or 'sonar' Example: '-rt sel -ret sonar"
   echo "h  ->   Print this Help."
   echo
}


deploy_grid () {
    chmod +x scripts/deploy_grid.sh
    ./scripts/deploy_grid.sh
}
deploy_app () {
    chmod +x scripts/deploy_app.sh
    ./scripts/deploy_app.sh
}
deploy_sonar () {
    chmod +x scripts/deploy_sonar.sh
    ./scripts/deploy_sonar.sh
}
run_selenium_tests () {
    chmod +x ./scripts/run_tests.sh
    ./scripts/run_tests.sh
}
run_sonar_scan () {
    chmod +x ./scripts/sonar_scan.sh
    ./scripts/sonar_scan.sh
}
exec_deploy_option ( ) {
     case $1 in
      grid) # display Help
        deploy_grid;;
      app) # Enter a name
        deploy_app;;
      sonar)
        deploy_sonar;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
     esac
}
exec_tests_option () {
    case $1 in
      sel)
        run_selenium_tests;;
      sonar)
        run_sonar_scan;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
     esac
}
while getopts ":d:h:rt" option; do
   case $option in
      h) # display Help
         USAGE
         exit;;
      d) # Enter a name
         OPTION=$OPTARG
         exec_deploy_option $OPTION;;
      rt) OPTION=$OPTARG
         exec_tests_option $OPTION;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done
