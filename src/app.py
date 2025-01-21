from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminhos dos modelos
model_paths = {
    "Forest area (% of land area)": os.path.join(BASE_DIR, "../modelos_deploy_src/modelo_Forest_area_%_of_land_area_Random_Forest.joblib"),
    "Literacy rate, adult total (% of people ages 15 and above)": os.path.join(BASE_DIR, "../modelos_deploy_src/modelo_Literacy_rate_adult_total_%_of_people_ages_15_and_above_Random_Forest.joblib")
}

# Carregar modelos
models = {name: joblib.load(path) for name, path in model_paths.items()}

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


