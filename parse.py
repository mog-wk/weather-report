import os
import pandas as pd
import fetch


def add_csv_row(path):
    bulk = fetch.fetch()
    data = pd.DataFrame(bulk,
                        columns=["date", "time", "region", "min_temp(°C)", "max_temp(°C)",
                                 "wind(Km/h)", "wind_dir", "humidity(%)",
                                 "precipitation_prob(%)", "precipitation(mm)", "UV_index"
                                 ],
                        ).set_index("region")

    data.to_csv(f"{path}/{bulk[0][0]}-{bulk[0][1]}.csv")

if __name__ == "__main__":
    add_csv_row(os.path.dirname(os.path.abspath(__file__)) + "/test_db/")
