import subprocess

from django.shortcuts import render
from django.views import View

from .forms import HostForm

class DemoSslyze(View):
    def get(self, request):
        form = HostForm()
        return render(request, 'demo_sslyze/sslyze.html', {'form': form})

    def post(self, request):
        form = HostForm(request.POST)

        if form.is_valid():
            hostname = form.cleaned_data['hostname']
            ip_addr = form.cleaned_data['ip_addr']
            try:
                completed_process = subprocess.run(["sslyze", "--regular", f"{hostname}:443{{{ip_addr}}}"], check=True, capture_output=True)
                return render(request, 'demo_sslyze/sslyze.html', {'form': form, 'status': 'Success', 'output': completed_process.stdout.decode("utf-8")})
            except CalledProcessError as ex:
                return render(request, 'demo_sslyze/sslyze.html', {'form': form, 'status': 'Failed', 'output': ex})

        return render(request, 'demo_sslyze/sslyze.html', {'form': form})