<!--
  <<< Author notes: Header of the course >>>
  Include a 1280×640 image, course title in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Add your open source license, GitHub uses Creative Commons Attribution 4.0 International.
-->

# Continuous Integration

_Create workflows that enable you to use Continuous Integration (CI) for your projects._

<!--
  <<< Author notes: Start of the course >>>
  Include start button, a note about Actions minutes,
  and tell the learner why they should take the course.
  Each step should be wrapped in <details>/<summary>, with an `id` set.
  The start <details> should have `open` as well.
  Do not use quotes on the <details> tag attributes.
-->

<!--step0-->

[Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) can help you stick to your team’s quality standards by running tests and reporting the results on GitHub. CI tools run builds and tests, triggered by commits. The results post back to GitHub in the pull request. The goal is fewer issues in `main` and faster feedback as you work.

- **Who is this for**: Developers, DevOps Engineers, new GitHub users, students, teams.
- **What you'll learn**: What continuous integration is, how to use GitHub Actions for CI, how to create a workflow that runs tests and produces test reports.
- **What you'll build**: We'll use [remark-lint](https://github.com/remarkjs/remark-lint) to check the consistency of Markdown files.
- **Prerequisites**: We assume you've completed [Hello GitHub Actions](https://github.com/skills/hello-github-actions) first.
- **How long**: This course is five steps long and takes less than two hours to complete.

## How to start this course

1. Above these instructions, right-click **Use this template** and open the link in a new tab.
   ![Use this template](https://user-images.githubusercontent.com/1221423/169618716-fb17528d-f332-4fc5-a11a-eaa23562665e.png)
2. In the new tab, follow the prompts to create a new repository.
   - For owner, choose your personal account or an organization to host the repository.
   - We recommend creating a public repository—private repositories will [use Actions minutes](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
   ![Create a new repository](https://user-images.githubusercontent.com/1221423/169618722-406dc508-add4-4074-83f0-c7a7ad87f6f3.png)
3. After your new repository is created, wait about 20 seconds, then refresh the page. Follow the step-by-step instructions in the new repository's README.

<!--endstep0-->

<!--
  <<< Author notes: Step 1 >>>
  Choose 3-5 steps for your course.
  The first step is always the hardest, so pick something easy!
  Link to docs.github.com for further explanations.
  Encourage users to open new tabs for steps!
-->

<details id=1>
<summary><h2>Step 1: Add a test workflow</h2></summary>

_Welcome to "GitHub Actions: Continuous Integration"! :wave:_

**What is _continuous integration_?**: [Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) can help you stick to your team’s quality standards by running tests and reporting the results on GitHub. CI tools run builds and tests, triggered by commits. The results post back to GitHub in the pull request. The goal is fewer issues in `main` and faster feedback as you work.

![An illustration split in two. On the left: illustration of how GitHub Actions terms are encapsulated. At the highest level: workflows and event triggers. Inside of workflows: jobs and definition of the build environment. Inside jobs: steps. Inside steps: a call to an action. On the right: the sequence: workflows, job, step, action.](https://user-images.githubusercontent.com/6351798/88589835-f5ce0900-d016-11ea-8c8a-0e7d7907c713.png)

- **Workflow**: A workflow is a unit of automation from start to finish, including the definition of what triggers the automation, what environment or other aspects should be taken account during the automation, and what should happen as a result of the trigger.
- **Job**: A job is a section of the workflow, and is made up of one or more steps. In this section of our workflow, the template defines the steps that make up the `build` job.
- **Step**: A step represents one _effect_ of the automation. A step could be defined as a GitHub Action, or another unit, like printing something to the console.
- **Action**: An action is a piece of automation written in a way that is compatible with workflows. Actions can be written by GitHub, by the open source community, or you can write them yourself!

To learn more, check out "[Workflow syntax for GitHub Actions](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions)" in the GitHub Docs.

First, let's add a workflow to lint our Markdown files in this repository.

### :keyboard: Activity: Add a test workflow

1. Open a new browser tab, and work on the steps in your second tab while you read the instructions in this tab
1. Go to the **Actions tab**.
1. Click **New workflow**.
1. Search for "Simple workflow" and click **Configure**.
1. Name your workflow `ci.yml`.
1. Update the workflow to remove all steps other than the "checkout" step.
1. Add the following step to your workflow:
   ```yaml
      - name: Run markdown lint
        run: |
          npm install remark-cli remark-preset-lint-consistent
          npx remark . --use remark-preset-lint-consistent --frail
   ```
   > We expect this to create a error build. We'll fix this in the next step.
1. Click **Start commit**, and choose to make a new branch named `ci`.
1. Click **Propose a new file**.
1. Click **Create pull request**.
1. Wait about 20 seconds then refresh this page for the next step

</details>

<!--
  <<< Author notes: Step 2 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

<details id=2>
<summary><h2>Step 2: Fix the test</h2></summary>

_Great job adding the templated workflow! :tada:_

Adding that file to this branch is enough for GitHub Actions to begin running CI on your repository.

When a GitHub Actions workflow is running, you should see some checks in progress, like the screenshot below.

<img alt="checks in progress in a merge box" src=https://user-images.githubusercontent.com/16547949/66080348-ecc5f580-e533-11e9-909e-c213b08790eb.png width=400 />

You can follow along as GitHub Actions runs your job by going to the **Actions** tab or by clicking on "Details" in the merge box below.

When the tests finish, you'll see a red X :x: or a green check mark :heavy_check_mark: in the merge box. At that point, you'll have access to logs for the build job and its associated steps.

<!-- Note here: Learners -- yup, you found the error! Course maintainers -- leave the italics with * instead of _ for the error case. -->

_By looking at the logs, can you identify which tests failed?_ To find it, go to one of the failed builds and scrolling through the log. Look for a section that lists all the unit tests. We're looking for the name of the test with an "x".

<img alt="screenshot of a sample build log with the names of the tests blurred out" src=https://user-images.githubusercontent.com/16547949/65922013-e740a200-e3b1-11e9-8151-faf52c30201e.png width=400 />

If the checks don't appear or if the checks are stuck in progress, there's a few things you can do to try and trigger them:

- Refresh the page, it's possible the workflow ran and the page just hasn't been updated with that change.
- Try making a commit on this branch. Our workflow is triggered with a `push` event, and committing to this branch will result in a new `push`.
- Edit the workflow file on GitHub and ensure there are no red lines indicating a syntax problem.

### :keyboard: Activity: Fix the test

1. Update the code in the `ci` branch to get the test to pass. You need to look something like this:
   ```markdown
   _underscore_
   ```
1. **Commit changes**.
1. Wait about 20 seconds then refresh this page for the next step.

</details>

<!--
  <<< Author notes: Step 3 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

<details id=3>
<summary><h2>Step 3: Upload test reports</h2></summary>

_The workflow has finished running! :sparkles:_

So what do we do when we need the work product of one job in another? We can use the built-in [artifact storage](https://docs.github.com/en/actions/advanced-guides/storing-workflow-data-as-artifacts) to save artifacts created from one job to be used in another job within the same workflow.

To upload artifacts to the artifact storage, we can use an action built by GitHub: [`actions/upload-artifacts`](https://github.com/actions/upload-artifact).

### :keyboard: Activity: Upload test reports

1. Edit your workflow file.
1. Add a step to your `build` job that uses the `upload-artifacts` action.
   ```yaml
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2

         - name: Run markdown lint
           run: |
             npm install remark-cli remark-preset-lint-consistent
             npx remark . --use remark-preset-lint-consistent --frail

         - uses: actions/upload-artifact@main
           with:
             name: remark-lint-report
             path: public/
   ```
1. Commit your change to this branch.
1. Wait about 20 seconds then refresh this page for the next step.

Similar to the upload action to send artifacts to the storage, you can use another action built by GitHub to download these previously uploaded artifacts from the `build` job: [`actions/download-artifact`](https://github.com/actions/download-artifact). To save you time, we'll skip that step for this course.

</details>

<!--
  <<< Author notes: Step 4 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

<details id=4>
<summary><h2>Step 4: Add branch protections</h2></summary>

_Great job uploading test reports! :partying_face:_

Take a look at the merge box, you'll notice you can merge this even though the review process hasn't been met.

Protected branches ensure that collaborators on your repository cannot make irrevocable changes to branches. Enabling protected branches also allows you to enable other optional checks and requirements, like required status checks and required reviews.

### :keyboard: Activity: Add branch protections

1. Go to **Branches** settings. You can navigate to that page manually by clicking on the right-most tab in the top of the repository called **Settings** and then clicking on **Branches**.
1. Click on **Add rule** under "Branch protection rules".
1. Type `main` in **Branch name pattern**.
1. Check **Require pull request reviews before merging**.
1. Check **Require status checks to pass before merging**.
1. Check all build and test jobs that you'd like to see in the newly visible gray box.
1. Click **Create**.
1. _Once you turn on branch protection, Actions can no longer push directly to `main`. You'll need to open the next step on your own._

<!-- Wait about 20 seconds then refresh this page for the next step. -->

</details>

<!--
  <<< Author notes: Step 5 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

<details id=5>
<summary><h2>Step 5: Merge your pull request</h2></summary>

_Almost there! :heart:_

You can now [merge](https://docs.github.com/en/get-started/quickstart/github-glossary#merge) your pull request!

### :keyboard: Activity: Merge your pull request

1. Click **Merge pull request**.
1. Delete the branch `ci` (optional).
1. _Once you turn on branch protection, Actions can no longer push directly to `main`. You'll need to open the "finish" on your own._

<!-- Wait about 20 seconds then refresh this page for the next step. -->

</details>

<!--
  <<< Author notes: Finish >>>
  Review what we learned, ask for feedback, provide next steps.
-->

<details id=X>
<summary><h2>Finish</h2></summary>

_Congratulations friend, you've completed this course!_

<img src=https://octodex.github.com/images/Fintechtocat.png alt=celebrate width=300 align=right>

Here's a recap of all the tasks you've accomplished in your repository:

- We created an Actions workflow to lint our Markdown files.
- You caught an issue in a file and fixed the issue before it could make it to `main`.
- You learned how to use build artifacts for test reports.
- You enabled branch protections to require the workflow to pass before merging.

### What's next?

- Get more ideas of what you can do with [awesome actions](https://github.com/sdras/awesome-actions).
- We'd love to hear what you thought of this course [in our discussion board](https://github.com/skills/.github/discussions).
- [Take another GitHub Skills course](https://github.com/skills).
- [Read the GitHub Getting Started docs](https://docs.github.com/en/get-started).
- To find projects to contribute to, check out [GitHub Explore](https://github.com/explore).

</details>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, GitHub status page, code of conduct, license link.
-->

---

Get help: [Post in our discussion board](https://github.com/skills/.github/discussions) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2022 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [CC-BY-4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode)
