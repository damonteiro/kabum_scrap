from flask import Flask, render_template, jsonify
import pandas as pd
import requests
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder='insights')

@app.route('/')
def get_metrics():
    file_path = './basestratadas/TabelaPrecos.csv'
    df = pd.read_csv(file_path)

    metrics = {
        'mean': df['% Desconto'].mean(),
        'median': df['% Desconto'].median(),
        'std_dev': df['% Desconto'].std()
    }

    return jsonify({
        'data': df.to_dict(orient='records'),
        'metrics': metrics
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
