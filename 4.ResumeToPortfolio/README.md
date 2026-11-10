# Build and publish a website with Codex

Follow the Cookie Shop tutorial to set up Codex, open a project folder, and preview a site in the app. You can build the game as shown or swap in your own résumé to make a portfolio. Both paths end with a live website at `https://YOUR-USERNAME.github.io/`.

[Follow the Cookie Shop tutorial on VideoToBlog](https://videotoblog.ai/share/jrVWl38Gw2wAlp9P71La)

## 1. Choose what to build

Follow the tutorial’s desktop setup until you have a local project folder open in Codex. When you reach the first build prompt, choose one path.

- **Cookie Shop** — Use the game prompt from the tutorial and preview the result as shown.
- **Your portfolio** — Add your résumé to the project folder, then use the portfolio prompt below.

### Prepare your résumé

If your résumé is a PDF:

1. Open the [PDF-to-Markdown converter](https://cloudconvert.com/pdf-to-md), click **Select File**, and choose a PDF you’re comfortable uploading.
2. Click **Convert**, then download the Markdown (`.md`) file when it’s ready.
3. Open **Downloads** and copy the downloaded file into the project folder you opened in Codex. Rename it to `resume.md` if it has a different name. Open it and check that your names, dates, and sections came through.

If you already have a Markdown résumé, copy it into the project folder and name it `resume.md`. If you don’t have a résumé handy, save the [fictional sample résumé](SAMPLE-RESUME.md) there as `resume.md` and tell Codex you’re using the sample.

### Portfolio prompt

```text
I’ve opened a new folder containing resume.md. Use the Git available in the workspace to initialize a local repository here with main as the initial branch. If this folder is already inside a different repository, ask me to open a separate project folder before committing. After I approve the design and you’ve built and checked the first working version, commit the website files. Make a separate local commit for each completed revision I request. Stage website files by name and keep resume.md, reference screenshots, and private notes out of every commit. Wait for my approval before pushing to GitHub.

Help me turn resume.md in this folder into a one-page portfolio website.

Ask me what you need to know about the look, who the site is for, and what I want to highlight. I can share a screenshot, a website URL, or a description. If I say “surprise me,” suggest a distinctive direction that suits my work. Use any reference as inspiration for an original design.

Use my résumé as the source for factual claims and choose sections that fit my experience. Show me a short proposal for the content and design before you build. Ask before including personal contact details. If I’m using the sample résumé, clearly label the site as a fictional demo.

Once I approve, create readable, formatted index.html and styles.css files in the same folder as resume.md. Add a separate JavaScript file only if an interaction needs it. Use relative paths so the page works when I double-click index.html, with no server or build step.

Optional design reference: [screenshot filename, website URL, or description, plus what I like about it]
```

Open the preview and try the result. For a portfolio, check the facts, links, and public contact details. For Cookie Shop, try playing one day. If you want a change, describe it in the same Codex chat.

## 2. Send the site to GitHub

Follow the tutorial’s GitHub plugin setup. In Codex, open **Customize → Plugins**, find **GitHub**, and follow the connection prompts. Sign in to GitHub when prompted. If you’re new to GitHub, [create a free account](https://github.com/signup), verify your email, then return to Codex and finish connecting. If GitHub asks which repositories the connection can access, grant access to your website repository once it exists.

A **commit** saves a version of the website files. The first prompt saves your checkpoints locally. The GitHub plugin can send the approved files as a new commit on GitHub, so the two histories may differ. Paste this into your project chat once you’ve reviewed the preview.

```text
Use the connected GitHub plugin to help me publish the website we just reviewed. Ask me for my GitHub username if you need it. Use my personal account and a public repository named exactly YOUR-USERNAME.github.io, with my actual username in place of YOUR-USERNAME.

If that repository already exists, inspect it and ask before making changes. If the plugin cannot create the repository, tell me what I need to do on GitHub and wait for me to finish. If you can access an existing repository but cannot write to it, tell me what access is missing.

Prepare a short README.md for the public repository. Describe the site and include a clickable link to https://YOUR-USERNAME.github.io/ with my actual username. Say that the link will work once GitHub Pages deploys. If GitHub created a starter README, update it with this content. Show me which files will be public and ask for my approval. Then commit and send only those approved files to main. Place index.html, README.md, and the site’s CSS, scripts, and public assets at the top level of the repository, preserving any asset paths the site uses. Leave resume.md, the original résumé, reference screenshots, and private notes out of every commit. If any of those files are already in local Git history, upload only the approved files to the remote repository without pushing that history. Give me the repository link and tell me whether the upload succeeded.
```

**If Codex says the connected plugin can’t create a repository:** Open [New repository](https://github.com/new), select your personal account, and name it exactly `YOUR-USERNAME.github.io`. For example, if your username is `octocat`, enter `octocat.github.io`. Choose **Public**, turn on **Add README** to create the first branch, and click **Create repository**. Codex will update that starter README with your site link. Return to Codex and ask it to continue. If the connection can’t write to the repository, check its repository access. You can also use **Add file → Upload files** on GitHub to upload the approved site files. [GitHub file upload guide](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

Open your repository link and confirm that `index.html` and `README.md` appear in the top-level file list.

## 3. Turn on GitHub Pages

1. On your GitHub repository page, click **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Choose **main** and **/(root)**, then click **Save**.
4. Wait for deployment, then return to the repository’s **Code** tab and click the site link in the README. Check that the site, styles, and images load. If the site is still unavailable after 10 minutes, check the **Actions** tab for the Pages deployment result. [Illustrated GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart)

When you make a later edit, preview it first and ask Codex to send the approved changes to the same repository and branch. After Pages deploys again, refresh the same public address.
