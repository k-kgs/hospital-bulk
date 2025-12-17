import csv
from io import StringIO

REQUIRED_FIELDS = {"name", "address"}
MAX_ROWS = 20

def read_csv(content: bytes):
    text = content.decode("utf-8")
    reader = csv.DictReader(StringIO(text))

    if not reader.fieldnames:
        raise ValueError("Missing CSV headers")

    if not REQUIRED_FIELDS.issubset(reader.fieldnames):
        raise ValueError("Invalid CSV headers")

    rows = list(reader)

    if not rows:
        raise ValueError("CSV is empty")

    if len(rows) > MAX_ROWS:
        raise ValueError("CSV exceeds 20 rows")

    return rows

