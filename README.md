# Appian-AI — Python scaffold

This repository contains a minimal Python scaffold demonstrating a simple AI-related service for the Appian AI Process Platform demo.

Repository: https://github.com/24f3003018/Appian-AI

## What this is

A very small Flask application exposing a single endpoint `/classify` that accepts JSON input and returns a simple keyword-based classification label (finance / hr / operations / general). This is intended as a lightweight example you can extend and integrate with Appian process models.

## Files added

- `main.py` — Flask app with `/classify` endpoint
- `requirements.txt` — runtime dependencies
- `.gitignore` — common Python ignores
- `example_input.json` — sample payload
- `README.md` — this file

## Run locally

1. Create a virtual environment and install deps:

```bash
python -m venv venv
source venv/bin/activate  # mac/linux
venv\\Scripts\\activate     # windows
pip install -r requirements.txt
```

2. Run the app:

```bash
python main.py
```

3. Test with curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"task":"Process invoice for payment of amount $1500"}' http://localhost:5000/classify
```

## Example response

```json
{"input":"Process invoice for payment of amount $1500","label":"finance"}
```

## Next steps

- Replace the keyword classifier with an ML model or call an external AI service
- Package as a container for deployment
- Integrate with Appian by wrapping calls in a connected system or integration
