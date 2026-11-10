# Build and publish a website with Codex

Follow the Cookie Shop tutorial to set up Codex, open a project folder, and preview a site in the app. You can build the game as shown or swap in your own résumé to make a portfolio. Both paths end with a live website at `https://YOUR-USERNAME.github.io/`.

[Follow the Cookie Shop tutorial on VideoToBlog](https://videotoblog.ai/share/jrVWl38Gw2wAlp9P71La) · [ChatGPT desktop setup help](https://learn.chatgpt.com/docs/quickstart?setup=app)

Before the workshop, install the ChatGPT desktop app, sign in, and confirm you can open Codex.

## 1. Choose what to build

Follow the tutorial’s desktop setup until you have a local project folder open in Codex. When you reach the first build prompt, choose one path.

- **Cookie Shop** — Use the game prompt from the tutorial and preview the result as shown.
- **Your portfolio** — If you have a PDF résumé, upload a copy you’re comfortable sharing to the converter, download the Markdown (`.md`) file, and copy it from Downloads into the project folder you opened in Codex. If you already have a Markdown or plain-text résumé, copy it into that folder. You can also save a copy of the [fictional sample résumé](SAMPLE-RESUME.md) there. Then paste the portfolio prompt below. [PDF-to-Markdown converter](https://cloudconvert.com/pdf-to-md)

### Portfolio prompt

```text
Help me turn the résumé in this folder into a one-page portfolio website.

Ask me what you need to know about the look, who the site is for, and what I want to highlight. I can share a screenshot, a website URL, or a description. If I say “surprise me,” suggest a distinctive direction that suits my work. Use any reference as inspiration for an original design.

Use my résumé as the source for factual claims and choose sections that fit my experience. Show me a short proposal for the content and design before you build. Ask before including personal contact details. If I’m using the sample résumé, clearly label the site as a fictional demo.

Once I approve, create a portfolio folder with readable, formatted index.html and styles.css files. Add a separate JavaScript file only if an interaction needs it. Use relative paths so the page works when I double-click index.html, with no server or build step. Keep my original résumé and reference screenshots outside the portfolio folder.

Show me how to open the finished page in Codex’s built-in browser. If that preview is unavailable, point me to the index.html file I can open directly.

Optional design reference: [screenshot filename, website URL, or description, plus what I like about it]
```

Open the preview and try the result. For a portfolio, check the facts, links, and public contact details. For Cookie Shop, try playing one day. If you want a change, describe it in the same Codex chat.

## 2. Send the site to GitHub

Follow the tutorial’s GitHub plugin setup. In Codex, open **Customize → Plugins**, find **GitHub**, and follow the connection prompts. Sign in to GitHub when prompted. If you’re new to GitHub, [create a free account](https://github.com/signup), verify your email, then return to Codex and finish connecting. If GitHub asks which repositories the connection can access, grant access to your website repository once it exists.

A **commit** saves a version of the website files. **Pushing** sends that version to GitHub. Paste this into your project chat once you’ve reviewed the preview.

```text
Use the connected GitHub plugin to help me publish the website we just reviewed. Ask me for my GitHub username if you need it. Use my personal account and a public repository named exactly YOUR-USERNAME.github.io, with my actual username in place of YOUR-USERNAME.

If that repository already exists, inspect it and ask before making changes. If the plugin cannot create the repository, tell me what I need to do on GitHub and wait for me to finish.

Show me which files will be public and ask for my approval. Then commit and send only those approved website files to main. For the portfolio, take the contents of portfolio/ and place index.html and its assets at the top level of the repository. For Cookie Shop, send the game’s site files in the same way. Keep the original résumé, reference screenshots, and private notes out of the commit. Give me the repository link and tell me whether the upload succeeded.
```

**If Codex asks you to create the repository:** Open [New repository](https://github.com/new), select your personal account, and name it exactly `YOUR-USERNAME.github.io`. For example, if your username is `octocat`, enter `octocat.github.io`. Choose **Public**, turn on **Add README**, and click **Create repository**. Return to Codex and ask it to continue. If the connection can’t write to the repository, check its repository access. You can also use **Add file → Upload files** on GitHub to upload the approved site files. [GitHub file upload guide](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

Open your repository link and confirm that `index.html` appears in the top-level file list.

## 3. Turn on GitHub Pages

1. On your GitHub repository page, click **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Choose **main** and **/(root)**, then click **Save**.
4. Wait for deployment, then open `https://YOUR-USERNAME.github.io/` using your actual username. Check that the site, styles, and images load. If the site is still unavailable after 10 minutes, check the **Actions** tab for the Pages deployment result. [Illustrated GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart)

When you make a later edit, preview it first and ask Codex to send the approved changes to the same repository and branch. After Pages deploys again, refresh the same public address.
