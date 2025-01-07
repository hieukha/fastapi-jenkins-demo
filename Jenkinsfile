pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hieukha/fastapi-jenkins-demo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
            githubChecksPublish name: 'FastAPI App', detailsURL: 'https://github.com/hieukha/fastapi-jenkins-demo.git'
        }
    }
}
