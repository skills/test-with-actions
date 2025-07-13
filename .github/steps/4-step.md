## Step 4: Enforce workflows

You may have noticed that the merge button was still active before our tests finished.
Even worse, the some tests failed and there was nothing to prevent merging the broken code anyway! 😱

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

   > ❕ **Important:** To keep the lesson simple, we are only checking the coverage workflow.

   <img width="300" alt="target branch settings" src="https://github.com/user-attachments/assets/9b68fd13-8348-401e-b1a3-6fd2f8744759" />

   <img width="300" alt="required status checks" src="https://github.com/user-attachments/assets/a5fe16aa-9d3a-4ab1-9406-a288b6c7b2b5" />

1. Click **Create**.

1. Navigate back to the pull request and refresh the page.

1. The **Merge** button is now disabled! Nice! 🥰

   <img width="500" alt="failed tests and disabled merge button" src="https://github.com/user-attachments/assets/6dd46999-f98f-42fa-af65-b553c4e59c8e" />

1. In the pull request, find the comment that shares information about the coverage and failed tests. There are 2 issues preventing merging.

   - 1 test is failing.
   - Coverage is below the 90% requirement.

### Activity: Fix broken test

1. Switch to the VS Code Codespace.

1. Open the `tests/calculations_test.py` file.

1. After some investigation, we see the broken test might have been commented out because it was designed incorrectly.

   - A quick google search shows that the 10th entry in the Fibonacci sequence is `55`, not `89`.

1. Change the test to use the correct assert value.

   ```bash
   def test_get_nth_fibonacci_ten():
      """Test with n=10."""
      # Arrange
      n = 10

      # Act
      result = get_nth_fibonacci(n)

      # Assert
      assert result == 55
   ```

1. Commit the change and wait for the updated coverage report.

   - We will now see that all tests pass, but unfortunately the coverage is still too low.

## Activity: Fix low test coverage

1. Let's ask GitHub Copilot to find missing test cases.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, the test coverage is too low. Please find the missing tests to get us to 100% coverage.
   > ```

   <details>
   <summary>🪧 <b>Show:</b> Manual steps</summary>

   1. Open the `tests/calculations_test.py` file.

   1. Add the following 2 entries.

      ```py
      def test_area_of_circle_negative_radius(self):
         """Test with a negative radius to raise ValueError."""
         # Arrange
         radius = -1

         # Act & Assert
         with self.assertRaises(ValueError):
            area_of_circle(radius)
      ```

      ```py
      def test_get_nth_fibonacci_negative(self):
         """Test with a negative number to raise ValueError."""
         # Arrange
         n = -1

         # Act & Assert
         with self.assertRaises(ValueError):
            get_nth_fibonacci(n)
      ```

   </details>

1. Commit and push the changes.

1. Wait a moment for the tests to complete. If they all pass, the merge button should activate!

### Activity: Merge

1. Click the **Merge** button. Congrats, you are all done!

   <img width="500" alt="image" src="https://github.com/user-attachments/assets/1c75d9bc-62e9-429f-ad4d-45ea8b7d1a73" />
