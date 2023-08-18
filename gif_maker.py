import subprocess
import argparse

def create_gif(movie_name, subtitle_name, movie_start_time, movie_duration, subtitle_start_time, subtitle_duration, gif_name):
    """
    Create an animated GIF from a specific time in a movie, 
    using the specified subtitle file and the given durations and start times.

    Parameters:
    - movie_name: The name of the movie file
    - subtitle_name: The name of the subtitle file
    - movie_start_time: The start time in the movie for creating the GIF
    - movie_duration: The duration for the GIF
    - subtitle_start_time: The start time in the subtitle
    - subtitle_duration: The duration of the subtitle to use
    - gif_name: The name of the generated GIF file
    """
    
    # Extract the relevant portion of the subtitle file
    command1 = [
        'ffmpeg', '-y', '-ss', subtitle_start_time, '-t', str(subtitle_duration),
        '-i', subtitle_name, 'tempsub.srt'
    ]
    subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Generate a color palette for the GIF
    command2 = [
        'ffmpeg', '-y', '-ss', movie_start_time, '-t', str(movie_duration),
        '-i', movie_name, '-r', '15',
        '-filter_complex', "[0:v] fps=10,scale=512:-1,palettegen", 'palette.png'
    ]
    subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Create the GIF using the extracted subtitle and the generated color palette
    command3 = [
        'ffmpeg', '-y', '-ss', movie_start_time, '-t', str(movie_duration),
        '-i', movie_name, '-i', 'palette.png',
        '-filter_complex', "[0:v] fps=10,subtitles=tempsub.srt,scale=720:-1 [new];[new][1:v] paletteuse", f'{gif_name}.gif'
    ]
    subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':
    # Define and parse command line arguments
    parser = argparse.ArgumentParser(description='Create animated GIFs from movies with subtitles.')
    
    parser.add_argument('movie_name', help='The name of the movie file')
    parser.add_argument('subtitle_name', help='The name of the subtitle file')
    parser.add_argument('movie_start_time', help='The start time in the movie for creating the GIF (format: HH:MM:SS)')
    parser.add_argument('movie_duration', type=int, help='The duration (in seconds) for the GIF')
    parser.add_argument('subtitle_start_time', help='The start time in the subtitle (format: HH:MM:SS)')
    parser.add_argument('subtitle_duration', type=int, help='The duration (in seconds) of the subtitle to use')
    parser.add_argument('gif_name', help='The name of the generated GIF file')
    
    args = parser.parse_args()
    
    # Call the function with parsed arguments
    create_gif(args.movie_name, args.subtitle_name, args.movie_start_time, args.movie_duration, args.subtitle_start_time, args.subtitle_duration, args.gif_name)

