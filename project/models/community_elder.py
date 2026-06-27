from .user import User

class CommunityElder(User):
    # Constructor
    def __init__(self, 
            first_name, last_name, email, phone, password, 
            community_elder_id, community_name):
        # Call parent's init
        super().__init__(first_name=first_name, last_name=last_name, 
                           email=email, phone=phone, password=password)
        self.community_elder_id = community_elder_id
        self.community_name = community_name


    # Get community elder details
    def get_community_elder_details(self):
        return {
            "Community Elder ID": self.community_elder_id,
            "Full Name": self.full_name,
            "Community Name": self.community_name,
            "Email": self.email
        }


    # __repr__ 
    def __repr__(self):
        return (
            f"\nCommunity Elder\n"
            f"------------------------\n"
            f"ID: {self.community_elder_id}\n"
            f"Name: {self.full_name}\n"
            f"Community: {self.community_name}\n"
            f"Email: {self.email}\n"
        )


    # Review item
    def review_item(self, item):
        print(f"\n{self.full_name} is reviewing item:")
        print(f"Item ID: {item.item_id} | Title: {item.title}")


    # Record outcome decision 
    def record_outcome_decision(self, review, outcome, notes):
        review.update_outcome(outcome)
        review.add_notes(notes)
        print(f"{self.full_name} has recorded a decision.")
