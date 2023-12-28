## SSPEnc using ffmpeg (simple streaming platform encoder)

This repository contains a Python script that utilizes FFmpeg to encode video files into different resolutions and extract audio into an MP3 file. The tool employs multi-threading to optimize the encoding process for various resolutions concurrently.

### Prerequisites

- Python 3.x
- FFmpeg installed and added to system PATH

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    pip install ffmpeg-python argparse
    ```

### Usage

Run the script:

```bash
python main.py <file_path>
```

Replace `<file_path>` with the path to the video file you want to encode.

### Code Overview

#### Dependencies

- `argparse`: Parsing command-line arguments.
- `time`: Handling time-related operations.
- `ffmpeg-python`: Python FFmpeg bindings.
- `threading`: Managing concurrent execution using threads.

#### Script Logic

1. **Argument Parsing**: The script uses `argparse` to accept a single argument - the path to the file to be encoded.

2. **FFmpeg Functions**:
   - `ffmpeg_func`: Encodes the video file into different resolutions concurrently.
   - `convert_to_mp3`: Extracts audio from the video file into an MP3 format.

3. **File Validation**:
   - Checks if the provided file exists. If not, it displays an error message and exits.
   - Creates an "encoded" directory if it doesn't exist already.

4. **Video Resolution Handling**:
   - Determines the height of the input video file.
   - Defines resolutions to encode the video into (1080p, 720p, 360p, 144p).
   - Initiates encoding threads for resolutions supported by the input video's height.

5. **Execution**:
   - Starts threads for video encoding and audio extraction.
   - Waits for all threads to complete their tasks.

6. **Performance Measurement**:
   - Calculates the execution time of the entire process.

### Example

```bash
python main.py path/to/your/video.mp4
```

This command will concurrently encode the video into different resolutions and extract its audio into an MP3 file, all within the "encoded" directory.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
