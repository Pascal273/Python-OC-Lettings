pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
//     environment {
//         DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB_CREDENTIALS')
//     }
    stages {
        stage('build-and-test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python manage.py collectstatic --noinput'
                sh 'flake8'
                sh 'python manage.py test'
            }
        }
//         stage('containerization') {
//             steps {
//                 sh 'docker build -t pascal237/oc_lettings_site_jenkins:latest .'
//                 sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
//                 sh 'docker push pascal237/oc_lettings_site_jenkins:latest'
//             }
//         }
    }
}