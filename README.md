# YouTube Video Downloader

A simple Python-based YouTube video downloader with a graphical user interface (GUI) built using Tkinter.  This project allows users to download YouTube videos by pasting the video link into the application.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Project Overview

This project provides a user-friendly way to download YouTube videos.  The application features a simple GUI that minimizes the technical hurdles for users.  It solves the problem of needing to navigate complex websites or use command-line tools to download videos.  The primary use case is for individuals who want to easily download videos for offline viewing.


## Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Project Architecture](#project-architecture)
* [License](#license)


## Prerequisites

* Python 3.x
* `pytube` library

```bash
pip install pytube
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/harshkasat/Youtube-video-download.git
```

2. Navigate to the project directory:

```bash
cd Youtube-video-download
```

3. Install the required library (if not already installed):

```bash
pip install pytube
```


## Usage

1. Run the `youtube-downloader.py` script:

```bash
python youtube-downloader.py
```

2. A GUI window will appear. Paste the YouTube video link into the provided entry field.

3. Click the "Download" button.  The video will be downloaded to the same directory as the script.  A "Downloaded" label will appear to confirm completion.

## Project Architecture

The project consists of a single Python file (`youtube-downloader.py`) that uses the `Tkinter` library for the GUI and the `pytube` library for downloading videos.  The application's logic is straightforward: it takes a YouTube link as input, uses `pytube` to fetch the video stream, and then downloads the highest-quality available stream.


```python
from tkinter import Tk, Label, Entry, Button, StringVar
from pytube import YouTube

# Create the main window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube Downloader')

# ... (GUI elements as shown in the provided code) ...

def download():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.first() #Downloads the highest quality by default.  Could be improved to allow user selection.
        video.download()
        Label(root, text="Downloaded", font="arial 15").place(x=100, y=120)
    except Exception as e:
        Label(root, text=f"Error: {e}", font="arial 15", fg="red").place(x=100, y=120)

# ... (rest of the GUI code) ...
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
