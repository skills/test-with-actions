## Step 3: Trigger the workflows

As specified in our workflows, they will only run when a pull request is targeting the `main` branch.

Pull requests have a nice advantage when a workflow is associated with them. The run status and results can be displayed directly in the conversation feed.

### ⌨️ Activity: Start a PR and propose a code change

1. Return to the VS Code Codespace.

1. Create a new branch based from `main` with the following name and **publish** it to GitHub.

   ```txt
   reenable-unit-test
   ```

1. Double check that you are on the `reenable-unit-test` branch, then open the `tests/calculations_test.py` file.

1. After investigating the code, we see a commented out test on line 56. Uncomment it to re-enable it.

   > Hopefully it wasn't disable to get around testing! 😱

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

1. After the pull request is created, look near the Merge button to see many workflows running.

   - Our coverage workflow will fail, letting us know we have a test to fix.

1. With the pull request started, Mona should be busy checking your work and preparing the next steps.

<details>
<summary>Need help?</summary>

- If the checks don't appear or updated, try refreshing the page. It's possible the workflow ran and the page just hasn't been updated with that change.

</details>
