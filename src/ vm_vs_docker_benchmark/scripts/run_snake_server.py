from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/snake')
def snake_game():
    start = time.time()
    score = random.randint(1, 100)
    time.sleep(random.uniform(0.01, 0.05))  # Simula procesamiento
    return jsonify({
        'status': 'ok',
        'score': score,
        'time_elapsed': round(time.time() - start, 4)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
