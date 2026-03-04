# ConvoEase

**AI-Powered Group Chat Platform with Real-Time Multi-Modal Content Moderation**

ConvoEase is an industry-grade, plugin-based conversational platform built to ensure safe group interactions. It features sophisticated, real-time AI moderation across text, images, and audio seamlessly integrated into a web interface. 

## Key Features

- **Multi-Modal AI Moderation Plugin Engine:** 
  - *Text:* Moderates messages strictly against custom, user-defined group rules.
  - *Image:* Utilizes Vision AI (e.g., Gemma-3) to produce an objective summary of an image before passing the summary through text moderation.
  - *Audio:* Converts speech-to-text via Google Speech Recognition, summarizes transcripts with AI natively, and checks against rules.
- **Dynamic Granular Access System:** Role-based access enabling group admins to dictate moderation rules, access analytical moderation reports, and review flagged messages.
- **Data Persistence & Theming:** Persisted multimedia assets, flat-file database structures via pandas schemas, and a fully reactive UI theme switcher (Light/Dark + 5 accents).
- **Scalable Plugin Architecture:** Designed to easily accommodate new modalities natively (e.g., document parsing) without altering the core routing mechanisms, thanks to an abstract Registry/Dispatcher pattern.

## Tech Stack

- **Backend:** Python 3.11+, Flask, Flask-CORS
- **AI/ML Integration:** OpenRouter API (dynamic model toggling), Google Speech Recognition
- **Audio Processing:** `pydub`, `SpeechRecognition`
- **Database:** Flat-File CSV data store with auto-migration scripting (via Pandas)
- **Frontend:** Vanilla HTML/CSS/JavaScript (No Frameworks)
