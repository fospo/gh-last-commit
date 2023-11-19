# Last GitHub Commit
This Python script retrieves the latest commit for each repository of a specified GitHub organization.

## Usage
1. Set your GH_TOKEN environment variable with your GitHub personal access token.

```bash
export GH_TOKEN=your_github_token
```

2. Run the script with the organization name and the file name as arguments. The file should contain the names of the repositories, one per line.

```bash
python last_commit.py organization_name file_name
```

The script will create a `results.csv` file with the repository names, the date of the last commit, and the author of the last commit. If a repository has no commits, "No commits found" will be printed.

## Chaining
It possible to chain this script with a discovery script that gets repos from a org.
For example see the following:
    
```bash
python3 gh_pyxplorer/crawler.py -i org fospo -o print -f name > tmp.txt && \
python3 last_commit.py fospo tmp.txt && \ 
rm tmp.txt
```

in this way, we will explore the `fospo` org with the relevant script, print the results to a file, and then use that file to get the last commit for each repo. At last, we remove the tmp file.
A tmp file is needed since this script needs a file in input and cannot parse directly the output of the crawler.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.