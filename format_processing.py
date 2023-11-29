import re


def format_medals_data(medals_data_array_for_print, medals_dict, args):
    formatted_data = f"Medals Data for {args[0]} National Olympic Committee for the {args[1]} year:\n\n"
    for dict in medals_data_array_for_print:
        for key, value in dict.items():
            formatted_data += f"{key}: {value}\n"
        formatted_data += "-" * 50 + '\n'
    formatted_data += "Summary:\n"
    for key, value in medals_dict.items():
        formatted_data += f"    {key}: {value}\n"
    return formatted_data


def format_total_data(data_array, args):
    # data_array = [('Italy', 'Bronze', "Rowing Men's Coxless Pairs"), ('Azerbaijan', 'Bronze', "Taekwondo Women's Flyweight"), ('France', 'Silver', "Handball Men's Handball"), ...]
    data_dict = {}
    for triple_set in data_array:
        country, medal, event = triple_set
        if not country in data_dict:
            data_dict[country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
        data_dict[country][medal] += 1
    # data_dict = {'Italy': {'Gold': 8, 'Silver': 11, 'Bronze': 8}, 'Azerbaijan': {'Gold': 1, 'Silver': 7, 'Bronze': 10}, ...}
    formatted_data = f"Total Data for the {args[0]} year:\n\n"
    for country, medals_dict in data_dict.items():
        formatted_data += f"{country}:\n"
        for class_of_medal, quantity in medals_dict.items():
            formatted_data += f"    {class_of_medal} : {quantity}\n"
    formatted_data += "-" * 50 + '\n'
    return formatted_data


def format_overall_data(data_array, args):
    # data_array = [('Canada', '1984', 'Bronze', "Swimming Women's 4 x 100 metres Medley Relay"), ('Japan', '1994', 'Gold', "Nordic Combined Men's Team"), ...]
    data_dict = {}
    for quadro_set in data_array:
        country, year, medal, event = quadro_set
        if not country in data_dict:
            data_dict[country] = {}
        if not year in data_dict[country]:
            data_dict[country][year] = {'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Sum': 0}
        data_dict[country][year][medal] += 1
        data_dict[country][year]['Sum'] += 1

    # data_dict = {'Canada': {'1984': {'Gold': 12, 'Silver': 19, 'Bronze': 17, 'Sum': 48}, ...} ... }
    record_data = []
    for country, result_for_each_year_dict in data_dict.items():
        max = ['country', 'year', 'medal_class_dict', 0]
        for year, medal_class_dict in result_for_each_year_dict.items():
            if medal_class_dict['Sum'] > max[-1]:
                max = [country, year, medal_class_dict, medal_class_dict['Sum']]
        record_data.append(max)

    # record_data = [['Canada', '1984', {'Gold': 12, 'Silver': 19, 'Bronze': 17, 'Sum': 48}, 48], ...]
    if args[-2] == '-output' and re.search(r'\.txt$', args[-1]):
        countries = args[:-2]
    else:
        countries = args
    formatted_line = f"Overall Data for countries {countries}:\n\n"
    for quadro_set in record_data:
        country, year, medals_dict, sum = quadro_set
        formatted_line += f"For {country} the most successful season was in {year}:\n"
        for key, value in medals_dict.items():
            formatted_line += f"    {key} : {value}\n"
        formatted_line += '-' * 50 + '\n'

    return formatted_line


def format_interactive_data(data_array, country):
    # data_array = [('2008', 'Gold', "Shooting Men's Small-Bore Rifle, Prone, 50 metres"), ('2012', 'Silver', "Wrestling Men's Heavyweight, Freestyle"), ...]
    data_dict = {}
    for triple_set in data_array:
        year, medal, event = triple_set
        if year not in data_dict:
            data_dict[year] = {'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Sum': 0}
        if medal == None:
            pass
        else:
            data_dict[year][medal] += 1
            data_dict[year]['Sum'] += 1
    # data_dict = {'2008': {'Gold': 7, 'Silver': 5, 'Bronze': 15, 'Sum': 27}, '2012': {'Gold': 6, 'Silver': 5, 'Bronze': 9, 'Sum': 20}, ...}
    min = ['year', 'medal_class_dict', 1000]  # ['2002', {'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Sum': 0}, 0]
    max = ['year', 'medal_class_dict', 0]  # ['2008', {'Gold': 7, 'Silver': 5, 'Bronze': 15, 'Sum': 27}, 27]
    min_year = [2024, 'medal_class_dict']  # ['1994', {'Gold': 1, 'Silver': 0, 'Bronze': 1, 'Sum': 2}]
    average = {'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Sum': 0}  # {'Gold': 3.08, 'Silver': 2.75, 'Bronze': 5.17, 'Sum': 11.0}
    counter_of_years = 0
    for year, medal_class_dict in data_dict.items():
        if medal_class_dict['Sum'] < min[-1]:
            min = [year, medal_class_dict, medal_class_dict['Sum']]
        if medal_class_dict['Sum'] > max[-1]:
            max = [year, medal_class_dict, medal_class_dict['Sum']]
        if int(year) < int(min_year[0]):
            min_year = [year, medal_class_dict]
        for key, value in medal_class_dict.items():
            average[key] += value
        counter_of_years += 1
    for key, value in average.items():
        average[key] /= counter_of_years
        average[key] = round(average[key], 2)
    formatted_line = f"Interactive Data for {country}:\n\n"
    formatted_line += f"The least successful year for {country} was {min[0]}:\n"
    for key, value in min[1].items():
        formatted_line += f"    {key} : {value}\n"
    formatted_line += f"The most successful year for {country} was {max[0]}:\n"
    for key, value in max[1].items():
        formatted_line += f"    {key} : {value}\n"
    formatted_line += f"The first performance for {country} was {min_year[0]}:\n"
    for key, value in min_year[1].items():
        formatted_line += f"    {key} : {value}\n"
    formatted_line += f"The average performance for {country} was:\n"
    for key, value in average.items():
        formatted_line += f"    {key} : {value}\n"
    return (formatted_line)


def format_top_data(data_array, args):
    data_dict = {}
    for line in data_array:
        name, year, medal, event = line
        if name not in data_dict:
            data_dict[name] = {'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Sum': 0}
        data_dict[name][medal] += 1
        data_dict[name]['Sum'] += 1
    data_dict = sorted(data_dict.items(), key=lambda x: x[1]['Sum'], reverse=True)
    counter = 0
    if len(args) > 1 and args[-2] == '-output' and re.search(r'\.txt$', args[-1]):
        args_for_printing = args[:-2]
    else:
        args_for_printing = args
    if len(args_for_printing) == 1:
        formatted_line = f"Top Data of {args[0]} best athletes:\n\n"
    else:
        formatted_line = f"Top Data of {args[0]} best {'female' if args[1] == 'F' else 'male'} athletes in age range {args[2]} limit:\n\n"
    for name, medals_dict in data_dict:
        if counter < int(args[0]):
            formatted_line += f"{name}:\n"
            for key, value in medals_dict.items():
                formatted_line += f"    {key} : {value}\n"
            formatted_line += '-' * 50 + '\n'
            counter += 1
        else:
            break
    return formatted_line


def output_function(formatted_data, args):
    with open(args[-1], 'w') as result_file:
        result_file.write(formatted_data)
    return "Data is written in the given file"
