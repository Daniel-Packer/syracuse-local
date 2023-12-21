from pathlib import Path
import pandas as pd
import os

os.chdir("..")
os.chdir("..")

root_path = Path("")
data_path = root_path / "data"

if __name__ == "__main__":
    ny_chunks = []

    print("reading 2020-STATE_precinct_general.csv")
    with pd.read_csv(
        data_path / "2020-STATE_precinct_general.csv", chunksize=10000
    ) as reader:
        for chunk in reader:
            ny_chunks.append(chunk.query("state_po == 'NY'"))

    print("concatenating chunks")
    ny_df = pd.concat(ny_chunks)
    ny_df.to_csv(data_path / "2020-NY_precinct_general.csv")
