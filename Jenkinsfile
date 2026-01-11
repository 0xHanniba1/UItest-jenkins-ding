pipeline {
    agent any

    environment {
        HEADLESS = 'true'
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

        stage('Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        success {
            script {
                if (env.DINGTALK_WEBHOOK) {
                    sh 'python3 utils/dingtalk.py success'
                } else {
                    echo 'DINGTALK_WEBHOOK not configured, skipping notification'
                }
            }
        }
        failure {
            script {
                if (env.DINGTALK_WEBHOOK) {
                    sh 'python3 utils/dingtalk.py failure'
                } else {
                    echo 'DINGTALK_WEBHOOK not configured, skipping notification'
                }
            }
        }
        cleanup {
            cleanWs()
        }
    }
}
