from flask import Flask, render_template, request, jsonify
from graph.langgraph_flow import run_graph
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def process_query():
    query = request.json.get('query', '')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    try:
        answer = run_graph(query)
        return jsonify({
            'answer': answer,
            'file_path': os.path.join('answers', os.listdir('answers')[-1]) if os.path.exists('answers') and os.listdir('answers') else None
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 