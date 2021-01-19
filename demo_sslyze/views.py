from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .forms import HostForm
from .tasks import run_sslyze

class DemoSslyze(View):
    def get(self, request):
        form = HostForm()
        return render(request, 'demo_sslyze/sslyze.html', {'form': form})

    def post(self, request):
        form = HostForm(request.POST)

        if form.is_valid():
            hostname = form.cleaned_data['hostname']
            ip_addr = form.cleaned_data['ip_addr']
            result = run_sslyze.delay(hostname, ip_addr)
            task_id = result.task_id
            return render(request, 'demo_sslyze/sslyze.html', {'form': form, 'task_id': task_id})

        return render(request, 'demo_sslyze/sslyze.html', {'form': form})

class SslyzeResult(View):
    def get(self, request, task_id):
        if task_id:
            # Celery does not have a function to verify if the id is a valid task id.
            # Any invalid id passed to AsyncResult will return a valid AsyncResult with status set to Pending forever
            # A separate model may be necessary to keep track of the ids and map them to the requesters
            result = AsyncResult(id=task_id)
            if result.status == "SUCCESS":
                return JsonResponse({'task_id': task_id, 'status': 'Success', 'output': result.result})
            if result.status == "FAILURE":
                return JsonResponse({'task_id': task_id, 'status': 'Failure'})
            return JsonResponse({'task_id': task_id, 'status': 'Pending'})
        return JsonResponse({'error': 'Invalid task id'})