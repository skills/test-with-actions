## Step 4: Enforce workflows

You may have noticed that the merge button was still active before our tests finished.
Even worse, the tests failed and there was nothing to prevent merging the broken code anyway! 😱

Let's fix this to avoid anyone (accidentally) bypassing verification.

### ⌨️ Activity: Add branch protections

1. In the top navigation, select the **Settings** tab.

1. In the left navigation, select **Rules** and choose **Rulesets**.

1. Click the **New ruleset** and select **New branch ruleset**. Use the following settings:

   - **Ruleset Name:** `Protect main`
   - **Enforcement status:** `Active`
   - **Target branches:**
     - **Include default branch**
     - **Include by pattern:** `main`
   - **Require status checks to pass**: ☑️ Checked
     - `python-coverage`
     - `python-tests`

   <img width="300" alt="target branch settings" src="https://github.com/user-attachments/assets/9b68fd13-8348-401e-b1a3-6fd2f8744759" />

   <img width="300" alt="required status checks" src="https://github.com/user-attachments/assets/a5fe16aa-9d3a-4ab1-9406-a288b6c7b2b5" />

1. Click **Create**.

1. Navigate back to the pull request and refresh the page.

1. The **Merge** is now disabled! Nice! 🥰

   <img width="500" alt="failed tests and disabled merge button" src="https://github.com/user-attachments/assets/6dd46999-f98f-42fa-af65-b553c4e59c8e" />

### Activity: Fix the broken test and merge

1. In the pull request, find the area near the merge button with the list of the workflows.

1. Click on the title of the failed workflow.

1. Scroll through the logs to investigate the root cause of the issue.

   - You will learn that one of the tests checks for minimum Python version.
   - This explains why only the jobs using `3.8` and `3.9` failed.
   - We know these are good from our own testing, so let's update the test.

1. Switch to the VS Code Codespace.

1. Open the `tests/supported_versions_test.py` file.

1. At around line 17, update the line to change the minimum required minor version.

```py
self.assertGreaterEqual(minor, 8, "Python minor version must be >= 8")
```

1. Commit and push your changes. After a moment, the testing workflows should run again.

1. Wait a moment for the tests to complete. If they all pass, the merge button should activate!

1. Click the **Merge** button. Congrats, you are all done!

   <img width="500" alt="image" src="https://github.com/user-attachments/assets/1c75d9bc-62e9-429f-ad4d-45ea8b7d1a73" />
