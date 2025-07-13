## Step 3: Trigger the workflows

<!-- Take a look at the merge box, you'll notice you can merge this even though the review process hasn't been met. -->

<!-- Protected branches ensure that collaborators on your repository cannot make irrevocable changes to branches. Enabling protected branches also allows you to enable other optional checks and requirements, like required status checks and required reviews. -->

As specified in our workflows, they will only run when a pull request is targeting the `main` branch.

Pull requests have a nice advantage when a workflow is associated with them. The run status and results can be displayed directly in the conversation feed.

### ⌨️ Activity: Make a code change

1. Return to the VS Code Codespace.

1. Create a new branch based on `main` with the following name and **publish** it to GitHub.

   ```txt
   reenable-unit-test
   ```

1. Open the `tests/calculations_test.py` file.

1. After investigating the code, we see a commented out test on line 56. Uncomment it to re-enable it.

   > Hopefully they didn't disable it to get around testing! 😱

   ```py
   def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 89
   ```

1. Commit the changes and push them to GitHub.

1. Return to the browser and create a pull request. Use the following details.

   - **base:** `main`
   - **source:** `reenable-unit-test`
   - **title**: `Reenable unit test that was disabled`

1. After the pull request is created, look near the Merge button to see the many workflows running.

   - Our coverage workflow will fail, letting us know we have a test to fix.

1. With the pull request started, Mona should be busy checking your work and preparing the next steps.

<details>
<summary>Need help?</summary>

- If the checks don't appear or updated, try refreshing the page. It's possible the workflow ran and the page just hasn't been updated with that change.

</details>
