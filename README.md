# Security Scanner Test Repository

## Purpose

This is a small demonstration/test application designed to validate repository security scanning, recursive file discovery, source-file detection, vulnerability detection, severity classification, line-number detection, and finding aggregation.

## Project Structure

- `app.py` — small Flask-style application with intentional fake findings
- `config/` — Python and JSON configuration examples
- `src/` — Python source files, including clean and intentionally vulnerable examples
- `frontend/` — HTML, JavaScript, and CSS files
- `tests/` — simple application and security tests
- `docs/` — scanner test notes and expected findings

## Running the Example

Install the minimal dependency with `pip install -r requirements.txt`, then run `python app.py`.

The application is intentionally simple and is not intended for production use.

## Security Testing

The repository intentionally contains fake passwords, API keys, tokens, and credential-like values so a security scanner can exercise detection and severity classification across multiple file types.

## Important Note

All credentials, secrets, tokens, and password-like values appearing in this repository are **fake test values**. They are deliberately unusable and must never be treated as real credentials.
