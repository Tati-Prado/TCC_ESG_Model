# TCC_ESG_Model
Título do Projeto: Desenvolvimento de Modelo Preditivo de Risco ESG para Investimentos Sustentáveis

Descrição:
No meu TCC do MBA em Machine Learning in Production, desenvolverei um modelo preditivo voltado para a análise de riscos de sustentabilidade e impacto social (ESG) em portfólios de investimento. Utilizando algoritmos de Machine Learning e técnicas de MLOps, criarei uma solução que prevê o risco ESG de empresas, apoiando investidores na tomada de decisões baseadas em práticas responsáveis e na mitigação de riscos associados a questões ambientais, sociais e de governança. A solução incluirá um índice de risco ESG, calculado a partir de uma ponderação dos três pilares (Ambiental, Social e Governança), permitindo categorizar as empresas em diferentes níveis de risco.
Fonte de Dados:
Para construir o modelo, utilizarei o conjunto de dados “Environment, Social, And Governance Data” disponível no Kaggle, que inclui métricas ESG essenciais de diversas empresas. Esses dados permitirão criar um índice de risco ESG com base em práticas corporativas, e o modelo será estruturado para manter um pipeline automatizado e monitorado em produção.
Metodologia de Implementação:
1.	Desenvolvimento do Modelo: Começarei com uma análise exploratória e pré-processamento dos dados, realizando o cálculo de um “ESG Risk Score” com base nas métricas ESG e pesos atribuídos a cada pilar. Utilizando algoritmos de classificação e regressão, desenvolverei um modelo que classifica empresas por nível de risco ESG.
2.	Pipeline Automatizado: O modelo será implantado como um serviço de API utilizando Flask e Docker, permitindo o processamento contínuo de novas previsões. Utilizarei MLflow para controle de versões e criarei um pipeline CI/CD com GitHub Actions para automação do deploy.
3.	Monitoramento em Produção: O desempenho do modelo será monitorado em tempo real com Prometheus e Grafana, que fornecerão alertas e dashboards para acompanhamento das métricas de performance e desvio de dados. Isso permitirá uma análise contínua da estabilidade e precisão do modelo em produção.
4.	Manutenção e Atualização: Implementado com técnicas de MLOps, o modelo realizará re-treinamento automático baseado em degradações de performance e manterá logs de versão, garantindo a longevidade e adaptação do modelo às mudanças nos dados ESG.
Esse projeto demonstrará uma aplicação prática de machine learning em produção, proporcionando uma ferramenta valiosa para investidores que desejam incorporar práticas ESG em suas decisões financeiras de forma eficiente e sustentável.
