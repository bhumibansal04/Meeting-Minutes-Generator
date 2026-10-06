# AI-Powered Meeting Minutes Generator

An AI-powered desktop application that converts recorded meeting audio into structured and meaningful meeting minutes automatically.

The system takes a meeting audio recording as input, transcribes the conversation, processes the transcript using NLP techniques, and generates organized meeting minutes containing important information such as key points, decisions, action items, and entities.

## Features

* 🎤 Audio-based meeting input
* 📝 Automatic speech-to-text transcription
* 🤖 NLP-based text processing
* 📌 Extraction of important meeting information
* 👥 Entity extraction
* ✅ Identification of action items and decisions
* 📄 Automatic generation of meeting minutes in DOCX format
* 🖥️ Simple graphical user interface
* 💻 Runs locally without requiring an external API

## Technologies Used

| Technology  | Purpose                                           |
| ----------- | ------------------------------------------------- |
| Python      | Core programming language                         |
| Whisper     | Speech-to-text transcription                      |
| spaCy       | Natural Language Processing and entity extraction |
| NLTK        | Text processing and sentence tokenization         |
| Tkinter     | Graphical User Interface                          |
| python-docx | Generation of meeting minutes in DOCX format      |

## Project Workflow

```text
Meeting Audio
     |
     v
Audio Upload
     |
     v
Whisper Transcription
     |
     v
Text Processing
     |
     v
NLP / Entity Extraction
     |
     v
Important Information Extraction
     |
     +-------------------+
     |         |         |
     v         v         v
 Decisions  Action     Key
            Items      Points
     |         |         |
     +---------+---------+
               |
               v
     Structured Meeting Minutes
               |
               v
          DOCX Output
```

## Project Structure

```text
Meeting-Minutes-Generator/
|
├── main.py
├── gui.py
├── meeting_ai.py
├── utils.py
|
├── sample.wav
├── meeting_minutes.docx
├── sample_meeting_minutes.docx
|
├── .gitignore
└── README.md
```

## File Description

### `main.py`

Main entry point of the application.

### `gui.py`

Contains the Tkinter-based graphical user interface through which users can interact with the application and provide meeting audio.

### `meeting_ai.py`

Contains the core AI and NLP processing logic used for transcription and meeting information extraction.

### `utils.py`

Contains supporting utility functions used by the application.

### `sample.wav`

Sample meeting audio file used to test the application.

### `meeting_minutes.docx`

Example generated meeting-minutes document.

### `sample_meeting_minutes.docx`

Sample output document demonstrating the generated meeting minutes.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/bhumibansal04/Meeting-Minutes-Generator.git
```

### 2. Open the project directory

```bash
cd Meeting-Minutes-Generator
```

### 3. Install the required Python libraries

```bash
pip install openai-whisper
pip install spacy
pip install nltk
pip install python-docx
```

Install the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

## Running the Application

Run the application using:

```bash
python main.py
```

If the GUI is started directly through `gui.py`, use:

```bash
python gui.py
```

Upload a meeting audio file through the application and allow the system to process the recording.

The application generates structured meeting minutes in DOCX format.

## Output

The generated meeting minutes can contain information such as:

* Meeting summary
* Key discussion points
* Decisions
* Action items
* Important entities
* Other relevant information extracted from the meeting

The final result is saved as a Word document for easy sharing and documentation.

## Advantages

* Reduces the effort required to manually prepare meeting minutes.
* Converts lengthy meeting recordings into structured information.
* Helps identify important decisions and action items.
* Provides a simple desktop interface.
* Generates reusable DOCX documentation.
* Can work locally without depending on an external AI API.

## Future Enhancements

* Speaker identification and diarization
* Improved meeting summarization using transformer-based models
* Support for multiple languages
* Automatic deadline and task extraction
* Searchable meeting history
* Improved action-item classification
* Cloud-based deployment
* User authentication and meeting management

## Use Cases

The system can be useful for:

* College project meetings
* Team meetings
* Software development meetings
* Academic discussions
* Business meetings
* Interviews and discussions
* Project review meetings

## Project Information

**Project:** AI-Powered Meeting Minutes Generator

**Technology:** Python, Whisper, NLP, Tkinter

**Project Type:** AI / NLP / Desktop Application

**Developer:** Bhumi Bansal

## License

This project is created for educational and academic purposes.
