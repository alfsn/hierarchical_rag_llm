import re

class PrivacyFilter:
    def __init__(self):
        self.patterns = [
            (r'\b\d{3}-\d{2}-\d{4}\b', 'SSN'),  # SSN
            (r'\b\d{16}\b', 'CREDIT_CARD'),  # Credit Card
            (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'EMAIL')  # Email
        ]

    def filter(self, text):
        for pattern, replacement in self.patterns:
            text = re.sub(pattern, f'[REDACTED {replacement}]', text)
        return text