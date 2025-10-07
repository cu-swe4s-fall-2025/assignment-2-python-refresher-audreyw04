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
    parser.add_argument('--calculate',
                        type=str,
                        choices=['mean', 'median', 'sd'],
                        required=False,
                        help='Calculate mean, median or standard '
                        'deviation of the number of fires in the given '
                        'country')
    return parser.parse_args()


def main():
    args = parse_args()
    # get array of number of fires in the given
    # country using get_column function
    fires = mu.get_column(args.file_name,
                          args.country_column,
                          args.country,
                          result_column=args.fires_column)

    # perform calculation if specified and print result
    if len(fires) == 0:
        print("No data to perform calculations.")
        return
    else:
        if args.calculate == 'mean':
            mean = mu.calculate_mean(fires)
            print(f"Mean number of fires: {mean}")
        elif args.calculate == 'median':
            median = mu.calculate_median(fires)
            print(f"Median number of fires: {median}")
        elif args.calculate == 'sd':
            sd = mu.calculate_sd(fires, mu.calculate_mean(fires))
            print(f"Standard Deviation of number of fires: {sd}")
    if not args.calculate:
        print(fires)


if __name__ == '__main__':
    main()
