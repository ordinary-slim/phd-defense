import pandas as pd
import argparse

def main(input_csv, output_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    df['x'] *= -1e-3
    df['x'] += +(0.000236*1e3) - (-38.72943637745948*1e-3)
    df.sort_values(by='x', inplace=True)

    # Save the modified DataFrame back to a new CSV file
    df.to_csv(output_csv, index=False)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='data.csv', help='Input CSV file path')
    parser.add_argument('-o', '--output', type=str, default='scaled_data.csv', help='Output CSV file path')
    args = parser.parse_args()
    main(args.input, args.output)
