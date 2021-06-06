import datetime                     #IMPORTING DATE TIME MODULE IN ORDER TO FETCH THE CURRENT DATE.

#--------------------------------</ CLASS NOTE>------------------------------------#
class Note:
    """Represent a note in the notebook. Match against a
     string in searches and store tags for each note."""

    last_id=0               #Unique id for each Note Type Object for match functionality.

    def __init__(self,memo,tags=""):
        """initialize a note with memo and optional
         space-separated tags. Automatically set the note's
         creation date and a unique id."""

        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags

        Note.last_id+=1

        self.id = Note.last_id


    def match(self,filter):
        """Determine if this note matches the filter
         text. Return True if it matches, False otherwise.
         Search is case sensitive and matches both text and
         tags."""


        return filter in self.memo or filter in self.tags

#--------------------------------</ CLASS NOTEBOOK>------------------------------------#
class NoteBook:
    """Represent a collection of notes that can be tagged,
     modified, and searched."""

    def __init__(self):
        """Initialize a notebook with an empty list."""
        self.notes = []


    def new_note(self,memo,tags=""):
        """Create a new note and add it to the list."""

        self.notes.append(Note(memo,tags))              #THIS IS COMPOSITION



    def _find_note(self,note_id):                               #PROTECTED METHOD FOR INTERNAL USE:-
        """Locate the note with the given id and Return it"""

        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None



    def modify_memo(self,note_id,memo):
        """Find the note with the given id and change its
         memo to the given value."""

        self._find_note(note_id).memo = memo


    def modify_tags(self,note_id,tags):
        """Find the note with the given id and change its
         tags to the given value."""

        self._find_note(note_id).tags = tags

    def search(self,filter):
        """Find all notes that match the given filter
         string."""

        return [note for note in self.notes if note.match(filter)]


#--------------------------------</ CLASS MENU>------------------------------------#
import sys

class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.notebook = NoteBook()          #AN ATTRIBUTE WHICH IS AN INSTANCE OF NOTEBOOK CLASS:-

        self.choices = {

            "1" : self.show_notes,
            "2" : self.search_notes,
            "3" : self.add_note,
            "4" : self.modify_note,
            "5" : self.quit,
        }

    def display_menu(self):
        print(f"WELCOME TO NOTEBOOK MENU:-\n"
              f"1. Show all Notes\n"
              f"2. Search Notes\n"
              f"3. Add Note\n"
              f"4. Modify Note\n"
              f"5. quit")



    def run(self):
        """Display the menu and respond to choices."""

        while True:
            self.display_menu()

            choice = input("Enter the choice Number:")

            action = self.choices.get(choice)

            if action:
                action()

            else:
                print(f"{choice} is not a valid option")


    def show_notes(self,notes=None):
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print(f"The id of the Note is : {note.id}\n"
                  f"The memo of the Note is : {note.memo}\n"
                  f"The tags of the Note is : {note.tags}")



    def search_notes(self):

        filter = input('Search For : ')

        notes = self.notebook.search(filter)

        self.show_notes(notes)


    def add_note(self):

        memo = input('Enter the memo :')

        self.notebook.new_note(memo)

        print(f"Your note has been Added!")


    def modify_note(self):

        id = input("Enter ID of the Note which you want to change :")

        memo = input("Enter the modified memo : ")

        tags = input("Enter the modified tags : ")

        if memo:
            self.notebook.modify_memo(id,memo)

        if tags:
            self.notebook.modify_tags(id,tags)


    def quit(self):
        print(f"Thanks For Using The NoteBook:)")
        sys.exit(0)




if __name__ == "__main__":
    Menu().run()

