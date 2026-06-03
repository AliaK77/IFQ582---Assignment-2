
class CollectionItem:
    # Constructor
    def __init__(self, item_id, title, description, image_link,
                 item_type, item_category, review_status,
                 access_status, access_considerations, sensitivity_level):

        self.item_id = item_id
        self.title = title
        self.description = description
        self.image_link = image_link
        self.item_type = item_type
        self.item_category = item_category
        self.review_status = review_status
        self.access_status = access_status
        self.access_considerations = access_considerations
        self.sensitivity_level = sensitivity_level


    # Get item details
    def get_item_details(self):
        return {
            "ID": self.item_id,
            "Title": self.title,
            "Description": self.description,
            "Image Link": self.image_link,
            "Type": self.item_type,
            "Category": self.item_category,
            "Review Status": self.review_status,
            "Access Status": self.access_status,
            "Access Considerations": self.access_considerations,
            "Sensitivity Level": self.sensitivity_level
        }


    
def __repr__(self):
        details = self.get_item_details()

        return (
            f"\nCollection Item\n"
            f"------------------------\n"
            f"ID: {details['ID']}\n"
            f"Title: {details['Title']}\n"
            f"Description: {details['Description']}\n"
            f"Image Link: {details['Image Link']}\n"
            f"Type: {details['Type']}\n"
            f"Category: {details['Category']}\n"
            f"Review Status: {details['Review Status']}\n"
            f"Access Status: {details['Access Status']}\n"
            f"Access Considerations: {details['Access Considerations']}\n"
            f"Sensitivity Level: {details['Sensitivity Level']}\n"
        )



    # Display details
    def display_details(self):
        print("Collection Item Details")
        print("----------------------")
        for key, value in self.get_item_details().items():
            print(key + ":", value)


    # Update access status
    def update_access_status(self, new_status):
        self.access_status = new_status
        print("Access status updated to:", new_status)


    # Submit for review (boolean)
    def submit_for_review(self):
        self.review_status = "Pending Review"
        return True

