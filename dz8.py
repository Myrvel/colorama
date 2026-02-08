import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class StudentSimulator:
    def __init__(self, name, days=5):
        self.name = name
        self.days = days

    def __iter__(self):
        for day in range(1, self.days + 1):
            activity = random.choice(["вчиться", "відпочиває", "грає", "читає"])
            result = f"День {day}: студент {self.name} {activity}"
            logging.info(result)   # Логування кожного дня
            yield result
student = StudentSimulator("Ростислав", days=5)
for day_result in student:
    print(day_result)