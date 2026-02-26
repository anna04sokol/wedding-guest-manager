# Happea Wedding Manager

A Python object-oriented project that manages wedding invitations, RSVP tracking, CSV data handling, and email invitations.

## Features

- Send invitations
- Accept or decline RSVP
- Track confirmed guests
- Special guests can invite a plus-one
- Export/import guest list to CSV
- Send email invitations to guests

## How to Run

1. Download files
2. Install requirements: `pip install -r requirements.txt`
3. Set up your `.env` file with your email credentials (see README for details)
4. Run: `python demo.py`

## CSV Export/Import

- Export guests: `w.export_guests_to_csv("guests_export.csv")`
- Import guests: `w.import_guests_from_csv("guests_export.csv")`

## Testing & Coverage

Run all unit tests:

```
PYTHONPATH=src pytest
```

Check test coverage:

```
PYTHONPATH=src pytest --cov=src
```

Generate a detailed HTML coverage report:

```
PYTHONPATH=src pytest --cov=src --cov-report=html
```

Open `htmlcov/index.html` in your browser to see which lines are covered.

## Email Invitations

- Send an email: `send_email_invitation(guest_email, subject, body)`
- Credentials are stored securely in a `.env` file
