from wedding import Wedding

# Create wedding
w = Wedding("Anna", "Nazar")

# Send invitations
w.send_invitation("Alex", "alex@email.com")
w.send_invitation("Sara", "sara@email.com", is_special=True)

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
