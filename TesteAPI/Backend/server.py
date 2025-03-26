# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from fuzzywuzzy import fuzz

app = Flask(__name__)
CORS(app) # Adicionado apenas para testes em ambiente local

# Load the CSV data
df = pd.read_csv('Relatorio_cadop.csv', sep=';', encoding='utf-8')

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    # Simple search implementation (can be enhanced)
    results = []
    for _, row in df.iterrows():
        # Search in multiple fields
        search_fields = [
            str(row['Razao_Social']),
            str(row['Nome_Fantasia']),
            str(row['Cidade']),
            str(row['UF'])
        ]
        
        # Calculate match score
        max_score = max(fuzz.partial_ratio(query.lower(), field.lower()) for field in search_fields if pd.notna(field))
        
        if max_score > 50:  # Threshold for relevance
            results.append({
                'score': max_score,
                'data': row.to_dict()
            })
    
    # Sort by relevance
    results.sort(key=lambda x: x['score'], reverse=True)
    
    # Return only the data (without scores)
    results_df = pd.DataFrame([r['data'] for r in results[:20]])
    return results_df.to_json(orient='records', date_format='iso', force_ascii=False)

if __name__ == '__main__':
    app.run(debug=True, port=5000)