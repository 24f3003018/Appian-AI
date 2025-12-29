from flask import Flask, request, jsonify

app = Flask(__name__)


def classify_task(text):
    """Simple keyword-based classifier that returns a business domain label."""
    if not text:
        return 'general'
    text = text.lower()
    if any(k in text for k in ['invoice', 'payment', 'billing', 'amount', 'receipt']):
        return 'finance'
    if any(k in text for k in ['employee', 'leave', 'hiring', 'hr', 'payroll', 'benefits']):
        return 'hr'
    if any(k in text for k in ['shipment', 'order', 'inventory', 'delivery', 'logistics', 'warehouse']):
        return 'operations'
    return 'general'


@app.route('/classify', methods=['POST'])
def classify():
    """POST JSON {"task": "text to classify"} -> {"input": ..., "label": ...} """
    data = request.get_json(silent=True) or {}
    text = data.get('task') or data.get('text') or data.get('description')
    if not text:
        return jsonify({'error': 'No input text provided. Send JSON with "task" or "text".'}), 400
    label = classify_task(text)
    return jsonify({'input': text, 'label': label})


@app.route('/', methods=['GET'])
def root():
    return jsonify({'service': 'Appian-AI sample classifier', 'endpoint': '/classify'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
