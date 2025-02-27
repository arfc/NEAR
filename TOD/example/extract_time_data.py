import os
import re
import csv
import pandas as pd

import numpy as np
import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.use('../../plotting.mplstyle')

mycolors = ["332288", "117733", "44AA99", "88CCEE", "DDCC77", "CC6677", "AA4499", "882255"]

# Extract data from a single file
def extract_data(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Regular expressions to extract values
    patterns = {
        "task_clock": r"([\d,]+\.?\d*) msec task-clock",
        "context_switches": r"([\d,]+) +context-switches",
        "cpu_migrations": r"([\d,]+) +cpu-migrations",
        "page_faults": r"([\d,]+) +page-faults",
        "cycles": r"([\d,]+) +cycles",
        "instructions": r"([\d,]+) +instructions",
        "branches": r"([\d,]+) +branches",
        "branch_misses": r"([\d,]+) +branch-misses",
        "time_elapsed": r"([\d.]+) seconds time elapsed",
        "user_time": r"([\d.]+) seconds user",
        "sys_time": r"([\d.]+) seconds sys",
    }

    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            data[key] = match.group(1).replace(",", "")  # Remove commas for numeric conversion
        else:
            data[key] = None  # Fill missing data with None

    return data

    def extract(input_dir, output_csv):

        # Process all text files in the directory
        all_data = []
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".txt"):  # Process only text files
                file_path = os.path.join(input_dir, file_name)
                data = extract_data(file_path)
                data["file_name"] = file_name  # Add file identifier
                all_data.append(data)

        # Write to CSV
        csv_headers = ["file_name"] + list(patterns.keys())
        with open(output_csv, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(all_data)

        print(f"CSV file '{output_csv}' created successfully!")

if __name__ == '__main__':
    # Directory containing the text files
    extract("tod_reactor", "tod_reactor_performance_data.csv")
    extract("cycamore_reactor", "cycamore_reactor_performance_data.csv")

    # read the csv in with pandas and make a DataFrame
    file = 'cycamore_reactor_performance_data.csv'
    cycamore_df = pd.read_csv(file)

    # remove the 0th row with the callgrind file, all NaNs
    cycamore_df = cycamore_df.drop(0)

    # read the csv in with pandas and make a DataFrame
    tod_file = 'tod_reactor_performance_data.csv'
    tod_df = pd.read_csv(tod_file)

    tod_df['isn'] = tod_df['instructions']/tod_df['cycles']
    cycamore_df['isn'] = cycamore_df['instructions']/cycamore_df['cycles']


    for col in tod_df.columns.to_list()[1:]:
        tod_df.loc[11,col] = tod_df[col][1:11].mean()
        cycamore_df.loc[11,col] = cycamore_df[col][1:11].mean()

        tod_df.loc[12,col] = tod_df[col][1:11].max()
        cycamore_df.loc[12,col] = cycamore_df[col][1:11].max()

        tod_df.loc[13,col] = tod_df[col][1:11].min()
        cycamore_df.loc[13,col] = cycamore_df[col][1:11].min()

        tod_df.loc[14,col] = tod_df[col][1:11].std()
        cycamore_df.loc[14,col] = cycamore_df[col][1:11].std()

    tod_df.loc[11,'file_name'] = 'mean'
    cycamore_df.loc[11,'file_name'] = 'mean'

    tod_df.loc[12,'file_name'] = 'max'
    cycamore_df.loc[12,'file_name'] = 'max'

    tod_df.loc[13,'file_name'] = 'min'
    cycamore_df.loc[13,'file_name'] = 'min'

    tod_df.loc[14,'file_name'] = 'std'
    cycamore_df.loc[14,'file_name'] = 'std'

    cycamore_task_clock_mean = cycamore_df["task_clock"][:10].mean()
    tod_task_clock_mean = tod_df['task_clock'][:10].mean()

    speedup = cycamore_task_clock_mean / tod_task_clock_mean
    print(f"Speedup of tod Reactor over Cycamore Reactor: {speedup:.4f}x")




    fig, axs = plt.subplots(nrows=1, ncols=1) # , figsize=(12, 6)

    # generate some random test data
    all_data = [tod_df['task_clock'][:10]/1000, cycamore_df['task_clock'][:10]/1000]

    # plot violin plot
    axs.violinplot(all_data,
                    showmeans=False,
                    showmedians=True)

    axs.yaxis.grid(True)
    axs.set_xticks([y + 1 for y in range(len(all_data))],
                    labels=['TOD', 'Cycamore'])
    axs.set_ylabel('Time Clock [sec]')

    plt.savefig('time_clock_violin')
    plt.clf()
    plt.close()




    fig, axs = plt.subplots(nrows=1, ncols=1) # , figsize=(12, 6)

    # generate some random test data
    all_data = [tod_df['isn'][:10], cycamore_df['isn'][:10]]

    # plot violin plot
    axs.violinplot(all_data,
                    showmeans=False,
                    showmedians=True)

    axs.yaxis.grid(True)
    axs.set_xticks([y + 1 for y in range(len(all_data))],
                    labels=['TOD', 'Cycamore'])
    axs.set_ylabel('Instructions per Cycle')

    plt.savefig('ins_per_cyc_violin')
    plt.clf()
    plt.close()




    fig, axs = plt.subplots(nrows=1, ncols=1) # , figsize=(12, 6)

    # generate some random test data
    all_data = [tod_df['instructions'][:10], cycamore_df['instructions'][:10]]

    # plot violin plot
    axs.violinplot(all_data,
                    showmeans=False,
                    showmedians=True)

    axs.yaxis.grid(True)
    axs.set_xticks([y + 1 for y in range(len(all_data))],
                    labels=['TOD', 'Cycamore'])
    axs.set_ylabel('Instructions [#]')

    plt.savefig('is_violin')
    plt.clf()
    plt.close()





    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 7))

    # Fixing random state for reproducibility
    np.random.seed(19680801)


    # generate some random test data
    instructions_data = [tod_df['instructions'][:10], cycamore_df['instructions'][:10]]

    ins_data = [tod_df['isn'][:10], cycamore_df['isn'][:10]]


    axs[0].violinplot(instructions_data,
                    showmeans=False,
                    showmedians=True)

    first = plt.violinplot(ins_data,
                    showmeans=False,
                    showmedians=True)
    second = plt.violinplot(ins_data,
                    showmeans=False,
                    showmedians=True)
    # axs[1].second


    axs[0].yaxis.grid(True)
    axs[0].set_xticks([y + 1 for y in range(len(all_data))],
                    labels=['TOD', 'Cycamore'])
    axs[0].set_ylabel('Instructions [#]')

    axs[1].yaxis.grid(True)
    axs[1].set_xticks([y + 1 for y in range(len(all_data))],
                    labels=['TOD', 'Cycamore'])
    axs[1].set_ylabel('Instructions/Cycle [#]')

    plt.savefig('ins_cyc_both')
    plt.clf()
    plt.close()

