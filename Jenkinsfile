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
        stage('run python') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'api/app.py'
                    } else {
                        sh 'api/app.py'
                    }
                }
            }
        }
        stage('run python') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python 1.py'
                    } else {
                        sh 'python 1.py'
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
