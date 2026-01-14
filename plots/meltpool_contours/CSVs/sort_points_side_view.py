import pandas as pd
import numpy as np
import argparse

def main(csv_file):
    contour = pd.read_csv(csv_file)
    contour = contour.rename(columns={"Points:0" : "x",
                                      "Points:1" : "z",
                                      "Points:2" : "y"})
    contour = contour.drop(columns=["z"])
    contour = contour.sort_values(by=["x"])

    data_set_name = csv_file.split(".")[0]
    new_file = data_set_name + "_sorted.csv"

    contour.to_csv(new_file, index=False)
    print(f"wrote {new_file}")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file')
    args = parser.parse_args()
    main(args.csv_file)
