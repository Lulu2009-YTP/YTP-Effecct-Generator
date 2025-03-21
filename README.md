# YTP Effects Generator

A modern Python-based YouTube Poop (YTP) effects generator with GUI interface, inspired by classic 2000s video editing techniques from Sony Vegas, Windows Movie Maker, and Audacity.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Last Updated](https://img.shields.io/badge/last%20updated-2025--03--21-brightgreen)

## 📝 Table of Contents
- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Effects](#effects)
- [Contributing](#contributing)
- [License](#license)

## 🎥 About

YTP Effects Generator is a modern reimagining of classic YouTube Poop editing techniques, providing an easy-to-use GUI interface for creating video effects commonly used in the YouTube Poop genre. This tool combines the accessibility of traditional video editors with the power of Python's video processing capabilities.

## ✨ Features

- **User-friendly GUI Interface**: Built with tkinter for easy effect selection and video processing
- **Multiple Effect Types**: Classic YTP effects including:
  - Sentence Mixing
  - Reverse Effects
  - Speed Changes
  - Color Distortion
  - Stutter Effects
- **Batch Processing**: Process entire videos with multiple effects
- **Modern Video Processing**: Powered by moviepy and ffmpeg
- **Cross-platform Support**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.8 or higher
- ffmpeg (system installation)
- Required Python packages:
  ```
  moviepy==1.0.3
  numpy>=1.21.0
  Pillow>=8.0.0
  tk
  ```

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/Lulu2009-YTP/ytp-effects-generator.git
cd ytp-effects-generator
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Install ffmpeg:
- **Windows**: Download from [ffmpeg website](https://ffmpeg.org/download.html) and add to PATH
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt-get install ffmpeg`

## 🚀 Usage

1. Run the program:
```bash
python youtube_poop_generator.py
```

2. In the GUI:
   - Click "Select Input Video" to choose your source video
   - Click "Select Output Location" to set where to save the result
   - Select desired effects using checkboxes
   - Click "Generate YTP" to process the video

## 🎨 Effects

### Sentence Mixing
Randomly rearranges audio segments while maintaining video synchronization.

### Reverse Effect
Reverses video segments for classic YTP style transitions.

### Speed Changes
Applies random speed variations to video segments.

### Color Distortion
Adds color manipulation effects similar to classic YTP videos.

### Stutter Effect
Creates repetitive stuttering effects on random video segments.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 Notes

- This project is inspired by classic YouTube Poop editing techniques from the 2000s
- The effects are designed to be modular and easily extensible
- All effects are randomized to create unique outputs each time

## 🙏 Acknowledgments

- Inspired by classic YouTube Poop creators
- Built using modern Python video processing libraries
- Thanks to the moviepy and ffmpeg communities

---
Last updated: 2025-03-21 02:31:21 UTC  
Created by: [Lulu2009-YTP](https://github.com/Lulu2009-YTP)