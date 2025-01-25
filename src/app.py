from flask import Flask, request, jsonify, Response
from prometheus_client import CollectorRegistry, Counter, generate_latest

import joblib
import pandas as pd
import os

# Criação do app Flask
app = Flask(__name__)

# Configuração do Prometheus-client
registry = CollectorRegistry()
request_counter = Counter(
    'http_requests_total',
    'Contador de requisições HTTP',
    ['method', 'endpoint'],
    registry=registry
)

print("PrometheusMetrics inicializado!")  # Log para verificar a inicialização

@app.before_request
def count_requests():
    request_counter.labels(method=request.method, endpoint=request.path).inc()

@app.route('/metrics')
def metrics():
    return Response(generate_latest(registry), mimetype='text/plain')

# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminhos dos modelos
model_paths = {
    "Forest area (% of land area)": os.path.join(BASE_DIR, "../modelos_deploy_src/modelo_Forest_area_%_of_land_area_Random_Forest.joblib"),
    "Literacy rate, adult total (% of people ages 15 and above)": os.path.join(BASE_DIR, "../modelos_deploy_src/modelo_Literacy_rate_adult_total_%_of_people_ages_15_and_above_Random_Forest.joblib")
}

# Carregar modelos
models = {}
for name, path in model_paths.items():
    try:
        models[name] = joblib.load(path)
    except Exception as e:
        print(f"Erro ao carregar o modelo {name}: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Dados recebidos no corpo da requisição
        input_data = request.get_json()

        # Converter dados para DataFrame
        input_df = pd.DataFrame(input_data)

        # Inicializar dicionário de resultados
        predictions = {}

        # Fazer previsões para cada modelo
        for variable, model in models.items():
            predictions[variable] = model.predict(input_df).tolist()

        return jsonify(predictions)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/')
def home():
    return "API ESG Risk está funcionando! Acesse /metrics para monitoramento."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)


