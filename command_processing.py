from file_processing import process_file
from validation_function import is_valid
from format_processing import format_medals_data, format_total_data, format_overall_data, format_interactive_data, format_top_data, output_function
import re


def process_command(args_list):
    # args_list[0] = 'main.py'
    filename = args_list[1]
    command = args_list[2]
    command_arguments = args_list[3:]
    if command in command_dict:
        return command_dict[command](filename, command_arguments)
    else:
        return "Unknown command"


def medals(filename, args):
    if is_valid(filename, 'NOC', args[0]) and is_valid(filename, 'Year', args[1]):
        medals_data_array = []
        medals_data_array_for_print = []
        counter = 0
        limit = 10
        for line in process_file(filename):
            if line['NOC'] == args[0] and int(line['Year']) == int(args[1]) and line['Medal'] != "NA":
                if counter < limit:
                    medals_data_array_for_print.append(line)
                if not (line['Medal'], line['Event']) in medals_data_array:
                    medals_data_array.append((line['Medal'], line['Event']))
                counter += 1
        medals_dict = {"Gold": 0, "Silver": 0, "Bronze": 0}
        for pair in medals_data_array:
            medals_dict[pair[0]] += 1
        if args[-2] == '-output':
            return output_function(format_medals_data(medals_data_array_for_print, medals_dict, args), args)
        else:
            return format_medals_data(medals_data_array_for_print, medals_dict, args)
    else:
        return "Invalid data entered by user [NOC or year]"


def total(filename, args):
    if is_valid(filename, 'Year', args[0]):
        total_data = []
        for line in process_file(filename):
            if int(line['Year']) == int(args[0]) and line['Medal'] != "NA" and not (line['Team'], line['Medal'], line['Event']) in total_data:
                total_data.append((line['Team'], line['Medal'], line['Event']))
        if len(args) > 2 and args[-2] == '-output':
            return output_function(format_total_data(total_data, args), args)
        else:
            return format_total_data(total_data, args)
    else:
        return "Invalid year entered by user for '-total' command"


def overall(filename, args):
    # args = ['Ukraine', 'Canada', 'Japan', ..., '-output', 'result.txt']
    for country in args:
        if country == '-output' or re.search(r'\.txt$', country):
            continue
        if not is_valid(filename, 'Team', country):
            return f"Invalid country name '{country}' entered by user for '-overall' command"
    overall_data = []
    for line in process_file(filename):
        if line['Team'] in args and line['Medal'] != "NA" and not (line['Team'], line['Year'], line['Medal'], line['Event']) in overall_data:
            overall_data.append((line['Team'], line['Year'], line['Medal'], line['Event']))
    if len(args) > 3 and args[-2] == '-output':
        return output_function(format_overall_data(overall_data, args), args)
    else:
        return format_overall_data(overall_data, args)


def interactive(filename, args):
    # args =  [] or ['-output', 'result.txt']
    input_data = []
    input_data.append(input("Enter country name: "))
    while input_data[-1:] != ['exit']:
        country = input_data.pop()
        if is_valid(filename, 'Team', country):
            interactive_data = []
            for line in process_file(filename):
                if line['Team'] == country and not (line['Year'], line['Medal'], line['Event']) in interactive_data:
                    if line['Medal'] != "NA":
                        interactive_data.append((line['Year'], line['Medal'], line['Event']))
                    else:
                        interactive_data.append((line['Year'], None, line['Event']))
            if len(args) > 1 and args[-2] == '-output':
                print(output_function(format_interactive_data(interactive_data, country), args))
            else:
                print(format_interactive_data(interactive_data, country))
        else:
            print(f"Invalid country name '{country}' entered by user for '-interactive' command")
        input_data.append(input("Enter country name: "))
    return "Interactive mode is finished"


def top(filename, args):
    if args[0].isnumeric():
        top_data = []
        if len(args) > 2 and args[1] in ['M', 'F'] and '-' in args[2]:
            for line in process_file(filename):
                if line['Sex'] == args[1] and line['Age'] != 'NA' and (int(line['Age']) >= int(args[2].split('-')[0]) and int(line['Age']) <= int(args[2].split('-')[1])) and line['Medal'] != 'NA' and (
                        line['Name'], line['Year'], line['Medal'], line['Event']) not in top_data:
                    top_data.append((line['Name'], line['Year'], line['Medal'], line['Event']))
        else:
            for line in process_file(filename):
                if line['Medal'] != 'NA' and (line['Name'], line['Year'], line['Medal'], line['Event']) not in top_data:
                    top_data.append((line['Name'], line['Year'], line['Medal'], line['Event']))
        if len(args) > 2 and args[-2] == '-output':
            return output_function(format_top_data(top_data, args), args)
        else:
            return format_top_data(top_data, args)
    else:
        return "Invalid number entered by user for '-top' command"


command_dict = {"-medals": medals, "-total": total, "-overall": overall, "-interactive": interactive, "-top": top}
