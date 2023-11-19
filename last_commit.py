import sys
import csv
import os
from github import Github
import concurrent.futures

# Max number of threads to use
MAX_WORKERS = 10


def get_last_commit(repo):
    commits = repo.get_commits()
    if not commits:
        return [repo.name, "No commits found"]
    last_commit = commits[0]
    last_commit_author = last_commit.commit.author.name
    last_commit_date = last_commit.commit.author.date
    last_commit_date_formatted = last_commit_date.strftime("%Y-%m-%d %H:%M:%S")
    return [repo.name, last_commit_date_formatted, last_commit_author]


def write_to_csv(results):
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(results)


def main(org_name, file_name):
    access_token = os.getenv("GH_TOKEN")
    g = Github(access_token)
    org = g.get_organization(org_name)

    with open(file_name, "r") as f:
        repo_list = [org.get_repo(line.strip()) for line in f.readlines()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map(get_last_commit, repo_list)

    write_to_csv(results)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 last_activity.py org_name file_name")
    main(sys.argv[1], sys.argv[2])
