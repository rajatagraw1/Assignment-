import re
from collections import Counter

log_file_path = 'sample_log.log'

def parse_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.readlines()
    return log_data

def count_404_errors(log_data):
    return sum(1 for line in log_data if ' 404 ' in line)

def most_requested_pages(log_data):
    pages = []
    for line in log_data:
        match = re.search(r'\"(?:GET|POST) (.*?) HTTP/', line)
        if match:
            pages.append(match.group(1))
    return Counter(pages).most_common(10)

def ip_with_most_requests(log_data):
    ips = [line.split()[0] for line in log_data]
    return Counter(ips).most_common(10)

def generate_report(log_file_path):
    log_data = parse_log(log_file_path)

    print("Number of 404 errors: " + str(count_404_errors(log_data)))
    # print(count_404_errors(log_data))
    print("Most requested pages:")
    for page, count in most_requested_pages(log_data):
        print(str(page)+": "+str(count))
    print("IP addresses with the most requests:")
    for ip, count in ip_with_most_requests(log_data):
        print(str(ip)+": "+str(count))

if __name__ == "__main__":
    generate_report(log_file_path)