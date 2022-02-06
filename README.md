# Azure DevOps PR Exporter

## Description

A python script to download all PRs from a Azure DevOps repository and write them to JSON

## Usage

```bash
python azure-pull-requests.py config.yml ProjectName outfile.json
```

### Example config.yaml

```text
pat: "<your PAT (Personal Access Token)>"
org: "<your-organization>"
```

on PAT see: [Authenticate with personal access tokens - Azure DevOps | Microsoft Docs](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&viewFallbackFrom=vsts&tabs=preview-page)

get the `org` from the DevOps URL: `https://dev.azure.com/<your-organization>/`

## see also

- [Pull Requests - Get Pull Requests By Project
](https://docs.microsoft.com/en-us/rest/api/azure/devops/git/pull-requests/get-pull-requests-by-project?view=azure-devops-rest-6.0)
- [GitHub - microsoft/azure-devops-python-api: Azure DevOps Python API](https://github.com/Microsoft/azure-devops-python-api)