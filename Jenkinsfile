pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "aniket3003/devops-demo"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/aniket36565954961/devops-pipeline-demo-01.git'
            }
        }

        stage('Build Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push %DOCKER_IMAGE%'
            }
        }
    }
}
