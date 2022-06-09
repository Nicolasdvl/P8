from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)


@shared_task
def update_db_task():
    logger.info("Updating db...")
    call_command("delete_data")
    call_command("insert_data")
    logger.info("Update done")
