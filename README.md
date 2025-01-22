# TCC_ESG_Model

## Título do Projeto
Desenvolvimento de Modelo Preditivo de Risco ESG para Investimentos Sustentáveis

## Descrição
Este projeto visa desenvolver um modelo preditivo voltado para a análise de riscos de sustentabilidade e impacto social (ESG) em portfólios de investimento. Utilizando algoritmos de Machine Learning e técnicas de MLOps, a solução prevê o risco ESG de empresas, apoiando investidores na tomada de decisões responsáveis e na mitigação de riscos associados a questões ambientais, sociais e de governança.

O modelo utiliza um índice de risco ESG calculado com base nos três pilares (Ambiental, Social e Governança), permitindo categorizar empresas em diferentes níveis de risco.

## Fonte de Dados
Os dados foram extraídos do conjunto "Environment, Social, And Governance Data" disponível no Kaggle, contendo métricas ESG essenciais de diversas empresas. Essas métricas possibilitam o cálculo de um índice ESG robusto e a criação de um pipeline automatizado.

---

## Metodologia de Implementação

### Desenvolvimento do Modelo
1. **Análise Exploratória de Dados**:
   - Exploração e limpeza dos dados ESG.
   - Cálculo do ESG Risk Score com pesos atribuídos a cada pilar.

2. **Modelagem**:
   - Desenvolvimento de modelos de classificação e regressão para previsão do risco ESG.

3. **Pipeline Automatizado**:
   - Implantado como um serviço de API utilizando Flask e Docker.
   - Controle de versões com MLflow.
   - Pipeline CI/CD com GitHub Actions para automação do deploy.

4. **Monitoramento**:
   - Utilização de Prometheus e Grafana para monitoramento em produção.

5. **Manutenção**:
   - Re-treinamento automático com base em degradações de performance.

---

## Instruções para Execução

### Executar Localmente

#### 1. Clonar o Repositório
```bash
$ git clone https://github.com/Tati-Prado/TCC_ESG_Model.git
$ cd TCC_ESG_Model
```

#### 2. Configurar Ambiente Virtual
```bash
$ python3 -m venv esg_model_env
$ source esg_model_env/bin/activate
$ pip install -r requirements.txt
```

#### 3. Executar a API Localmente
```bash
$ python src/app.py
```
A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

#### 4. Testar a API
Envie uma requisição para o endpoint `/predict`:
```bash
$ curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d @src/entrada.json
```

### Executar com Docker

#### 1. Construir a Imagem Docker
```bash
$ docker build -t esg-risk-api .
```

#### 2. Executar o Container
```bash
$ docker run -p 5000:5000 esg-risk-api
```

#### 3. Testar a API
Envie uma requisição para o endpoint `/predict`:
```bash
$ curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d @src/entrada.json
```

---

## Deploy em Produção

### 1. Configuração de CI/CD com GitHub Actions
O workflow de CI/CD está configurado no diretório `.github/workflows/docker-build.yml`.

#### Descrição do Workflow
- **Build e Push**:
  - Constrói a imagem Docker e faz o push para o Docker Hub.
- **Requisitos**:
  - Variáveis de ambiente `DOCKER_USERNAME` e `DOCKER_PASSWORD` configuradas nos Secrets do repositório.

#### Configurar no GitHub
1. Adicione os secrets `DOCKER_USERNAME` e `DOCKER_PASSWORD` no repositório.
2. Certifique-se de que o branch principal é o `main` e que o workflow está ativo.

### 2. Testar Imagem no Docker Hub
Faça o pull da imagem e teste localmente:
```bash
$ docker pull tatiprado/esg-risk-api:latest
$ docker run -p 5000:5000 tatiprado/esg-risk-api:latest
```

---

## Monitoramento (Prometheus e Grafana)

Planejamento para futuras implementações:
1. **Prometheus**:
   - Configurar o Flask para exportar métricas.
   - Adicionar o Prometheus Metrics Exporter no `app.py`.

2. **Grafana**:
   - Criar dashboards para monitoramento em tempo real.
   - Configurar alertas para desvios de performance.

---

## Autor
Tatiana Prado Santos

## Contribuições
Contribuições são bem-vindas! Siga as diretrizes no arquivo `CONTRIBUTING.md` para mais informações.


