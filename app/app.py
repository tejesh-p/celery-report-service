from flask import Flask

from app.tasks import craete_faers_report

app = Flask(__name__)


@app.route('/faers/data', methods=['GET'])
def export_data():
    print("Api called")
    # Trigger Celery task
    result = craete_faers_report.apply_async()

    # You can handle the result or return a response to the user
    return f'Task started. Task ID: {result.id}'
