# Make your own portfolio website

Rehearsal draft v0.3. Follow the steps in order. You choose the look and check your information; AI handles the files. Keep this guide open beside the desktop app.

## 1. Open the workshop page

1. Click [the workshop folder on GitHub](https://github.com/RaiqaRasool/PBSG-Sessions/tree/main/4.ResumeToPortfolio).
2. Read the introduction below the file list. GitHub is where the workshop materials are stored. You do not need an account to read a public page.
3. Click its **step-by-step guide** link to return here.

**Expected result:** you can see the introduction and guide. If the link is unavailable, ask the facilitator for the materials. Do not set up Git.

## 2. Download your starter folder

1. Click [Download the starter kit](https://github.com/RaiqaRasool/PBSG-Sessions/raw/refs/heads/main/4.ResumeToPortfolio/portfolio-starter.zip).
2. Open your computer's **Downloads** folder.
3. On a Mac, double-click `portfolio-starter.zip`. On Windows, right-click it, choose **Extract All**, then **Extract**.
4. Open the extracted `my-portfolio` folder. Check that it contains `AGENTS.md`, `DESIGN-OPTIONS.md`, `design-menu.svg`, and `START-HERE.md`.
5. Move this folder to your Desktop. If that name already exists, rename the new folder `my-portfolio-test-2` instead of replacing your previous work.

**Expected result:** a normal folder on your Desktop containing four files. Do not use the ZIP as your project. Do not download the whole sessions repository or copy its planning instructions.

## 3. Sign in

### Your AI assistant

1. Open the desktop app used for Codex. If needed, use [OpenAI's desktop download page](https://chatgpt.com/download/).
2. Sign in with your ChatGPT account.
3. Choose **Codex** for the portfolio work.

### Your website account

1. Open [GitHub](https://github.com/).
2. Click **Sign in** if you have an account. Otherwise click **Sign up** and follow the account-creation steps.
3. Complete any email verification requested by GitHub and stay signed in.

**Expected result:** both services are signed in. If your account lacks Codex access or your workplace blocks a service, ask the facilitator before continuing. Never paste passwords or access tokens into chat.

## 4. Connect GitHub

1. In the desktop app, open **Plugins**.
2. Search for **GitHub** and open its details.
3. Select its install control (shown as **+** in the current official instructions).
4. Follow the connection prompt. If GitHub opens in your browser, use the account from step 3 and review the access request before approving it. Some accounts are prompted to connect only when the plugin is first used.
5. Return to the desktop app and start a new Codex chat after installation.

**Expected result:** GitHub is installed. If the controls look different, ask the facilitator; do not install a separate MCP server or put a token in the chat.

## 5. Open your portfolio folder

1. In the desktop app, open **Projects** and create a project named **My Portfolio**.
2. Open the project's menu and choose **Edit project**.
3. Choose **Add folder**, select `my-portfolio` on your Desktop, and confirm the selection.
4. If there are several attached folders, use **Make primary** on this folder.
5. Start a new Codex chat inside **My Portfolio**.
6. Copy and send:

```text
Read AGENTS.md in this project's primary folder. Confirm that you can find DESIGN-OPTIONS.md and create files here. Check whether the connected GitHub tools are available. Do not build or publish yet. If anything is missing, give me one next action to fix it without using a terminal or setting up Git.
```

**Expected result:** AI confirms the starter files and identifies any connection problem before you begin. If it cannot find them, check that you selected the extracted folder, not the ZIP or its parent.

## 6. Supply your résumé and check the draft

1. Open your résumé and copy its text.
2. Paste the prompt below into the chat, then paste your résumé text underneath it.
3. If copying scrambles the text, open [PDF to Markdown](https://cloudconvert.com/pdf-to-md), click **Select File**, choose your PDF, start conversion, and download the result. Move the downloaded `.md` file into your portfolio folder and give AI its filename instead. This alternative uploads your résumé to another service; pasted text avoids that extra upload.

```text
Use my résumé below, or the résumé Markdown file I just added, to draft my portfolio content. Follow AGENTS.md. Show the proposed website text and list the contact details or other personal information that would become public. Do not build or publish yet.
```

**Expected result:** a readable draft suited to your work. Check names, dates, achievements, and public links. Tell AI any corrections. When satisfied, send:

```text
I approve the website content and public contact links we reviewed. Save the approved version in CONTENT.md.
```

## 7. Pick a look and preview

1. Open `design-menu.svg` from your folder in a browser, or [view the style cards here](design-menu.svg). They are schematic design references, not screenshots of finished portfolios.
2. Pick a number. Every option can suit research, technical, or business work.

| Number | Look | Personality |
| --- | --- | --- |
| **1** | Field Notes | Warm paper, ink blue, notebook-style notes |
| **2** | The Magazine | Big editorial headlines, ivory and red, work as stories |
| **3** | Color Studio | Bold cobalt and coral, playful blocks, expressive type |
| **4** | Retro Desktop | Nostalgic computer windows, mint accents, clear navigation |

3. Send this, replacing the number if needed. If unsure, choose **1**:

```text
Build my portfolio using design option 1 from DESIGN-OPTIONS.md and my approved CONTENT.md. Follow AGENTS.md. Open a preview, check desktop and phone layouts, and fix issues. Do not publish yet.
```

**Expected result:** AI opens a working preview or gives a clickable preview link. You should not need to run commands. Request changes in ordinary language, for example:

```text
Make the introduction shorter and my research more prominent. Keep the chosen look. Update the preview without publishing.
```

## 8. Publish the approved website

GitHub stores your website files in an online folder called a repository. GitHub Pages turns those files into the website. AI will handle this where its tools allow; the browser fallback below covers the two setup actions the plugin may not support.

1. When you like the preview, send:

```text
Publish this approved portfolio. Follow the first-publication procedure in AGENTS.md. Use my connected personal GitHub account and a new repository named my-portfolio. Save the repository address, publishing settings, and verified live website address in AGENTS.md so later updates need no links from me. Handle setup using available connected tools or browser. If I must click something, give one action at a time with a direct link. Do not require Git installation or terminal commands.
```

2. Complete authentication or permission prompts you approve. If the name already exists, AI must check before using it and must not replace an existing project.
3. Use **8A** only if AI cannot create the online folder. Use **8B** only if it cannot enable website publishing. Otherwise let AI finish.

### 8A. Create the online folder once, if needed

1. Click [Create my website folder](https://github.com/new?name=my-portfolio&visibility=public).
2. Check that **Owner** is your own GitHub username.
3. Keep **my-portfolio** as the name. If GitHub says it is already taken, use **my-portfolio-workshop**; do not delete an existing project.
4. Select **Public**, because these are the files for the website you are choosing to share. Your private source résumé will not be uploaded.
5. Turn on **Add a README file** so the folder has its first file. Leave the other optional settings unchanged.
6. Click **Create repository**.
7. Copy the browser address, paste it into the portfolio chat, and say: “This is my new website repository. Save this address and continue publishing.”

This is a one-time handoff, not something you repeat for updates. If the plugin has access only to selected repositories, grant it access to the new repository in its connection settings before retrying.

### 8B. Enable website publishing once, if needed

Wait until AI confirms that it uploaded the website files. Ask it for the direct link to your website repository's **Settings → Pages** screen.

1. Open that link. Alternatively, open the repository, click **Settings**, then **Pages** in the left sidebar.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Under **Branch**, choose **main**.
4. In the folder dropdown, choose **/docs**. The starter instructions place the website files there.
5. Click **Save**.
6. Return to the chat and send: “Pages is enabled for main and /docs. Verify the live website and save its address.”

**Expected result:** AI gives a clickable live link and confirms it checked the published version. Open it yourself too. Publishing may take time; uploaded files alone do not mean the site is live. If there is an error, paste it into chat and ask AI to diagnose it before retrying setup.

## 9. Update your website later

1. Open the desktop app and select **My Portfolio**.
2. Return to its chat or start a new Codex chat inside that same project. Keep your portfolio folder: it contains the saved publishing record.
3. Send this, changing only the description of your change:

```text
Read AGENTS.md and update my existing portfolio. Change my introduction to: [type your new introduction here]. Preview and check the change, then publish it using the saved repository and publishing settings. Verify that the saved live website address shows the update. Keep everything else as it is.
```

To preview only, replace “then publish it” with “do not publish yet.” You can describe any content or design change.

**Expected result:** the same live website address shows the update. You should not need to provide either address again. If AI asks, say: “Read the publishing record in AGENTS.md first.” If the folder or record was lost, AI should help recover the existing destination rather than create a second website.

## If you get stuck

- **Different buttons:** ask the facilitator and say which numbered step you reached.
- **AI asks for Git installation or terminal commands:** say, “Use the connected GitHub tools and this starter's no-terminal instructions.”
- **Permission denied:** check that the plugin uses the account owning the website repository and has access to that repository.
- **Old or missing website:** ask AI to check deployment status and the saved live URL before uploading again.

## Setup sources

The facilitator must verify exact screens in the workshop app version before release. This draft uses official [desktop setup](https://developers.openai.com/codex/app/), [projects and folders](https://learn.chatgpt.com/docs/projects), [plugin installation](https://learn.chatgpt.com/docs/plugins), [repository creation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), and [Pages settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) documentation.
