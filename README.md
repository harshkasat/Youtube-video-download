# YouTube Video Downloader

A simple Python-based YouTube video downloader using `pytube`.  This program provides a graphical user interface (GUI) for easy downloading of YouTube videos.

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Project Overview

This project aims to create a user-friendly application for downloading YouTube videos.  It leverages the `pytube` library to handle the video downloading process, abstracting away the complexities of interacting with the YouTube API. The application features a simple GUI built using Tkinter.

**Key Features:**

*   Simple and intuitive graphical user interface (GUI) built with Tkinter.
*   Uses the `pytube` library for efficient and reliable video downloading.
*   Allows users to download videos by pasting the YouTube video URL.


## Table of Contents

*   [Prerequisites](#prerequisites)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Code Overview](#code-overview)
*   [License](#license)


## Prerequisites

*   Python 3.x
*   `pytube` library:  This can be installed using `pip install pytube`

## Installation

1.  Clone the repository: `git clone https://github.com/harshkasat/Youtube-video-download.git`
2.  Navigate to the project directory: `cd Youtube-video-download`
3.  Install the required library: `pip install pytube`


## Usage

1.  Run the `youtube-downloader.py` script.  This will open a GUI window.
2.  Paste the YouTube video URL into the provided entry field.
3.  Click the "Download" button.  The video will be downloaded to the same directory as the script.


## Code Overview

The core logic resides in `youtube-downloader.py`.  The GUI is created using Tkinter, and the `pytube` library handles the video download.

**Key functions:**

*   `download()`: This function is called when the "Download" button is pressed. It retrieves the URL from the entry field, uses `pytube` to download the highest resolution video available, and displays a "Downloaded" message.


```python
def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="Downloaded", font="arial 15").place(x=100, y=120)
```

The `url.streams.first()` line downloads the first stream found (usually the highest resolution).  For more control over the download quality, you could modify this line to select a specific stream based on resolution or file type.  Refer to the `pytube` documentation for more details.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
