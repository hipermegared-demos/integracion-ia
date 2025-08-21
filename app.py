from flask import Flask, request;
from flasgger import Swagger
import requests
import json

app = Flask(__name__)
Swagger(app)

@app.route('/gemini', methods = ['POST'])
def ask_gemini():
    """
        Recibe una pregunta y la envia a Gemini.
        ---
        tags:
            - Data API
        parameters:
            - name: body
              in: body
              required: true
              schema: 
                type: object
                properties:
                    prompt:
                        type: string
                        example: que es una IA
        responses:
          200:
            description: Respuesta de la IA.
            schema:
              type: object
        """
    data = request.get_json()
    p = data.get('prompt')
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
    payload = {'contents': [{'parts': [{'text': p}]}]}
    headers = {
        'Content-Type': 'application/json',
        'X-goog-api-key': '{{GEMINI_API_KEY}}' 
    }
    res_ia = requests.post(url, json=payload, headers=headers)

    return res_ia.json(), res_ia.status_code

if __name__ == '__main__':
    app.run(debug=True)