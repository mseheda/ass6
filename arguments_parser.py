# from argparser I will get list of arguments
# all possible examples below
# args_list = ["main.py", "data_source.tsv", "-medals", "RUS", "2014"]
# args_list = ["main.py", "data_source.tsv", "-medals", "UKR", "2014", "-output", "result.txt"]  # last two args are optional

# args_list = ["main.py", "data_source.tsv", "-total", "2014"]
# args_list = ["main.py", "data_source.tsv", "-total", "2014", "-output", "result.txt"]  # last two args are optional

# args_list = ["main.py", "data_source.tsv", "-overall", "Ukraine", "Canada", "Japan"]  # quantity of countries is >=1 and <infinity
# args_list = ["main.py", "data_source.tsv", "-overall", "Ukraine", "Canada", "Japan", "-output", "result.txt"]  # last two args are optional

# args_list = ["main.py", "data_source.tsv", "-interactive"]  # after this command user will input countryname one by one
# args_list = ["main.py", "data_source.tsv", "-interactive", "-output", "result.txt"]  # last two args are optional

# args_list = ["main.py", "data_source.tsv", "-top", "10"]
# args_list = ["main.py", "data_source.tsv", "-top", "15", "-output", "result.txt"]

args_list = ["main.py", "data_source.tsv", "-top", "10", "F", "18-35"]
# args_list = ["main.py", "data_source.tsv", "-top", "10", "M", "18-35", "-output", "result.txt"]
