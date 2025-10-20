import scribus

def check_overflow(cell, content):
    if scribus.textOverflows(cell):
        raise scribus.ScribusException(
            f"{cell} overflowed",
            f"Failed to insert {content}"
        )