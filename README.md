Make Sure FFMPEG is Installed.

```cmd
  --video VIDEO
  --fps FPS
  --width WIDTH
  --height HEIGHT
  --output_filename OUTPUT_FILENAME
  --output_dir OUTPUT_DIR
  --material_modify_control MATERIAL_MODIFY_CONTROL
```
Here is an Example command
```cmd
vid2vtf --video view.mp4 --fps 15 --width 256 --height 128
```
or
```cmd
vid2vtf-cli --video view.mp4 --fps 15 --width 256 --height 128
```
or
```cmd
python -m vid2vtf --video view.mp4 --fps 15 --width 256 --height 128
```