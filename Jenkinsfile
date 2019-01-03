pipeline {
    agent {
        docker { image 'python:3.7-stretch' }
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 -V'
            }
        }
    }
}
