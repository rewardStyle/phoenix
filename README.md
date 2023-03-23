# phoenix
A high level description of this repo.

Include the animal logo created by our very own Michael Sugimura. The art can be found in [this Google Drive folder](https://drive.google.com/drive/folders/1_Gsten6Ay4gBfj-w9GFso22FDC4NyXWc). Share the image in the drive folder, under `General access` change to `Anyone with the link` as `Viewer`, copy the link, it will look something like:
```
https://drive.google.com/file/d/1ib9y-7cNfMzeIgvtYBmD6EHfh5SpFB9Q/view?usp=sharing
```
Copy the link ID between the `.../d/` and `/view?...` of the shared URL. In the above example the ID is `1ib9y-7cNfMzeIgvtYBmD6EHfh5SpFB9Q`. Put the id in the `insert_id` portion of the following URL:
```
![](https://drive.google.com/uc?export=view&id=insert_id)
```
Remove the back ticks from the line above and it will render as an image! Yay!
## How to set up this library for installation in Databricks:
In order to upload the library wheel to Databricks, two GitHub secrets need to be configured: `DATABRICKS_HOST` and `DATABRICKS_TOKEN`. 
1. Follow the [GitHub instructions](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) for creating a secret.
2. Name the secret `DATABRICKS_HOST`.
3. The value for this secret is the Databricks instance name, this is the first part of the Databricks URL. More information can be found [here](https://docs.databricks.com/workspace/workspace-details.html).
4. Save that secret, then repeat the steps to create another GitHub secret.
5. Name the secret `DATABRICKS_TOKEN`.
6. Create a personal access token on Databricks following [these instructions](https://docs.databricks.com/dev-tools/auth.html#personal-access-tokens-for-users). Create a token with no lifetime by leaving the `Lifetime (days)` box empty.
7. Go back to GitHub, add the value for the secret - the token copied in step 6.
8. Uncomment the last section in `.github/workflows/main_branch_ci.yaml`
Now the library wheel will be uploaded to Databricks FileStore and can be installed using the instructions below. 

Note: completing this section is optional, and if not followed, the `Installation` section of this README will need to be updated or removed. This section should also be removed from this README. 

## What is this repo?
This is a thorough description of this repo including what it's used for and why. There will also be any links to resources such as jobs or APIs associated with the repo. If this is an API, include the WIP docs, the PRD docs, an exampled cURL request, and a Postman example.

## How does this repo relate to the DS code base at LTK?
This section explains how this repo is connected to any other repos at LTK, if applicable.

## Installation
The wheel will be uploaded to the Databricks FileStore on merges to the main branch. 
Then you can install the library from within Databricks with:
```bash
pip install /dbfs/FileStore/internal_library_wheels/phoenix/ltk_phoenix-latest-py3-none-any.whl
```
Note: this will only work within Databricks for installation.

## Development

### Local development
Explain how to add to development of this library, specific Databricks resources? Docker?

### Start JupyterLab
To run JupyterLab, start the container and execute the following:
```bash
jupyter lab --ip 0.0.0.0 --no-browser --allow-root
```

Connect to JupyterLab here for local development: [http://localhost:8888/lab](http://localhost:8888/lab)<br>
And here for development on an EC2 instance: `PRIVATE_IP:8888/lab/TOKEN`

### Unit Tests
Linting and unit tests in this repo can be run using:

```bash
flake8 phoenix tests
pytest -v
```
