import json
from time import sleep
from datetime import datetime
import datetime as dt
from playsound import playsound


class TwentyTwentyTwenty:
    def __init__(self, mediaPath: str, reminderIntervallInMin: float = 20, pauseTimeInSec: float = 20) -> None:
        self.lastReminder = datetime.now()
        self.reminderIntervallInMin = dt.timedelta(
            minutes=reminderIntervallInMin)
        self.pauseTimeInSec = dt.timedelta(seconds=pauseTimeInSec)
        try:
            self.reminderSoundPath = mediaPath

        except Exception as e:
            self._onError(e, "Sound file not found!")

    def run(self):
        while True:
            nextReminderTime = self.lastReminder + self.reminderIntervallInMin
            timeToNextReminder = (
                nextReminderTime - self.lastReminder).total_seconds()
            sleep(timeToNextReminder)

            playsound(self.reminderSoundPath)

            beginningOfPause = datetime.now()
            nextReminderTime = beginningOfPause + self.pauseTimeInSec
            timeToNextReminder = (
                nextReminderTime - beginningOfPause).total_seconds()
            sleep(timeToNextReminder)

            playsound(self.reminderSoundPath)

            self.lastReminder = datetime.now()

    def _onError(self, exception: Exception, errorMsg: str = "Something went wrong!"):
        try:
            with open("error.log", "w") as file:
                file.write(f"{errorMsg}\n{exception}")

        except:
            with open("error.log", "x") as file:
                file.write(f"{errorMsg}\n{exception}")


if __name__ == "__main__":
    with open("reminder.json", "r") as config:
        configurations = json.load(config)
        workTimeMin = configurations["workTimeMin"]
        pauseTimeSec = configurations["pauseTimeSec"]
        path = configurations["pathToReminder"]

        del configurations

    TwentyTwentyTwenty(path, workTimeMin, pauseTimeSec).run()
