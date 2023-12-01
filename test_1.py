'''Python script to check the validity of log messages. The two main functions
are is_log_line which verifies a log messages is valid, and get_dict which
assumes a valid log line and extracts the key information.'''

import re

MIN_MESSAGE_LENGTH = 10


def extract_timestamp(line: str) -> tuple[str] | None:
    '''Takes a log line and returns the timestamp and the log line
    excluding the timestamp as a tuple in that order if the log line
    contains such a timestamp otherwise returns None.'''

    # Define a regex pattern for a timestamp
    timestamp_pattern = re.compile(r'\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}')

    # Search for this pattern in the line
    match = timestamp_pattern.search(line)
    if not match:
        return None

    # If a timestamp is in the line, remove it
    timestamp = match.group()
    index = line.find(timestamp)
    return (timestamp, line[:index] + line[index+len(timestamp):])


def extract_log_level(line: str) -> tuple[str] | None:
    '''Takes a log line and returns the log level and the log line
    excluding the log level as a tuple in that order if the log line
    contains such a log level otherwise returns None.'''

    # Check if the line has a valid log level
    log_levels = ['INFO', 'TRACE', 'WARNING']
    if all(level not in line for level in log_levels):
        return None

    # Separate the log level from the rest of the line
    for level in log_levels:
        index = line.find(level)
        return (level, line[:index] + line[index+len(level):])


def is_log_line(line: str) -> bool | None:
    """Takes a log line and returns True if it is a valid log line
    and returns None if it is not."""

    # Check timestamp is in the line
    if extract_timestamp(line) is not None:
        line = extract_timestamp(line)[1]
    else:
        return None

    # Check the log level is in the line
    if extract_log_level(line) is not None:
        line = extract_log_level(line)[1]
    else:
        return None

    # Check the line contains a message
    if len(line) >= MIN_MESSAGE_LENGTH:
        return True
    return None


def get_dict(line: str) -> dict:
    """Takes a valid log line and returns a dict with
    `timestamp`, `log_level`, `message` keys."""

    log_info = {}

    log_info['timestamp'] = extract_timestamp(line)[0]
    line = extract_timestamp(line)[1]

    log_info['log_level'] = extract_log_level(line)[0]
    line = extract_log_level(line)[1]

    # Extract the message from the line
    log_info['message'] = line.lstrip().rstrip()

    return log_info


# YOU DON'T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time

    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
