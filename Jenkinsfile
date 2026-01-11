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

        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export HEADLESS=true
                    python -m pytest tests/ -v --alluredir=reports/allure-results
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
                    sh '''
                        . venv/bin/activate
                        python utils/dingtalk.py success
                    '''
                } else {
                    echo 'DINGTALK_WEBHOOK not configured, skipping notification'
                }
            }
        }
        failure {
            script {
                if (env.DINGTALK_WEBHOOK) {
                    sh '''
                        . venv/bin/activate
                        python utils/dingtalk.py failure
                    '''
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
