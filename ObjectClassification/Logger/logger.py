import datetime
import logging
import json

LOG_FILE = 'Smart-Convayor-Belt/ObjectClassification/Logger/log.txt'
COUNT_FILE = 'Smart-Convayor-Belt/ObjectClassification/Logger/logcount.json'

class PredictionLogger:
    @staticmethod
    def log_prediction(prediction):
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
        logging.info(f'Prediction: {prediction}; Time: {datetime.datetime.now().strftime("%I:%M%p, %B %d, %Y")}')

    @staticmethod
    def update_count(prediction):
        try:
            with open(COUNT_FILE, 'r') as file:
                data = json.load(file)
                data[str(prediction)] += 1

            with open(COUNT_FILE, 'w') as file:
                json.dump(data, file, indent=2)

        except FileNotFoundError:
            with open(COUNT_FILE, 'w') as file:
                data = {
                    "0": 0,
                    "1": 0,
                    "2": 0,
                }

                data[str(prediction)] += 1
                json.dump(data, file, indent=2)

        except json.decoder.JSONDecodeError:
            # Handle the case where the file is empty or not in a valid JSON format
            with open(COUNT_FILE, 'w') as file:
                data = {
                    "0": 0,
                    "1": 0,
                    "2": 0,
                }

                data[str(prediction)] += 1
                json.dump(data, file, indent=2)

    @staticmethod
    def clearEverything():
        with open(COUNT_FILE, 'w') as file:
            data = {
                "0": 0,
                "1": 0,
                "2": 0,
            }

            json.dump(data, file, indent=2)

        with open(LOG_FILE, 'w') as file:
            file.write('')