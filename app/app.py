from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Trainee Application</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f6f8;
                text-align: center;
                padding-top: 100px;
            }
            .box {
                background: white;
                padding: 40px;
                margin: auto;
                width: 500px;
                border-radius: 10px;
                box-shadow: 0 2px 10px #ccc;
            }
            h1 {
                color: #2c3e50;
            }
            .success {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>DevOps Trainee Application</h1>
            <p class="success">Application is running successfully!</p>
            <p>Reverse Proxy: Nginx</p>
            <p>Backend: Python Flask</p>
            <p>Database: PostgreSQL</p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/db-health")
def db_health():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("DB_NAME", "appdb"),
            user=os.getenv("DB_USER", "appuser"),
            password=os.getenv("DB_PASSWORD", "apppassword")
        )

        connection.close()

        return jsonify({
            "database": "connected"
        })

    except Exception as e:
        return jsonify({
            "database": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
