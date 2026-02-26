from src.wedding import Wedding
from src.wedding import send_email_invitation

# Create wedding
w = Wedding("Anna", "Nazar")

# Send invitations
w.send_invitation("Alex", "alex@email.com")
w.send_invitation("Sara", "sara@email.com", is_special=True)

# Example: send an email invitation (uncomment and set a real email to use)
# send_email_invitation(
#     guest_email="guest@example.com",
#     subject="Test Wedding Invitation",
#     body="This is a test email from a wedding project!"
# )

# Accept invitation
guest = w.get_guest_by_email("alex@email.com")
guest.accept_invitation()

# Special guest invites plus one
special = w.get_guest_by_email("sara@email.com")
special.invite_plus_one("Mike", "mike@email.com")

# Print results
print("Confirmed Guests:")
for g in w.confirmed_guest_list:
    print(g.name)

print("\nAll Invitations:")
for inv in w.invitation_list:
    print(inv.guest.email, "-", inv.status)


# Test exporting guests to csv
w.export_guests_to_csv("guests_export.csv")
print("Guest list exported to guests_export.csv")


# New wedding object to see that import work
w2 = Wedding("Anna", "Nazar")
w2.import_guests_from_csv("guests_export.csv")
print("Imported guests:")
for inv in w2.invitation_list:
    print(inv.guest.name, inv.guest.email)
