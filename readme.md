# HomeWizard P1 Data Viewer

This is a simple Flask application that fetches data from your HomeWizard P1 meter and displays it in a web page.

## Requirements

- Python 3.11
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

```bash
python3 app.py
```

Open <http://localhost:5000> in your browser. The application will query `http://192.168.50.57/api/v1/data` and display the raw response.

