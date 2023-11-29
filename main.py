# master_file
import argparse
import logging
from command_processing import process_command

logging.basicConfig(filename='result.json', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser()
parser.add_argument('input', nargs='+', metavar='input')
parser.add_argument('-medals', nargs=2, metavar=("country", "year"), action='append')
parser.add_argument('-total', nargs=1, metavar="year", action='append')
parser.add_argument('-overall', nargs='+', metavar="countries", action='append')
parser.add_argument('-interactive', action='store_true')
parser.add_argument('-output', nargs='+', metavar='output_dest')
parser.add_argument('-top', nargs='+', help="Specify amount, sex (optional), and limits (optional)", )

args = parser.parse_args()
args_list = ['main.py']
log_message = {"input": args.input[0] if args.input else None}

if args.input:
    args_list.extend(args.input)

if args.medals:
    log_message["-medals"] = {"country": args.medals[0][0], "year": args.medals[0][1]}
    args_list.extend(['-medals'])
    args_list.extend(args.medals[0])

if args.total:
    log_message["-total"] = args.total[0][0]
    args_list.extend(['-total'])
    args_list.extend(args.total[0])

if args.overall:
    log_message["-overall"] = args.overall[0]
    args_list.extend(['-overall'])
    args_list.extend(args.overall[0])

if args.interactive:
    log_message["-interactive"] = args.interactive
    args_list.extend(['-interactive'])

if args.top:
    log_message["-top"] = {f"N best's: {args.top[0]}, sex: {args.top[1] if len(args.top) > 1 else None}, limits: {args.top[2] if len(args.top) > 2 else None}"}
    args_list.extend(['-top'])
    args_list.extend(args.top)

if args.output:
    log_message["-output"] = args.output[0]
    args_list.extend(['-output'])
    args_list.extend(args.output)

# write logs
logging.info(f"Received commands: {log_message}")

# Process the command
result = process_command(args_list)
print(result)

if __name__ == '__main__':
    print('main.py')
