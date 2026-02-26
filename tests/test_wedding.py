import pytest
from wedding import Wedding, Guest, SpecialGuest
import pytest
from unittest.mock import patch
from wedding import send_email_invitation

# --- Unit Tests for Wedding Guest Manager ---


def test_send_and_accept_invitation():
    w = Wedding("Anna", "Nazar")
    w.send_invitation("Alex", "alex@email.com")
    guest = w.get_guest_by_email("alex@email.com")
    assert guest is not None
    guest.accept_invitation()
    assert guest in w.confirmed_guest_list


def test_decline_invitation():
    w = Wedding("Anna", "Nazar")
    w.send_invitation("Alex", "alex@email.com")
    guest = w.get_guest_by_email("alex@email.com")
    guest.decline_invitation()
    assert guest not in w.confirmed_guest_list


def test_special_guest_plus_one():
    w = Wedding("Anna", "Nazar")
    w.send_invitation("Sara", "sara@email.com", is_special=True)
    special = w.get_guest_by_email("sara@email.com")
    assert isinstance(special, SpecialGuest)
    special.invite_plus_one("Mike", "mike@email.com")
    plus_one = w.get_guest_by_email("mike@email.com")
    assert plus_one is not None
    assert plus_one.inviting_guest_email == "sara@email.com"


def test_no_duplicate_guests():
    w = Wedding("Anna", "Nazar")
    w.send_invitation("Alex", "alex@email.com")
    w.send_invitation("Alex", "alex@email.com")
    guests = [inv.guest.email for inv in w.invitation_list]
    assert guests.count("alex@email.com") == 1


def test_export_import_guests(tmp_path):
    from wedding import Wedding
    w = Wedding("Anna", "Nazar")
    w.send_invitation("Alex", "alex@email.com")
    csv_file = tmp_path / "guests.csv"
    w.export_guests_to_csv(str(csv_file))
    w2 = Wedding("Anna", "Nazar")
    w2.import_guests_from_csv(str(csv_file))
    assert w2.get_guest_by_email("alex@email.com") is not None


@patch('wedding.yagmail.SMTP')
def test_send_email_invitation(mock_smtp):
    send_email_invitation("test@example.com", "Subject", "Body")
    mock_smtp.return_value.send.assert_called_once()
