pipeline {
    agent {
        docker {
            image 'python:3.7-stretch'
            args '-e HOME=/var/jenkins_home'
        }
    }

    stages {
        stage("Setup") {
            steps {
                sh 'PATH=~/bin:$PATH python -m pip install --user -e ".[test,packaging]"'
            }
        }
        stage('Test') {
            steps {
                sh 'PATH=~/bin:$PATH python -m pytest .'
            }
        }
    }
}
