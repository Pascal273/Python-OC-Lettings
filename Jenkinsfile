pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('Pull Image') {
            steps {
                sh 'docker pull python:3.10.7-alpine'
            }
    }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}