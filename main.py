from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

api_key = "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"
client = OpenAI(api_key=api_key)

def generate_response(prompt):
    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:socialbullyalert3:97z66Ua9",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    response = generate_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
