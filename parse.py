import os
from sys import abiflags
import pandas as pd
import fetch


def save_csv(path, analyze_data=False):
    bulk = fetch.fetch()
    df = pd.DataFrame(bulk,
                        columns=["date", "time", "region",
                      "min_temp", "max_temp",
                      "wind", "wind_dir", "humidity",
                      "precipitation_prob", "precipitation",
                      "UV_index"
                         ],
                        ).set_index("region")
    if analyze_data:
        df = analyze(df, keep=True)
    df.to_csv(f"{path}/{bulk[0][0]}-{bulk[0][1]}.csv")

def from_csv(path, analyze_data=False):
    df = pd.read_csv(path).set_index("region")
    if analyze_data:
        df = analyze(df)

def analyze(df: pd.DataFrame, keep=False):
    #df.describe()
    avg_temp = pd.Series((df["min_temp"] + df["max_temp"]) / 2, name="avg_temp")
    df = pd.merge(df, avg_temp, left_index=True, right_index=True)

    if keep:
        return df

    exit(0)

if __name__ == "__main__":
    test_dir = os.path.dirname(os.path.abspath(__file__)) + "/test_db/"
    #save_csv(test_dir)
    from_csv(test_dir + "2024-04-24-12:07:14.csv", analyze_data=True)


