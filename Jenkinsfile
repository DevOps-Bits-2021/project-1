pipeline{
    agent any
    parameters{
        booleanParam(name: 'Build', defaultValue: true, description: '\'true\' triggers image builds')
        booleanParam(name: 'Build', defaultValue: true, description: '\'true\' triggers image builds')


    }
    stages{
        stage("Deploy Grid"){
            when { expression { params.BuildLogin == true } }
            steps{
                sh "exec_project_ci.sh -d grid"
            }
        }
        stages('Run Tests'){
            parallel{
                stage('Selenium Tests for app'){
                    when { expression { params.Build == true } }
                    steps{
                        sh "exec_project_ci.sh -rt sel"
                    }
                }
                stage('Selenium tests for Login'){
                    agent { //here we select only docker build agents
                        docker {
                            image 'maven:latest' //container will start from this image
                        }
                    }
                    steps {
                        script{
                            dir('login_app/login_app_sel_tests/GridSetupTest'){
                                sh 'mvn clean install' //this command will be executed inside maven container
                                archive(includes: '**/TEST-TestSuite.xml')
                                junit '**/junitreports/*.xml'
                            }
                        }
                    }
                }
            }
        }
        stage("Run Sonar Scanner"){
            when { expression { params.RunSonarScan == true } }
            steps{
                sh "exec_project_ci.sh -rt sonar"
            }
        }
        stage('Deploy App'){
            when { expression { params.DeployApp == true } }
            steps{
                sh "exec_project_ci.sh -d app"
            }
        }
    }
    post {
        always {
            step([$class: 'Publisher', reportFilenamePattern: '**/testng-results.xml'])
        }
    }
}