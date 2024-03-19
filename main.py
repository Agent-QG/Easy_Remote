from flask import Flask, render_template
import keyboard
import time

app = Flask(__name__)

def press_sequence(sequence):
    for key in sequence:
        keyboard.press(key)
        time.sleep(0.2)
        keyboard.release(key)
        time.sleep(0.35)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/press-keys/<int:button_id>')
def press_keys(button_id):
    sequences = {
        1: ['up', 'down', 'left', 'right', 'up'],
        2: ['up', 'right', 'down', 'right'],
        3: ['down', 'left', 'down', 'up', 'right'],
        4: ['down', 'left', 'down', 'up', 'down']
    }
    if button_id in sequences:
        press_sequence(sequences[button_id])
        return {'status': 'success'}
    return {'status': 'error'}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
