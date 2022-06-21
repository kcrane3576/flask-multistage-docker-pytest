import logging
from flask import Flask


log_level = logging.DEBUG
log_level_name = logging.getLevelName(log_level)

logger = logging.getLogger(__name__)
logger.setLevel(log_level)
formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(process)d:%(thread)d | %(filename)s | %(funcName)s | %(lineno)d | %(message)s')

file_handler = logging.FileHandler('project/logs/main.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.info("Log Level: '%s'", log_level_name)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    logger.info("hello_world")

    return "hello_world"


if __name__ == "__main__":
    app.run()