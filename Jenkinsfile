pipeline {
    agent any

    environment {
        HEADLESS = 'true'
        DINGTALK_WEBHOOK = credentials('dingtalk-webhook')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    export HEADLESS=true
                    python3 -m pytest tests/ -v --alluredir=reports/allure-results
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'reports/allure-results']]
        }
        success {
            sh 'python3 utils/dingtalk.py success'
        }
        failure {
            sh 'python3 utils/dingtalk.py failure'
        }
        cleanup {
            cleanWs()
        }
    }
}
