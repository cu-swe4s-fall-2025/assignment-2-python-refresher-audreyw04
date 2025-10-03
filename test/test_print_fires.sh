#!/usr/bin/env bash
set -euo pipefail

test -e ssshtest || curl -s -o ssshtest https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

source ssshtest

# run from root directory
# bash test/test_print_fires.sh

python="python3"
script="src/print_fires.py"
data="data/subset_agrofood_co2_emission.csv"

run test_no_calculate $python $script \
    --country "Albania" \
    --country_column 0 \
    --fires_column 2 \
    --file_name $data 

    assert_in_stdout "Found 5 entries for 'Albania'"
    assert_in_stdout 5
    assert_in_stdout 5
    assert_in_stdout 5
    assert_in_stdout 5
    assert_in_stdout 5
    assert_exit_code 0

run test_mean $python $script \
    --country "Belarus" \
    --country_column 0 \
    --fires_column 2 \
    --calculate mean \
    --file_name $data

    assert_in_stdout "Found 5 entries for 'Belarus'"
    assert_in_stdout "Mean number of fires: 15.8"

run test_median $python $script \
    --country "Belarus" \
    --country_column 0 \
    --fires_column 2 \
    --calculate median \
    --file_name $data

    assert_in_stdout "Found 5 entries for 'Belarus'"
    assert_in_stdout "Median number of fires: 5.0"
run test_sd $python $script \
    --country "Belarus" \
    --country_column 0 \
    --fires_column 2 \
    --calculate sd \
    --file_name $data

    assert_in_stdout "Found 5 entries for 'Belarus'"
    assert_in_stdout "Standard Deviation of number of fires: 19.446336415890784"

run test_invalid_country $python $script \
    --country "Narnia" \
    --country_column 0 \
    --fires_column 2 \
    --file_name $data

    assert_in_stdout "No entries found for 'Narnia' in column 0"
    assert_in_stdout "No data to perform calculations."
    assert_exit_code 0