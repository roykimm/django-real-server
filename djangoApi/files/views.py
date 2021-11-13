from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
import os
# Create your views here.

# DJANGO project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@api_view(['GET'])
def download_file(request, file_name):
    print("download " + file_name)

    file_path = BASE_DIR + "/media/files/" + file_name

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/force_download")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    # If file is not exists
    raise Http404


@api_view(['GET'])
def download_image(request, file_name):

    print("download " + file_name)
    print("download_image")
    file_path = BASE_DIR + "/media/uploads/images/" + file_name

    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/force_download")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(file_path)
            return response
    # If file is not exists
    raise Http404


# @api_view(['GET'])
# def download_file(request, file_name):
#     print("download " + file_name)

#     file_path = BASE_DIR + "/media/files/" + file_name

#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(
#                 fh.read(), content_type="application/force_download")
#             response['Content-Disposition'] = 'inline; filename=' + \
#                 os.path.basename(file_path)
#             return response
#     # If file is not exists
#     raise Http404
