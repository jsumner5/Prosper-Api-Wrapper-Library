from RequestHandler import RequestHandler


class Note:


    def __init__(self, ):
        self.rh = RequestHandler()


    def get_notes(self):
        notes = self.rh.get('notes/')
        return notes

    def get_note_by_id(self, note_id):
        note = self.rh.get('notes/' + note_id)
        return note