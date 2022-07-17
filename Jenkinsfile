pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
               
            }
        }
        stage('run rest app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/2 python app.py'
                    } else {
                        sh 'python app.py'
                    }
                }
            }
        }
        stage('run rest API test') {
            steps {
                script {
                    bat 'pytest rest_api_tests\\Rest_test.py'
                }
                
                
            }
        }
        stage('clean environment') {
            steps {
                script {
                    bat 'python clean_environment.py'
                }


            }
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}
