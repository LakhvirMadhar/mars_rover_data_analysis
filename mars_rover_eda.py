"""
GOAL:
Using the Mars rover manifest API, do an exploratory data analysis.

-----BASIC INFO-----
* [DONE] Make a print statement on the basic info of each rover.

-----MISSION DATA ANALYSIS-----
* [DONE] How long did it take each rover to get to Mars?
* [DONE] If the status of a rover is complete, how long was their mission?
* [DONE] Which rover had the longest mission?

-----PHOTOS DATA ANALYSIS-----
* [DONE] Which rover took the most total photos?

For each rover:
    * [DONE] Which sol/earth date had the most photos taken?
    * [DONE] What's the average of photos taken.
    * [DONE] What's the median amount of photos taken.
    * [1/2 DONE] Get the frequencies of the amount of photos taken. Plot it.

-----DATES ANALYSIS-----
* [DONE] What's the largest gap time of when photos were taken?
* [DONE] What's the frequency of when photos were taken? Plot it.

"""
import json
import datetime as dt
import statistics
import matplotlib.pyplot as plt


# Getting the JSONs of each rover's manifest data.
# We go down a level in the dictionary for easier data manipulation
def get_json(filename):
    """
    Returns the JSON of a rover's manifest.
    We go down one level in the dictionary for easier data manipulation.
    """
    with open(filename) as f:
        data = json.load(f)
    return data['photo_manifest']


filenames = ['curiosity_manifest.json', 'opportunity_manifest.json', 'spirit_manifest.json']

curiosity_rover = get_json('curiosity_manifest.json')
opportunity_rover = get_json('opportunity_manifest.json')
spirit_rover = get_json('spirit_manifest.json')

rovers = [curiosity_rover, opportunity_rover, spirit_rover]

"""-----BASIC INFO-----"""


def get_info(rover):
    """Prints the information of a rover"""
    print(f"Rover Name: {rover['name']}")
    print(f"Launch Date : {rover['launch_date']}")
    print(f"Landing Date: {rover['landing_date']}")
    print(f"Status: {rover['status']}")
    print(f"Max Sol: {rover['max_sol']}")
    print(f"Max Date: {rover['max_date']}")
    print(f"Total Photos: {rover['total_photos']}")


for bot in rovers:
    get_info(bot)
    print()

"""-----MISSION DATA ANALYSIS-----"""


def get_time_gap(rover):
    """Gets the difference between the landing date and launch date of a rover"""
    time_format = "%Y-%m-%d"
    time_gap = (dt.datetime.strptime(rover['landing_date'], time_format)
                - dt.datetime.strptime(rover['launch_date'], time_format))
    print(f"\tThe {rover['name']} rover took {time_gap.days} Earth days to land on Mars.")


print("How long did it take each rover to get to Mars?")
for bot in rovers:
    get_time_gap(bot)

print("\nIf the status of a rover is complete, how long was their mission?")


def mission_length(rover_list):
    """Prints the length of each rover's mission if complete and prints which rover had the longest mission."""
    longest_mission = 0
    longest_rover = {}

    for rover in rover_list:
        if rover['status'] == 'complete':
            time_format = "%Y-%m-%d"
            difference = (dt.datetime.strptime(rover['max_date'], time_format)
                          - dt.datetime.strptime(rover['landing_date'], time_format))
            difference = difference.days
            years = difference/365.25
            print(f"\n\tRover Name: {rover['name']}")
            print(f"\tLanding Date: {rover['landing_date']}")
            print(f"\tFinal Mission Date: {rover['max_date']}")
            print(f"\tMission Length (days): {difference:,.0f} Earth days")
            print(f"\tMission Length (years): {years:.2f} Earth years")

            dict_item = {'name': rover['name'], 'length': difference}
            if difference > longest_mission:
                longest_mission = difference
                longest_rover.clear()
                longest_rover.update(dict_item)

    print(f"\nThe {longest_rover['name']} rover had the longest mission of {longest_rover['length']} Earth days!")


mission_length(rovers)


"""-----PHOTOS DATA ANALYSIS-----"""


def get_total_photo_amount(rover_list):
    """Prints which rover took the most total photos"""
    max_rover = {}
    max_photo_amount = 0

    for rover in rover_list:
        print(f"\tThe {rover['name']} rover has taken {rover['total_photos']:,.0f} photos.")

        info_to_append = {rover['name']: rover['total_photos']}

        if rover['total_photos'] > max_photo_amount:
            max_photo_amount = rover['total_photos']
            max_rover.clear()
            max_rover.update(info_to_append)

    for k, v in max_rover.items():
        print(f"\nThe {k} rover has taken the most photos, for a total of {v:,.0f} photos!")


print("\nWhich rover has taken the most photos?\n")
get_total_photo_amount(rovers)


def get_max_photo_amount(rover_list):
    """For each rover, prints the sol(s)/earth date(s) that had the most photos taken."""

    for rover in rover_list:
        # Reset our data when going to each rover
        max_photo_amount = 0
        max_rover_dict = {}
        max_rover_list = []

        for photo_data in rover['photos']:
            # For that rover, get the data in the photos key and do our comparison
            info_to_append = photo_data

            photo_amount = photo_data['total_photos']
            if photo_amount == max_photo_amount:  # in the event we get a tie, append it to our list
                max_photo_amount = photo_amount
                max_rover_dict.update(info_to_append)
                max_rover_list.append(max_rover_dict)

            elif photo_amount > max_photo_amount:
                # in the event we get a bigger number and not a tie, clear our data structures and then add our new data
                max_photo_amount = photo_amount
                max_rover_dict.clear()
                max_rover_list.clear()
                max_rover_dict.update(info_to_append)
                max_rover_list.append(max_rover_dict)

        for dict_item in max_rover_list:
            print(f"Rover Name: {rover['name']}")
            print(f"Max Total Photos: {dict_item['total_photos']}")
            print(f"Sol Date: {dict_item['sol']}")
            print(f"Earth Date: {dict_item['earth_date']}\n")


print("\nFor each rover, what sol(s)/earth date(s) had the most photos taken?")
get_max_photo_amount(rovers)


def get_average_photo_amount(rover_list):
    """For each rover, gets the average amount of photos taken every Sol."""
    for rover in rover_list:
        photo_amounts = []
        for photo_data in rover['photos']:
            photo_amounts.append(photo_data['total_photos'])
        average = sum(photo_amounts)/len(photo_amounts)
        print(f"\tThe {rover['name']} rover took an average of {average:.2f} photos a Sol.")


print("\nOn average, how many photos did each rover take a Sol?")
get_average_photo_amount(rovers)


def get_medium_photo_amount(rover_list):
    """Prints the median amount of photos taken for each rover."""
    for rover in rover_list:
        photo_amounts = []
        for photo_data in rover['photos']:
            photo_amounts.append(photo_data['total_photos'])
        sorted_photo_amounts = sorted(photo_amounts)
        median = statistics.median(sorted_photo_amounts)

        print(f"\tThe {rover['name']} rover took an median of {median} photos a Sol.")


print("\nWhat was the median amount of photos taken?")
get_medium_photo_amount(rovers)


def photo_frequencies(rover_list):
    """Returns a frequency of the amount of photos taken."""
    # NOTE: Need to somehow get each rover frequency stored as a separate variable
    all_photo_frequency = {}
    for rover in rover_list:
        photo_frequency = {}
        each_rover_name = rover['name']
        for photo_data in rover['photos']:
            num = photo_data['total_photos']
            a = f"{num}"
            if a in photo_frequency:
                photo_frequency[a] += 1
            else:
                photo_frequency[a] = 1
        all_photo_frequency[each_rover_name] = photo_frequency

    return all_photo_frequency


print(f"\nLet's plot the top 25 photo frequencies!")


def plot_top_25_photo_frequencies(rover_photo_frequencies_dict):
    pixels_width = 1920
    pixels_height = 1080
    dpi = 100
    fig_size = (pixels_width / dpi, pixels_height / dpi)

    for rover_name, photo_frequencies in rover_photo_frequencies_dict.items():
        sorted_frequencies = sorted(photo_frequencies.items(), key=lambda x: x[1], reverse=True)

        top_25_frequencies = dict(sorted_frequencies[:25])

        x_values = list(top_25_frequencies.keys())
        y_values = list(top_25_frequencies.values())

        fig = plt.figure()
        fig.set_size_inches(fig_size)

        plt.style.use('seaborn-v0_8')
        plt.bar(x_values, y_values, color='blue')

        plt.title(f"{rover_name} Rover Top 25 Photo Frequencies", fontsize=24, pad=20, fontweight='bold')
        plt.xlabel("Photos Taken", fontsize=18, labelpad=20, fontweight='bold')
        plt.ylabel("Frequency", fontsize=18, labelpad=20, fontweight='bold')
        plt.xticks(rotation=45, fontsize=16)
        plt.yticks(fontsize=16)

        for x, y in zip(x_values, y_values):
            plt.text(x, y + 2, str(y), ha='center', va='bottom', fontsize=12)

        plt.savefig(f"{rover_name}_Rover_Top_25_Photo_Frequencies.png")
        plt.close(fig)

    print("Top 25 photo frequency charts created!")


frequencies = photo_frequencies(rovers)
plot_top_25_photo_frequencies(frequencies)


def get_longest_time_gap(rover_list):
    for rover in rover_list:
        longest_sol_gap = 0
        for index in range(0, len(rover['photos'])-1):
            current_sol = rover['photos'][index]['sol']
            next_sol = rover['photos'][index+1]['sol']
            sol_difference = next_sol - current_sol

            if sol_difference > longest_sol_gap:
                longest_sol_gap = sol_difference
        print(f"\tThe {rover['name']} rover's longest sol gap time is {longest_sol_gap} sols.")


print("\nWhat's the longest sol between photo sessions for each rover?")
get_longest_time_gap(rovers)


def time_gap_frequency(rover_list):
    all_time_gaps = {}

    for rover in rover_list:
        time_gaps = {}
        each_rover_name = rover['name']
        landing_date = rover['landing_date']  # Updated to use landing_date
        max_date = rover['max_date']  # Updated to use max_date

        for index in range(0, len(rover['photos']) - 1):
            current_sol = rover['photos'][index]['sol']
            next_sol = rover['photos'][index + 1]['sol']
            sol_difference = next_sol - current_sol

            if sol_difference in time_gaps:
                time_gaps[sol_difference] += 1
            else:
                time_gaps[sol_difference] = 1

        # Store time gaps and mission dates
        all_time_gaps[each_rover_name] = {
            "time_gaps": time_gaps,
            "landing_date": landing_date,
            "max_date": max_date
        }

    return all_time_gaps


print(f"\nLet's plot the time gap frequencies!")


def plot_time_gap(rover_time_gaps_dict):
    pixels_width = 1920
    pixels_height = 1080
    dpi = 100
    fig_size = (pixels_width / dpi, pixels_height / dpi)

    for each_rover_name, rover_info in rover_time_gaps_dict.items():
        time_gaps = rover_info['time_gaps']
        landing_date = rover_info['landing_date']  # Updated to use landing_date
        max_date = rover_info['max_date']  # Updated to use max_date

        fig_02 = plt.figure()
        fig_02.set_size_inches(fig_size)

        # Extract the time gaps and frequencies for the current rover
        x_time_gap_amount = list(time_gaps.keys())
        y_frequency = list(time_gaps.values())

        # Plot the bar chart with Seaborn styling
        plt.style.use('seaborn-v0_8')
        plt.bar(x_time_gap_amount, y_frequency, color='blue')

        # Set plot title and labels
        plt.title(f"{each_rover_name} Rover Time Gap Frequencies\nLanding Date: {landing_date} to Max Date: {max_date}",
                  fontsize=24, pad=20, fontweight='bold')
        plt.xlabel("Time Gap (sol)", fontsize=18, labelpad=20, fontweight='bold')
        plt.xticks(x_time_gap_amount, fontsize=16)  # Explicitly set every time gap as a tick
        plt.ylabel("Frequency", fontsize=18, labelpad=20, fontweight='bold')
        plt.yticks(fontsize=16)

        # Annotate the bars with the frequencies
        for x, y in zip(x_time_gap_amount, y_frequency):
            plt.text(x, y + 15, str(y), ha='center', va='bottom', fontsize=16)

        # Save the plot for the current rover, including landing and max dates in the file name
        plt.savefig(f"{each_rover_name}_Rover_Time_Gap_Frequencies_{landing_date}_to_{max_date}.png")
        plt.close(fig_02)
    print("Frequency charts created!")


# Call the plot function with the time gap data
rover_time_gaps = time_gap_frequency(rovers)
plot_time_gap(rover_time_gaps)
