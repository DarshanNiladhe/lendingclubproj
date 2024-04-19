# Sample database setup
class Database:
    def __init__(self):
        self.candidates = [
            {"id": 1, "name": "John Doe", "email": "john@example.com", "skills": "Python, JavaScript"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "skills": "Java, SQL"}
        ]

    def get_candidate_by_id(self, candidate_id: int):
        candidate = next((c for c in self.candidates if c["id"] == candidate_id), None)
        if candidate:
            return candidate
        else:
            raise Exception("Candidate not found")

    def get_all_candidates(self):
        return self.candidates

