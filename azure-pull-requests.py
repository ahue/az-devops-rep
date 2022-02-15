from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.released.git import GitPullRequestSearchCriteria
import yaml
import json
import sys

def get_prs(config_file: str, project: str, outfile: str):
    with open(config_file) as file:
        try:
            cfg = yaml.safe_load(file)  
            print(cfg)
        except yaml.YAMLError as exc:
            print(exc)

    pat = cfg["pat"]
    organization_url = f'https://dev.azure.com/{cfg["org"]}'

    # Create a connection to the org
    credentials = BasicAuthentication('', pat)
    connection = Connection(base_url=organization_url, creds=credentials)

    client = connection.clients.get_git_client()

    sc = GitPullRequestSearchCriteria()
    sc.status = "all"

    
    skip = 0
    top = 100
    prl = []
    while True:

        prs = client.get_pull_requests_by_project(project=project, 
            search_criteria=sc, skip=skip, top=top)
        skip += top
        if not len(prs) > 0: 
            break

        prl += [pr.as_dict() for pr in prs]

    with open(outfile, "w") as outfile:
        outfile.write(json.dumps(prl))
        print(f"exported {len(prl)} PRs")

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 4:
        print("Expecting arguments config_file, project and output file")
        raise ValueError()
    else:
        get_prs(sys.argv[1], sys.argv[2], sys.argv[3])