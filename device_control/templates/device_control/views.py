from django.shortcuts import render, get_object_or_404, redirect 
from .models import Device 
from .forms import DeviceForm

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_control/device_list.html', {'devices': devices})

def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'device_control/device_form.html', {'form': form})

def device_update(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        form= DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'device_control/device_form.html', {'form':form})

def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        device.delete()
        return redirect('device_list')
    return render(request, 'device_control/device_confirm_delete.html', {'device': device})

