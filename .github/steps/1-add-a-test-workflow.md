<!--
  <<< Author notes: Step 1 >>>
  Choose 3-5 steps for your course.
  The first step is always the hardest, so pick something easy!
  Link to docs.github.com for further explanations.
  Encourage users to open new tabs for steps!
-->

## Step 1: Add a test workflow

_Welcome to "GitHub Actions: Continuous Integration"! :wave:_

**What is _continuous integration_?**: [Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) can help you stick to your team’s quality standards by running tests and reporting the results on GitHub. CI tools run builds and tests, triggered by commits. The quality results post back to GitHub in the pull request. The goal is fewer issues in `main` and faster feedback as you work.

![An illustration with a left half and a right half. On the left: illustration of how GitHub Actions terms are encapsulated. At the highest level: workflows and event triggers. Inside workflows: jobs and definition of the build environment. Inside jobs: steps. Inside steps: a call to an action. On the right: the evaluated sequence: workflow, job, step, action.](https://user-images.githubusercontent.com/6351798/88589835-f5ce0900-d016-11ea-8c8a-0e7d7907c713.png)

- **Workflow**: A workflow is a unit of automation from its start to finish, including the definition of what triggers the automation, what environment or other aspects should be taken into account during the automation, and what should happen as a result of the trigger.
- **Job**: A job is a section of the workflow, and is made up of one or more steps. In this section of our workflow, the template defines the steps that make up the `build` job.
- **Step**: A step represents one _effect_ of the automation. A step could be defined as a GitHub Action, or another unit, like printing something to the console.
- **Action**: An action is a piece of automation written in a way that is compatible with workflows. Actions can be written by GitHub, by the open source community, and you can write them yourself!

To learn more, check out [Workflow syntax for GitHub Actions](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions) in the GitHub Docs.

First, let's add a workflow to *lint* (clean, like a lint roller) our Markdown files in this repository. This workflow has a deliberate error in it ("npx" should be "npm"), which we'll debug in the next unit.

### :keyboard: Activity: Add a test workflow

1. Open a new browser tab, and work through the following steps in that tab while you read the instructions in this tab.
1. Go to the **Actions tab**.
1. Select **New workflow**.
1. Search for "Simple workflow" and select **Configure**.
1. Name your workflow `ci.yml`.
1. Update the workflow by deleting the last two steps.
1. Add the following step at the end of your workflow:
   ```yml
   - name: Run markdown lint
     run: |
       npm install remark-cli remark-preset-lint-consistent
       npx remark . --use remark-preset-lint-consistent --frail
   ```
   > Even after the code is indented properly in `ci.yml`, you will see a build error in GitHub Actions. We'll fix this in the next step.
1. Select **Commit changes...**, and choose to make a new branch named `ci`.
1. Select **Propose changes**.
1. Select **Create pull request**.
1. Wait about 20 seconds then refresh this page (the one you're following instructions from). [GitHub Actions](https://docs.github.com/actions) will automatically update to the next step.
