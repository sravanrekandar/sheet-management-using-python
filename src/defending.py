def get_eye_color_based_data(df):
    # The logic to extract the required data is simple one liner here
    # However, you can add complex logic here based on your use case
    result_df = df[["id", "name", "Gender", "Eye color"]]
    return result_df


def get_race_based_data(df):
    # The logic to extract the required data is simple one liner here
    # However, you can add complex logic here based on your use case
    result_df = df[["id", "name", "Race"]]
    return result_df
