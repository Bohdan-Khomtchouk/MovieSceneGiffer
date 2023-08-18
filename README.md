# MovieSceneGiffer

A simple <50 LOC Python script that automates the creation of GIFs from movies. This script allows users to specify a start time and duration for both the movie and its subtitles, then generates a GIF from that portion of the movie with the relevant subtitles burned in. For context: https://twitter.com/bohdanome/status/1692357945428734046?s=20

## Prerequisites

- Python 3.x
- FFmpeg

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Bohdan-Khomtchouk/MovieSceneGiffer.git
   ```

2. Change into the cloned directory:
   ```bash
   cd MovieSceneGiffer
   ```

## Usage

The script takes in several command-line arguments:

- `movie_name`: The name (and path, if not in the same directory as the script) of the movie file
- `subtitle_name`: The name (and path, if not in the same directory as the script) of the subtitle file
- `movie_start_time`: The start time in the movie for creating the GIF (format: `HH:MM:SS`)
- `movie_duration`: The duration of the GIF in seconds
- `subtitle_start_time`: The start time in the subtitle (format: `HH:MM:SS`)
- `subtitle_duration`: The duration of the subtitle to use in seconds
- `gif_name`: The desired name for the output GIF file (without extension)

Run the script with the following command:

```bash
python gif_maker.py <movie_name> <subtitle_name> <movie_start_time> <movie_duration> <subtitle_start_time> <subtitle_duration> <gif_name>
```

Example:

```bash
python gif_maker.py movie.mp4 subtitle.srt 00:56:41 4 00:56:42 5 output_gif
```

This will generate `output_gif.gif` in the current directory.

## Features

- Allows user to specify different start times and durations for the movie and the subtitle
- Automatically handles subtitle extraction and GIF palette creation for a higher quality gif generation
- Uses FFmpeg for powerful and efficient media processing

## Notes

- The script overwrites `tempsub.srt` and `palette.png` in its working directory each time it runs.
- Ensure that FFmpeg is installed and in your system's PATH.
