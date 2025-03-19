import argparse
from check_50 import check as check50
from check_60 import check as check60
from check_80 import check as check80
import os

mongodb_internal_application = ["MongoDB Automation Agent", "OplogFetcher"]

def main():
    parser = argparse.ArgumentParser(description="Script to check compatibility using logs.")
    parser.add_argument(
        '--log-path',
        type=str,
        required=True,
        help="Path to the directory where the logs are located."
    )
    args = parser.parse_args()
    log_path = args.log_path

    query_lines = []
    for root, _, files in os.walk(log_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for line in f:
                    # exclude lines that are comming from mongodb applications, like MongoDB Automation Agent
                    if not any(app in line for app in mongodb_internal_application):
                        if "Slow query" in line:
                            query_lines.append(line)

    print("Checking version 5 compatibility")
    results_50 = check50(query_lines)
    if len(results_50["errors"]) > 0:
        for error in results_50["errors"]:
            print(f"   { error }")

    print("Checking version 6 compatibility")
    results_60 = check60(query_lines)
    if len(results_60["errors"]) > 0:
        for error in results_60["errors"]:
            print(f"   { error }")

    print("Checking version 8 compatibility")
    results_80 = check80(query_lines)
    if len(results_80["errors"]) > 0:
        for error in results_80["errors"]:
            print(f"   { error }")

if __name__ == "__main__":
    main()