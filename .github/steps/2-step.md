## Step 2: Workflow files

The best way to add automation to your project's repository is with a GitHub Actions Workflow. Let's look at the anatomy of a workflow then create 2 of them.

### What are the parts of workflow?

![An illustration with a left half and a right half. On the left: illustration of how GitHub Actions terms are encapsulated. At the highest level: workflows and event triggers. Inside workflows: jobs and definition of the build environment. Inside jobs: steps. Inside steps: a call to an action. On the right: the evaluated sequence: workflow, job, step, action.](https://user-images.githubusercontent.com/6351798/88589835-f5ce0900-d016-11ea-8c8a-0e7d7907c713.png)

- **Workflow**: A unit of automation from start to finish. It starts when the trigger (`on`) matches an activity in the repository and runs 1 or more jobs.

- **Jobs**: The workflow's jobs each run in their own isolated environments and can be configured differently. They run in parallel unless configured otherwise or dependencies are set.

- **Steps**: The steps area is a series of related actions that achieve a job's goal. A step can be a pre-made _Action_ from the Actions Marketplace, a private workflow, or even a custom script.

- **Action**: Each step is an _Action_, a piece of automation written in a way that is compatible with workflows. Actions can be written by GitHub, by the open source community, or specific to the project.

In the above `Example Workflow` file, it will start when any commits are pushed to the repository on any branch. It will run 1 job with the name `build`. That job's first step uses a pre-made _Action_ from the `actions` organization named `checkout` that clones the code from the repository into the job's environment.

You can explore all of the configuration options in the [GitHub Actions Docs](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions).

### ⌨️ Activity: Add a workflow to run tests

1. Open a web browser tab and navigate to this exercise repository. The Codespace is not not needed right now.

1. In the top navigation, select the **Actions** tab.

1. In the left navigation, above list of workflows, click the **New workflow** button.

1. Enter `python` into the search box and click the **Enter** button.

   <img width="300" alt="search box with 'python' value" src="https://github.com/user-attachments/assets/34f2795c-85e8-4dc8-b03b-eac73e70e309" />

1. Find the **Python package** workflow and click the **Configure** button to open a file editor with a pre-made workflow.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/4a2ff616-aedd-41b5-a24c-82014e98bbee" />

1. Above the file editor, update the file name.

   ```txt
   python-tests.yml
   ```

1. Around line 6, simplify the `on` trigger to only use pull requests.

   ```yml
   on:
     pull_request:
       branches: ["main"]
   ```

1. Around line 17, update the matrix strategy to use Python versions important to our project.

   ```yml
   python-version: ["3.11", "3.12", "3.13"]
   ```

1. Around line 28, remove the unnecessary `pytest` dependency.

   ```diff
   python -m pip install flake8
   ```

1. Around line 36, change the test framework and command.

   ```yml
   - name: Run tests
      run: |
        python -m unittest discover -s tests -p "*_test.py"
   ```

1. Above the editor, on the right, click the **Commit changes...**.

### ⌨️ Activity: Add a workflow to show test coverage

1. Switch to the VS Code Codespace.

1. In the left navigation, select the **Explorer** tab to show the project files.

1. Expand the `.github/workflows/` folder.

1. Add a new file with the following name and open it.

   ```txt
   python-coverage.yml
   ```

1. Enter the name and set it to trigger on pull requests targeting the `main` branch.

   ```yml
   name: Python Coverage

   on:
     pull_request:
       branches:
         - main
   ```

1. Add the `python-coverage` job and a first step that gets the repository content.

   ```yml
   jobs:
   python-coverage:
     runs-on: ubuntu-latest

     steps:
       - name: Checkout code
         uses: actions/checkout@v4
   ```

1. Add steps to install Python and required packages.

   ```yml
   - name: Set up Python
     uses: actions/setup-python@v4
     with:
       python-version: 3.13

   - name: Install dependencies
     run: |
       pip install -r requirements.txt
       pip install coverage==7.9
       pip freeze
   ```

1. Add steps to run the coverage report and save for later use.

   ```yml
   - name: Run tests with coverage
     id: coverage
     run: |
       coverage run -m unittest discover -s tests -p "*_test.py"
       echo "coverage_report<<EOF" >> $GITHUB_OUTPUT
       coverage report >> $GITHUB_OUTPUT
       echo "EOF" >> $GITHUB_OUTPUT
   ```

1. Add steps to generate other formats.

   ```yml
   - name: Generate coverage reports
     run: |
       coverage xml
       coverage html

   - name: Upload coverage reports
     uses: actions/upload-artifact@v4
     with:
       name: coverage-reports
       path: |
         coverage.xml
         htmlcov/
   ```

1. Add a final step to share the coverage report as a comment on the pull requests.

   ```yml
   - name: Post coverage comment
     uses: actions/github-script@v7
     with:
       script: |
         const artifactsUrl = `https://github.com/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId}`;

         const commentBody = `### Test Coverage Report
         <details>
         <summary>Coverage Details</summary>

         \`\`\`
         ${steps.coverage.outputs.coverage_report}
         \`\`\`

         </details>

         [📊 Detailed HTML Coverage Report](${artifactsUrl})
         `;

         github.rest.issues.createComment({
           owner: context.repo.owner,
           repo: context.repo.repo,
           issue_number: context.issue.number,
           body: commentBody
         });
   ```

1. Commit and push the coverage workflow.

> [!TIP]
> We used custom steps here to show the flexibility of Actions. There are several AWESOME pre-made options from the community on the free [Actions Marketplace](https://github.com/marketplace?type=actions). Consider trying one of them out before you build your own!

⌨️ Activity: Merge workflows

1. Create a new pull request. Use the following details.

   - **target:** `main`
   - **base:** `add-testing-workflows`
   - **title:** `feat: Add testing and coverage workflows`
   - **description:** (blank)

1. Ensure

1. With the new workflow pushed to GitHub, Mona will review your work and post the next steps.

<!-- ### (optional) ⌨️ Activity: Filter triggers by file type

Our current workflow will trigger on any pull request targeting `main`, even if it doesn't change the code. That is unnecessary. -->

<!-- ### (optional) Activity: Ask Copilot to enable package caching

If you have Copilot, give the following prompt a try.
It will modify your workflow add caching between the workflow runs, making it much faster. Nice!

```prompt
Hey Copilot, these workflows take a while to run. Can you enable enable caching for installing the python version and required packages? The goal is to avoid constantly re-downloading the resources, which should make things faster.
```

<details>
<summary>Example workflow</summary>

```yml
sample
```

</details> -->
