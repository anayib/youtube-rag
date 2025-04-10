# Video Transcript Generator - RAG Application

## Overview

This project is an application that uses LangChain and OpenAI to generate a transcript of a YouTube video. It uses Whisper to transcribe the video and OpenAI to generate the transcript. Additionally, it uses Pinecone to store the transcript and LangChain to retrieve the transcript. Once retrieved, the transcript is used as the context to answer questions about the video that are passed to the OpenAI API LLM.

This is an example for MK students to learn how to use LangChain and OpenAI to build a RAG application. 

## Program flow
1. Create a tranascript from a video
2. Chunk the transcript into smaller chunks
3. Genetare embeddings for the chunks
4. Save the embbedings in a vector database
5. Retrieve from the vector database the most relevant chunks based on the embeddings
6. Answer questions about the video using the most relevant chunks as context using the LLM.

## Features

- Generate a transcript of a YouTube video
- Save the transcript to a file
- Load the transcript from a file

## Technologies Used

- LangChain
- OpenAI
- YouTube Transcript API
- Python
- LangChain

## Setup

1. Clone the repository
2. Create a virtual environment running `python -m venv venv`
3. Activate the virtual environment running `source venv/bin/activate`
4. Install the dependencies running `pip install -r requirements.txt`
5. Run the script running `python transcript.py` to create the transcript of the video passed as a value to the variable YOUTUBE_VIDEO. This is required just the first time . Once the transcript is created, the script will skip this step.
6. Run the script running `python app.py` to answer questions about the video.

Note 1: Future version will allow pasting the video URL in the CLI and create the transcript automatically, then answer questions about the video.

Note 2: The current version of the application is using a local LLM (Ollama) and a remote vector database (Pinecone) for learning purposes only but this is not an optimal solution. Future version will use a remote LLM (OpenAI) and a remote vector database (Pinecone).

## Usage

```bash
python transcript.py
``` 

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push your changes to your fork
5. Create a pull request


### Commit Messages

We use Conventional Commits to format our commit messages.

| Prefix       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `feat`       | A new feature (triggers a **minor** version bump in SemVer).                |
| `fix`        | A bug fix (triggers a **patch** version bump in SemVer).                    |
| `docs`       | Documentation changes (README, comments, etc.).                             |
| `style`      | Code style changes (formatting, linting, no functional changes).            |
| `refactor`   | Code restructuring (no new features or bug fixes).                          |
| `perf`       | Performance improvements.                                                   |
| `test`       | Adding or modifying tests.                                                  |
| `chore`      | Maintenance tasks (build config, dependencies, CI/CD).                      |
| `revert`     | Reverting a previous commit.                                                |
| `ci`         | Changes to CI/CD pipelines.                                                 |
| `build`      | Changes affecting the build system or dependencies.                         |

---

### Format of a Conventional Commit
<type>(<scope>): <description>
[optional body]
[optional footer]


```bash
- **`<type>`**: The kind of change (`feat`, `fix`, `docs`, etc.).
- **`<scope>`** (optional): The part of the codebase affected (e.g., `auth`, `api`, `ui`).
- **`<description>`**: A concise summary of changes (imperative tense: "add" instead of "added").
- **Body** (optional): Detailed explanation if needed.
- **Footer** (optional): References like `BREAKING CHANGE:` or issue links (`Closes #123`).
```

---

### Examples

#### 1. Simple Feature Addition
```bash
git commit -m "feat(auth): add OAuth2 login support"
```

#### 2. Bug Fix with Issue Reference
```bash
git commit -m "fix(api): handle null response in user endpoint

Closes #456"
```
#### 3. Breaking Change (Major Version Bump)
```bash

git commit -m "feat(db): migrate to PostgreSQL

BREAKING CHANGE: drops support for MongoDB"
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


