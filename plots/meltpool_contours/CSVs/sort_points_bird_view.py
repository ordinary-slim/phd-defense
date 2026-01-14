import pandas as pd
import numpy as np
import argparse

def main(csv_file):
    contour = pd.read_csv(csv_file)
    contour = contour.rename(columns={"Points:0" : "x",
                                      "Points:1" : "y",
                                      "Points:2" : "z"})
    contour = contour.drop(columns=["z"])
    upper_points = contour.loc[contour["y"] >= 0.0]
    lower_points = contour.loc[contour["y"] < 0.0]

    upper_points = upper_points.sort_values(by=["x"])
    lower_points = lower_points.sort_values(by=["x"], ascending=False)

    sorted_points = pd.concat([upper_points, lower_points])

    data_set_name = csv_file.split(".")[0]
    new_file = data_set_name + "_sorted.csv"

    sorted_points.to_csv(new_file, index=False)
    print(f"wrote {new_file}")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file')
    args = parser.parse_args()
    main(args.csv_file)
