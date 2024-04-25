## Step 1: Add a test workflow

_Let's get started! :rocket:_

**What are workflows_?**: A workflow is a complete unit of automation, defined from start to finish. It includes the definition of what triggers the automation, what environment or other aspects should be taken into account during the automation, and what should happen as a result of the trigger.

![A diagram of a workflow showing the relationship of workflow which includes a job, which includes a step, which references an action.](https://user-images.githubusercontent.com/6351798/88589835-f5ce0900-d016-11ea-8c8a-0e7d7907c713.png)

### Workflow terminology

- **Job**: A job is a section of the workflow. A workflow can have one or more jobs. Each job can have one or more steps. In the example above, the job is called `build` and contains a single step.
- **Step**: A step represents one _effect_ of the automation. Each step is defined within a `steps` section in the workflow. A step can be a shell script, or a reference to an action that's defined elsewhere. Each step performs one or more operations - for example, printing something to the workflow log.
- **Action**: An action (with a lowercase "a") is a piece of automation written in a way that's compatible with workflows. The actions you reference in a workflow can be written by GitHub, by the open source community, or you can write them yourself!

To learn more, see "[Workflow syntax for GitHub Actions](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions)."

First, let's add a workflow to lint (that is, clean, like a lint roller) our Markdown files in this repository.

### :keyboard: Activity: Add a test workflow

1. Open a new browser tab, and navigate to this same repository. Then work through the following steps in that browser tab while you read the instructions in this tab.
1. Go to the **Actions tab**.
1. Click **New workflow** to display a list of workflow templates.
1. In "Simple workflow by GitHub" and click **Configure**.

   If the "Simple workflow by GitHub" template isn't displayed, use the search field to find it.

1. At the top of the workflow editor, change the name of the workflow file from `blank.yml` to `ci.yml`.
1. Update the workflow by deleting the last two steps.
1. Add the following step at the end of your workflow:

   ```yaml
   - name: Run markdown lint
     run: |
       npm install remark-cli remark-preset-lint-consistent
       npx remark . --use remark-preset-lint-consistent --frail
   ```

1. Adjust the indentation of these lines in the workflow file, so that this workflow step is aligned with the first step in the `steps` section of the file. When it is aligned correctly there will be no red squiggly lines indicating errors.

   **Tip**: You can select all four lines of the step and use the <kbd>Tab</kbd> key to adjust the indentation.

1. Click **Commit changes**, choose the "Create a new branch for this commit and start a pull request" option and call the new branch `ci`.
1. Click **Propose changes**.
1. Click **Create pull request**.
1. Wait for a few seconds for the "CI / build (pull_request)" check to be displayed on the pull request. The check will start running and will then fail. This is expected. 🙂
1. Add a comment to the pull request containing the text: "The linter check is failing."
1. Wait about 20 seconds and then refresh the page you're reading now (the README for the repository).

   A separate Actions workflow in the repository (not the workflow you created) will run and will automatically replace the contents of this README file with instructions for the next step.
