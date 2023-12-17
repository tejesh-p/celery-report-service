import os
import uuid

from celery import Celery

from app.s3_handler import upload_file_to_s3
from app.task_functions import get_faers_data

celery_app = Celery('tasks', broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

celery_app.conf.timezone = 'Asia/Kolkata'

celery_app.conf.task_track_started = True
celery_app.conf.result_extended = {
    'queue_name': 'results_queue',
}


@celery_app.task(name='celery_handler.tasks.craete_faers_report')
def craete_faers_report():
    # Fetch data from the database
    file_path = get_faers_data()
    _, extension = os.path.splitext(file_path)
    object_name = str(uuid.uuid4()) + extension
    cloud_url = upload_file_to_s3(file_path, object_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    return cloud_url
