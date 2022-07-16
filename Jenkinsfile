pipeline {
    agent any
    stages {
        stage('checkout repo') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/MSkalt/devopswebapp.git'
            }
        }
        stage('run backend server') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start/min python api/app.py'
                    } else {
                        sh 'nuhup python api/app.py'
                    }
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
