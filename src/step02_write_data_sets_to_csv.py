import pandas as pd
from .step01_read_data import get_heros_data
from .defending import get_eye_color_based_data
from .defending import get_race_based_data


def main():
    heros = get_heros_data()
    # print(heros)
    columns = heros[0]
    rows = heros[1:]
    print("Data received. Createing a Pandas Data frame")
    df = pd.DataFrame(rows, columns=columns)

    eye_color_df = get_eye_color_based_data(df)
    print(eye_color_df)

    race_df = get_race_based_data(df)
    print(race_df)

    # Writing data to csv files
    eye_color_df.to_csv("data/eye_color.csv")
    print("data/eye_color.csv has been written")

    race_df.to_csv("data/race.csv")
    print("data/race.csv has been written")


if __name__ == "__main__":
    main()
