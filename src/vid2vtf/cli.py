import argparse
import sys
from vid2vtf.vid2vtf import video_to_vtf
def main():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument("--video")
        parser.add_argument("--fps", default=3)
        parser.add_argument("--width", default=256)
        parser.add_argument("--height", default=128)

        args = parser.parse_args()
    
        video_to_vtf(args.video, fps=int(args.fps), width=int(args.width), height=int(args.height))
    else:
        print("-- Use -h")

if __name__ == '__main__':
    main()   