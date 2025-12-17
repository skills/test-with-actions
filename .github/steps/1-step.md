## Step 1: Continuous Integration

GitHub Actions is a great way to automate several of your recurring tasks, saving you time to work on the more challenging and fun problems!

One of the most common tasks a developer deals with is testing their code. Unfortunately, this is often tedious and things get skipped or simply overlooked. Even more so, we often need to test against many frameworks, operating systems, and other situations, exaggerating the problem.

Let's learn how to automate this ever-growing need for testing our code by using workflows in GitHub Actions.

> [!NOTE]
> If you want to learn more check out these resources:
> - [Understanding GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
> - [Events that trigger workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)
> - [Actions runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing)

### What is Continuous Integration?

[Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) can help you stick to your team’s quality standards by running tests and reporting the results on GitHub. CI tools run builds and tests, triggered by commits. The quality results post back to GitHub in the pull request. The goal is fewer issues in `main` and faster feedback as you work.

### ⌨️ Activity: Start our sample Python application

1. Use the below button to open the **Create Codespace** page in a new tab. Use the default configuration.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirm the **Repository** field is your copy of the exercise, not the original, then click the green **Create Codespace** button.

   - ✅ Your copy: `/{{full_repo_name}}`
   - ❌ Original: `/skills/test-with-actions`

1. Wait a moment for Visual Studio Code to load in your browser.

1. In the left navigation, select the **Explorer** tab to show the project files.

1. Open the `src/calculations.py` and `tests/calculation_tests.py` files.

1. Take a moment to read these files to become familiar.

1. Expand VS Code's built-in terminal panel.

   > 💡 **Tip**: The keyboard shortcut is `CTRL` + `J`.

1. Run the below command to create a virtual environment, then install the required Python libraries and tools to show code coverage.

   ```bash
   python -m venv .venv/calculations
   source .venv/calculations/bin/activate
   pip install -r requirements.txt
   pip install pytest coverage pytest-cov
   ```

1. Run the below command to run all unit tests and view coverage information.

   ```bash
   pytest --cov=src --verbose
   ```

1. Add a comment to let Mona know the results of your coverage report. After reviewing, she will provide the next steps.

   ```md
   @professortocat, I've run my coverage report.
   Seems there is some opportunity to increase the test coverage. 🧐
   What should we do next?
   ```
