import pandas as pd
import re

PATTERN = r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'

def parse_log(file_path):

    data = []

    with open(file_path,"r",encoding="utf-8") as file:

        for line in file:

            match = re.match(PATTERN,line)

            if match:

                data.append(match.groups())

    df = pd.DataFrame(
        data,
        columns=[
            "IP",
            "Timestamp",
            "Request",
            "Status",
            "Size"
        ]
    )

    return df