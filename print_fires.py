import argparse
import my_utils as mu

def parse_args():
    """
    This function works as a parse command line arguments
    """
    parser = argparse.ArgumentParser(
        description='Print the number of fires in a given country')
    parser.add_argument('--country',
                        type=str,
                        default='Algeria',
                        help='Country name')
    parser.add_argument('--country_column',
                        type=int,
                        default=1,
                        help='Column number for country names')
    parser.add_argument('--fires_column',
                        type=int,
                        default=4,
                        help='Column number for number of fires')
    parser.add_argument('--file_name',
                        type=str,
                        default='Agrofood_co2_emission.csv',
                        help='CSV file name')
    return parser.parse_args()

def main():
    args = parse_args()
    fires = mu.get_column(args.file_name,
                          args.country_column,
                          args.country,
                          result_column=args.fires_column)
    print(fires)

if __name__ == '__main__':
    main()