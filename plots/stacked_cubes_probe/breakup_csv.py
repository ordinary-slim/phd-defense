import argparse
import pandas as pd
import os
from pathlib import Path

def breakup_csv(input_csv, output_dir):
    ''' Read CSV file, break it up into layer_n.csv files, where n is the layer number,
    based on jumps bigger than 0.01 in the 'time' column.
    '''
    if output_dir == '':
        dataset_name = Path(input_csv).stem.rstrip(".bp")
        output_dir = f'{dataset_name}_layers'
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(input_csv)
    # Discard all rows where the increment in 'time' is larger than 0.01
    df['t_diff'] = df['time'].diff().fillna(1e6)
    df = df[df.t_diff < 0.01]
    # Recompute jumps
    df['t_diff'] = df['time'].diff().fillna(0.0)
    # Divide into layers where jumps are larger than 1.0
    df['layer'] = (df.t_diff > 1.0).cumsum()
    # Save each layer to a separate CSV file
    for layer, group in df.groupby('layer'):
        group.drop(columns=['t_diff', 'layer'], inplace=True)
        if layer%2 == 0:
            # For even layers, Y is L and X is W
            group.rename(columns={'X':'W', 'Y':'L'}, inplace=True)
        else:
            # For odd layers, Y is W and X is L
            group.rename(columns={'X':'L', 'Y':'W'}, inplace=True)
        group.to_csv(f'{output_dir}/layer_{layer}.csv', index=False)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=str, help="Path to the input CSV file")
    parser.add_argument('-o', '--output-dir', type=str, default='', help="Directory to save the output CSV files")
    args = parser.parse_args()

    breakup_csv(args.input_csv, args.output_dir)
