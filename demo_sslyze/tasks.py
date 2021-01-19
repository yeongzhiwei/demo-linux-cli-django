import subprocess

from celery import shared_task


@shared_task
def run_sslyze(hostname, ip_addr):
    completed_process = subprocess.run(["sslyze", "--regular", f"{hostname}:443{{{ip_addr}}}"], check=True, capture_output=True)
    return completed_process.stdout.decode("utf-8")