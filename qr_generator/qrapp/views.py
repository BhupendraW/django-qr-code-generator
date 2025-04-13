import qrcode
from io import BytesIO
import base64
from django.http import HttpResponse
from django.shortcuts import render

def generate_qr(request):
    qr_image_base64 = None
    download_data = None

    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            qr = qrcode.make(url)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            img_data = buffer.getvalue()
            qr_image_base64 = "data:image/png;base64," + base64.b64encode(img_data).decode()
            download_data = base64.b64encode(img_data).decode()

    return render(request, 'qrapp/qr_generator.html', {
        'qr_image': qr_image_base64,
        'download_data': download_data,
    })
