# Publish at your own GitHub Pages address

Start here after you’ve opened and reviewed your local website. GitHub stores the website files in an online project folder called a **repository**. GitHub Pages turns those files into a website. GitHub Desktop is an app with buttons for saving and sending changes. It works without terminal commands or a separate Git installation.

The name of the repository determines the address. If your GitHub username is `octocat`, name the repository exactly `octocat.github.io`. Your site will open at `https://octocat.github.io/`.

If you want documentation for visitors to your repository, paste this into your portfolio chat before copying the website files.

```text
Add a short public README.md inside portfolio/. Explain what the site is, how to open it locally, and which files to edit for copy and styling. Leave the live link out until I have verified it. If I ask for AGENTS.md too, keep it short and cover direct browser preview, readable code, and approval before publishing. Leave private source details out of both files.
```

## 1. Set up GitHub and GitHub Desktop

1. If you need an account, open [GitHub sign-up](https://github.com/signup), choose a username you’re comfortable showing in your website address, and follow the email verification steps. If you already have an account, sign in. Click your profile picture in the top-right corner to check your username. [GitHub account setup](https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github)
2. Download and open GitHub Desktop for your Mac or Windows computer. On Mac, open **GitHub Desktop → Settings → Accounts**. On Windows, open **File → Options → Accounts**. Click **Sign Into GitHub.com**, approve the sign-in in your browser, and return to GitHub Desktop. Accept or review the name and email it will attach to your commits if prompted. [Download GitHub Desktop](https://desktop.github.com/) · [Illustrated install and sign-in guide](https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop)
3. In Finder or File Explorer, inspect the generated `portfolio` folder. Check that it contains only files you are comfortable making public, including the page copy, images, and any documents. Keep your original résumé, reference screenshots, and private notes in `my-portfolio`, outside `portfolio`.

## 2. Create your online project folder

1. In your browser, open [GitHub’s new repository page](https://github.com/new).
2. Under **Owner**, choose your personal account. For **Repository name**, enter your own username followed by `.github.io`. If GitHub says the name already exists, open the existing repository and check what it hosts before making changes. Ask the facilitator for help if the existing site is unfamiliar.
3. Choose **Public** for the free hosting path. Turn on **Add README** so GitHub creates the first branch. Click **Create repository**. You should see a repository page with a README in its file list. [GitHub Pages quickstart with screenshots](https://docs.github.com/en/pages/quickstart)

## 3. Put your website in the repository

1. On that repository page, click the green **Code** button and choose **Open with GitHub Desktop**. If your browser asks to open the app, allow it.
2. In GitHub Desktop, choose a **Local path** outside your private `my-portfolio` folder, such as a new folder inside **Documents** named after your repository. Click **Clone**. This makes a local copy of the online repository.
3. In GitHub Desktop, choose **Repository → Show in Finder** on Mac or **Show in Explorer** on Windows. The folder that opens should contain the README. Copy the **contents** of `my-portfolio/portfolio` into this folder. You should see `index.html` and `styles.css` next to `README.md`. Keep any image subfolders in the same arrangement. If you generated a README for the site, you can replace the default README with it.
4. In GitHub Desktop’s **Changes** tab, look through the file list and confirm each file belongs on the public site. In **Summary**, type `Add portfolio website`, then click **Commit to main**. A commit is a saved snapshot of those changes. Click **Push origin** to send it to GitHub.
5. Refresh the repository page in the browser. Confirm `index.html` is visible in the file list alongside `README.md`. [Illustrated cloning guide](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop) · [Illustrated commit and push guide](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)

## 4. Turn on GitHub Pages

1. On the repository page, choose **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch** for **Source**.
3. Select **main** and **/(root)** and click **Save**. If your repository displays a different default branch name, use the branch where you can see `index.html`.
4. Allow up to 10 minutes for the first deployment. Reload **Settings → Pages** and look for the live address or **Visit site**. Open `https://YOUR-USERNAME.github.io/` using your username. Check that it shows your website with styling and images. [GitHub Pages quickstart with screenshots](https://docs.github.com/en/pages/quickstart)

If the address shows a 404 or an unexpected page, check **Actions** on GitHub for the Pages deployment result. If it succeeded, confirm the repository name exactly matches your username plus `.github.io` and that `index.html` is beside the README on the selected branch. If the page loads but has missing styling, check that the CSS and assets were copied and pushed with their original names and folders.

## 5. Send later edits to the same address

1. Keep asking Codex to edit the website in your original `my-portfolio` project. Preview `portfolio/index.html` there. If you want Codex to add a short README or AGENTS.md for future editors, review those as public files too.
2. Copy the changed public website files to the same local repository folder from step 3. Replace the corresponding files. If you intentionally removed a public file, remove that file from the local repository copy as well.
3. In GitHub Desktop, review **Changes**, write a short summary such as `Improve research section`, click **Commit to main**, then **Push origin**.
4. Check **Actions** for the latest deployment, then refresh your existing website URL and check the change. Pages uses the saved branch and folder each time.
