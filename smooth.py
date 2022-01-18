import pandas as pd
import numpy as np
import os
import argparse


def smooth(input_path, output_path, weight=0.85):
    data = pd.read_csv(filepath_or_buffer=input_path, header=0, names=['Step', 'Value'], dtype={'Step': np.int32, 'Value': np.float64})
    print(data)
    scalar = data['Value'].values
    last = scalar[0]
    smoothed = []
    for point in scalar:
        smoothed_val = last * weight + (1 - weight) * point
        smoothed.append(smoothed_val)
        last = smoothed_val

    save = pd.DataFrame({'Step':data['Step'].values,'Value':smoothed})
    save.to_csv(output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Paths of both the input file and output file')
    parser.add_argument('--input', type=str, help='Path of the input file')
    parser.add_argument('--output', type=str, help='Path of the output file')
    parser.add_argument('--weight', type=float, help='Smooth weight')
    args = parser.parse_args()
    smooth(args.input, args.output, args.weight)