from datetime import datetime
from .user import User

class LibraryStaff(User):
    # Constructor
   def __init__(self, first_name, last_name, email, phone, password, position_title, start_date=None, is_admin=False, staff_id=None, user_id=None):
      # Call parent's init
      super().__init__(first_name=first_name, last_name=last_name, 
                        email=email, phone=phone, password=password, ID=user_id)
      self.staff_id = staff_id
      self.collection_items = []
      self.position_title = position_title
      # The defaults below are already covered by the form, but could
      # be helpful if a user is created in code without using the form
      if is_admin:
         self.is_admin = 1
      else:
         self.is_admin = 0
      if start_date:
         self.start_date = start_date
      else:
         self.start_date = datetime.now()


   #  Get staff details
   def get_staff_details(self):
      admin = str(bool(self.is_admin))
      return {
         "staff ID": self.staff_id,
         "Full Name": self.full_name,
         "Email": self.email,
         "Position": self.position_title,
         "Is Admin": admin
      }


   #  __repr__
   def __repr__(self):
      admin = str(bool(self.is_admin))
      return (
         f"\nLibrary staff\n"
         f"------------------------\n"
         f"ID: {self.staff_id}\n"
         f"Name: {self.full_name}\n"
         f"Email: {self.email}\n"
         f"Position: {self.position_title}\n"
         f"Is Admin: {admin}\n"
         f"Number of Items Managed: {len(self.collection_items)}\n"
      )


   # Add item
   def add_item(self, item):
      self.collection_items.append(item)
      print("Item added successfully.")


   # Edit item (simple example: update title)
   def edit_item(self, item_id, new_title):
      for item in self.collection_items:
         if item.item_id == item_id:
               item.title = new_title
               print("Item updated successfully.")
               return
      print("Item not found.")


   #  View review status of all items
   def view_review_status(self):
      print("\nReview Status of Items")
      print("------------------------")

      for item in self.collection_items:
         print(f"Item ID: {item.item_id} | Title: {item.title} | Review Status: {item.review_status}")
