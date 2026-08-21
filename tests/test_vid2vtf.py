import vid2vtf
import shutil
from pathlib import Path
import pytest
import os

video_name = "view.mp4"

def setup_temp_files(test_video, tmp_video):
    shutil.copyfile(test_video, tmp_video)
def test_default(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path)
    
def test_material_modify_control(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path, material_modify_control=True)

def test_use_video_fps(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path, use_video_fps=True)

def test_fps_count(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path, fps=30)

def test_width_and_height(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path, width=64, height=64)
def test_output_filename(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path, output_filename="view2")

def test_all_material_modify_control_true(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path, width=64, height=64, fps=30, output_filename="view32", material_modify_control=True)
def test_all_material_modify_control_false(tmp_path, request):
    print(tmp_path)
    print(os.path.dirname(request.path))
    tests_dir = os.path.dirname(request.path)
    test_video = os.path.join(tests_dir, video_name)
    tmp_video = os.path.join(tmp_path, video_name)
    if not os.path.isfile(tmp_video):
        setup_temp_files(test_video, tmp_video)
    assert vid2vtf.video_to_vtf(tmp_video, output_dir=tmp_path, width=64, height=64, fps=30, output_filename="view32", material_modify_control=False)