pipeline {
    agent none

    stages {
        stage('Unit Test') {
            agent {
                docker {
                    image 'python:3.7-stretch'
                    args '-e HOME=/var/jenkins_home'
                }
            }

            steps {
                sh 'PATH=~/bin:$PATH python -m pip install --user -e ".[test,packaging]"'
                sh 'PATH=~/bin:$PATH python -m pytest . --cov=ex4mple --junitxml=junit.xml --cov --cov-report=xml'
            }

            post {
                always {
                   junit keepLongStdio: true,
                       testResults: '*.xml'
                }
            }
        }
    }
}
