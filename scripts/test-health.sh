#!/bin/bash

echo "Validando endpoint /health da aplicação SPACE CONNECT..."

URL=${1:-http://host.docker.internal:5001/health}

echo "URL testada: $URL"

response=$(curl -s "$URL")

echo "Resposta recebida:"
echo "$response"

echo "$response" | grep "OK"

if [ $? -eq 0 ]; then
  echo "Teste de health check executado com sucesso."
  exit 0
else
  echo "Falha no teste de health check."
  exit 1
fi