pipeline {
    agent any

    environment {
        IMAGE_NAME = 'space-connect-app'
        IMAGE_TAG = '1.0'
        CONTAINER_NAME = 'space-connect-app'
        TEST_CONTAINER_NAME = 'space-connect-app-test'
        APP_PORT = '5000'
        TEST_PORT = '5001'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Iniciando build da imagem Docker...'
                sh '''
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Executando teste automatizado no endpoint /health...'
                sh '''
                    docker rm -f $TEST_CONTAINER_NAME || true

                    docker run -d --name $TEST_CONTAINER_NAME -p $TEST_PORT:5000 $IMAGE_NAME:$IMAGE_TAG

                    sleep 8

                    curl -f http://host.docker.internal:$TEST_PORT/health

                    docker rm -f $TEST_CONTAINER_NAME
                '''
            }
        }

        stage('Deploy Simulado') {
            steps {
                echo 'Executando deploy simulado da aplicação...'
                sh '''
                    docker rm -f $CONTAINER_NAME || true

                    docker run -d --name $CONTAINER_NAME -p $APP_PORT:5000 $IMAGE_NAME:$IMAGE_TAG

                    sleep 8

                    curl -f http://host.docker.internal:$APP_PORT/
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executada com sucesso.'
        }

        failure {
            echo 'Pipeline falhou. Verifique os logs.'
            sh '''
                docker rm -f $TEST_CONTAINER_NAME || true
            '''
        }
    }
}