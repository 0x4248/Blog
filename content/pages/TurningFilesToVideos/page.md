# Turning files into videos

I recently have seen a lot of videos on YouTube showing seemingly random static like videos. Here is an example of one of them:

**WARNING: This video contains flashing lights and is quite loud.**
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/M2x9PgNKbN4?si=32IZoCt4SGnLc3-R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I was curious about how these videos were made and I found out a way to make them using Python and ffmpeg.

## How to make these videos

To start you will need to install python and ffmpeg. You can install python from [here](https://www.python.org/downloads/) and ffmpeg from [here](https://ffmpeg.org/download.html).

If you are on Linux or macOS you an install ffmpeg and python using your package manager.

### Debian/Ubuntu

```bash
sudo apt install ffmpeg python3
```

### Fedora

```bash
sudo dnf install ffmpeg python3
```

### Arch Linux

```bash
sudo pacman -S ffmpeg python
```

### macOS

**Note:** You will need to have [Homebrew](https://brew.sh) installed to install ffmpeg.

```bash
brew install ffmpeg python3
```

### Windows

You can download the installer for ffmpeg from [here](https://ffmpeg.org/download.html) and python from [here](https://www.python.org/downloads/).


## Creating the video

First we will need to make a python script that creates the frames for the video. The following script will create a video with random static like frames. Create a file called `convert.py` and paste the following code into it:

```python
import os

input_file = "test.dat"
output_folder = "frames"
frame_width = 50
frame_height = 50

os.makedirs(output_folder, exist_ok=True)

with open(input_file, "rb") as f:
    data = f.read()

total_bits = len(data) * 8
total_frames = (total_bits + (frame_width * frame_height - 1)) // (frame_width * frame_height)

for frame_index in range(total_frames):
    with open(f"{output_folder}/frame_{frame_index:04d}.ppm", "w") as f:
        f.write(f"P3\n{frame_width} {frame_height}\n1\n")
        
        for y in range(frame_height):
            for x in range(frame_width):
                bit_index = frame_index * (frame_width * frame_height) + y * frame_width + x
                if bit_index < total_bits:
                    byte_index = bit_index // 8
                    bit_in_byte = bit_index % 8
                    bit_value = (data[byte_index] >> (7 - bit_in_byte)) & 1
                    f.write(f"{bit_value} {bit_value} {bit_value} ")
                else:
                    f.write("0 0 0 ")
            f.write("\n")
```

This script will create a folder called `frames` and will create a frame for each bit in the input file. The input file is `test.dat` and you can change it to any file you want. The frames will be saved as `.ppm` files which are a simple image format that ffmpeg can read.

Now run the script using the following command:

```bash
python3 convert.py
```

### Converting the frames to a video

Now that we have the frames we can convert them to a video using ffmpeg. Run the following command to convert the frames to a video:

```bash
ffmpeg -r 30 -f image2 -i frames/frame_%04d.ppm -vcodec libx264 -pix_fmt yuv420p output.mp4
```

This command will create a video called `output.mp4` with the frames in the `frames` folder. The `-r 30` flag sets the frame rate to 30 frames per second. You can change this value to any value you want.

### Upscaling the video (optional)

You can upscale the video using ffmpeg to make it look better. Run the following command to upscale the video:

```bash
ffmpeg -i output.mp4 -vf "scale=1000:1000:flags=neighbor" -c:a copy output_1000x1000.mp4  
```

This command will upscale the video to 1000x1000 pixels. You can change the values to any value you want.

---
## References
- [ffmpeg documentation](https://ffmpeg.org/documentation.html)
- [Modipaz youtube tutorial](https://www.youtube.com/watch?v=vUKQOypH6Ok)