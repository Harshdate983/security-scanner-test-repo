# Security Testing Notes

This repository intentionally contains fake security findings for scanner testing. The values are **not real credentials** and are deliberately unusable.

| File | Test Case | Expected Severity |
| --- | --- | --- |
| `app.py` | Hardcoded password | High |
| `app.py` | Hardcoded API key | High |
| `config/config.py` | Suspicious `sk-` value | High |
| `authentication.py` | Hardcoded token | High |
| `database.py` | Hardcoded DB password | High |
| `frontend/script.js` | Fake API key | High |

The repository is a controlled test environment, not a production application.
