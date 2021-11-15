from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
import os
import subprocess
import pytube
import json
import string
import random
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


def make_randomKey():
    _LENGTH = 20
    string_pool = string.ascii_lowercase  # 소문자
    result = ""
    for i in range(_LENGTH):
        result += random.choice(string_pool)  # 랜덤한 문자열 하나선택
    return result


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


@api_view(['POST'])
def download_tube(request):

    url = request.data['url']
    if not url:
        response = HttpResponse("url을 입력하여 주세요.")
        return response

    yt = pytube.YouTube(url)

    vids = yt.streams.all()
    parent_dir = BASE_DIR + "/media/tube/"  # 다운받을 경로

    vnum = 1
    vids[vnum].download(parent_dir)  # 다운로드 하기
    default_filename = vids[vnum].default_filename
    new_filename = make_randomKey() + ".mp3"
    subprocess.call(['ffmpeg', '-i', os.path.join(parent_dir,
                                                  default_filename), os.path.join(parent_dir, new_filename)])
    print('동영상 다운로드 && mp3변환완료!')

    file_path = parent_dir + new_filename

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
