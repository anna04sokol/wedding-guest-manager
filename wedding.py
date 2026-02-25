from typing import List, Optional


class Wedding:
    def __init__(self, bride_name: str, groom_name: str) -> None:
        self.bride_name: str = bride_name
        self.groom_name: str = groom_name
        self.confirmed_guest_list: List["Guest"] = []
        self.invitation_list: List["Invitation"] = []

    def send_invitation(self, name: str, email: str, is_special: bool = False) -> None:
        if self.get_guest_by_email(email):
            print(f"Guest with email {email} already exists")
            return

        guest: Guest = SpecialGuest(name, email, self) if is_special else Guest(name, email, self)
        invitation: Invitation = Invitation(guest)
        self.invitation_list.append(invitation)

    def retrieve_invitation(self, email: str) -> Optional["Invitation"]:
        for invitation in self.invitation_list:
            if invitation.guest.email == email:
                return invitation
        return None

    def get_guest_by_email(self, email: str) -> Optional["Guest"]:
        for invitation in self.invitation_list:
            if invitation.guest.email == email:
                return invitation.guest
        return None


class Invitation:
    def __init__(self, guest: "Guest") -> None:
        self.guest: Guest = guest
        self.status: str = "pending"

    def accept(self) -> None:
        self.status = "accepted"

    def decline(self) -> None:
        self.status = "declined"


class Guest:
    def __init__(self, name: str, email: str, wedding: Wedding, inviting_guest_email: Optional[str] = None) -> None:
        self.name: str = name
        self.email: str = email
        self.wedding: Wedding = wedding
        self.inviting_guest_email: Optional[str] = inviting_guest_email

    def accept_invitation(self) -> None:
        invitation = self.wedding.retrieve_invitation(self.email)
        if invitation:
            invitation.accept()
            if self not in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.append(self)

    def decline_invitation(self) -> None:
        invitation = self.wedding.retrieve_invitation(self.email)
        if invitation:
            invitation.decline()
            if self in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.remove(self)


class SpecialGuest(Guest):
    def __init__(self, name: str, email: str, wedding: Wedding) -> None:
        super().__init__(name, email, wedding)
        self.plus_one: Optional[Guest] = None

    def invite_plus_one(self, name: str, email: str) -> None:
        if self.plus_one:
            print("Already invited a plus one")
            return

        if self.wedding.get_guest_by_email(email):
            print(f"Guest with email {email} already exists")
            return

        self.wedding.send_invitation(name, email, is_special=False)
        invitation = self.wedding.retrieve_invitation(email)
        if invitation:
            self.plus_one = invitation.guest
            self.plus_one.inviting_guest_email = self.email
            print(f"Plus one invitation sent to {email}")

    def uninvite_plus_one(self) -> None:
        if self.plus_one:
            invitation = self.wedding.retrieve_invitation(self.plus_one.email)
            if invitation and invitation in self.wedding.invitation_list:
                self.wedding.invitation_list.remove(invitation)

            if self.plus_one in self.wedding.confirmed_guest_list:
                self.wedding.confirmed_guest_list.remove(self.plus_one)

            self.plus_one = None