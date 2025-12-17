from datetime import datetime

__all__ = ["Batch"]

class Batch:
    def __init__(self, batch_id: str, total: int):
        self.batch_id = batch_id
        self.total = total
        self.processed = 0
        self.failed = 0
        self.started_at = datetime.utcnow()
        self.results = []
        self.activated = False
