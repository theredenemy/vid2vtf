import srctools.vtf as vtf
import av
import pathlib
import os
import shutil
import time
import sys
from PIL import Image
def video_to_vtf(video, fps=3, width=256, height=128):
    ext = pathlib.Path(video).suffix
    name = pathlib.Path(video).stem
    maindir = os.getcwd()
    size = [width, height]
    fileeditname = f"{name}_256128{ext}"
    if os.path.isfile(fileeditname):
        os.remove(fileeditname)
    #os.system(f"ffmpeg -i {video} -r {fps}/1 -vf scale={width}:{height} -async 1 {fileeditname} -y")
    #os.system(f'ffmpeg -i {video} -ar 11025 {name}.wav -y')
    container = av.open(video)
    audio_container = av.open(video)
    audio_stream = audio_container.streams.audio[0]
    output_wav = av.open(f"{maindir}\\sound\\{name}.wav", mode='w')
    output_audio_stream = output_wav.add_stream('pcm_s16le', rate=11025)
    if os.path.isdir(f"{maindir}\\materials"):
        shutil.rmtree(f"{maindir}\\materials")
    os.mkdir(f"{maindir}\\materials")
    if os.path.isdir(f"{maindir}\\sound"):
        shutil.rmtree(f"{maindir}\\sound")
    os.mkdir(f"{maindir}\\sound")
    if os.path.isfile(f"{maindir}\\materials\\{name}.vtf"):
        os.remove(f"{maindir}\\materials\\{name}.vtf")
    if os.path.isfile(f"{maindir}\\sound\\{name}.wav"):
        os.remove(f"{maindir}\\sound\\{name}.wav")
    for frame in audio_container.decode(audio_stream):

        for packet in output_audio_stream.encode(frame):
            output_wav.mux(packet)
    
    for packet in output_audio_stream.encode(None):
        output_wav.mux(packet)
    
    audio_container.close()
    print("wait")
    time.sleep(3)
    stream = container.streams.video[0]
    original_fps = float(stream.average_rate)

    interval = max(1, round(original_fps / fps))
    frames = []
    
    for i, frame in enumerate(container.decode(stream)):
        if i % interval == 0:
            img = frame.to_image().resize(size).convert("RGB")
            frames.append(img.tobytes())
    print(len(frames))
    texture = vtf.VTF(width=width, height=height, frames=len(frames), fmt=vtf.ImageFormats.DXT1, version=(7, 2))

    for i, data in enumerate(frames):
        print(i, end='\r')
        vtf_frame = texture.get(frame=i)
        vtf_frame.copy_from(data, format=vtf.ImageFormats.RGB888)
    print("\n")
    texture.compute_mipmaps()

    with open(f"{maindir}\\materials\\{name}.vtf", 'wb') as f:
        texture.save(f)
    
    return True
           


        
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--video")
    parser.add_argument("--fps")

    args = parser.parse_args()
    
    video_to_vtf(args.video, fps=int(args.fps))       

    
