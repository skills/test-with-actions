<!--
  <<< Author notes: Step 4 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
-->

## Step 4: Add branch protections

_Great job uploading test reports! :partying_face:_

Take a look at the merge box, you'll notice you can merge this even though the review process hasn't been met.

Protected branches ensure that collaborators on your repository cannot make irrevocable changes to branches. Enabling protected branches also allows you to enable other optional checks and requirements, like required status checks and required reviews.

### :keyboard: Activity: Add branch protections

1. Go to **Branches** settings. You can navigate to that page manually by selecting the right-most tab in the top of the repository called **Settings** and then selecting **Branches**.
1. Select **Add branch protection rule** under "Branch protection rules".
1. Type `main` in **Branch name pattern**.
1. Check **Require a pull request before merging**.
1. Check **Require status checks to pass before merging**.
1. Check all build and test jobs that you'd like to see in the newly visible gray box.
1. Select **Save changes**.
1. _Once you turn on branch protection, Actions can no longer push directly to `main`. You'll need to open the next step on your own._

<!-- Wait about 20 seconds then refresh this page (the one you're following instructions from). [GitHub Actions](https://docs.github.com/actions) will automatically update to the next step. -->
