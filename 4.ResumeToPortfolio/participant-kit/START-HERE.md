# From résumé to your own portfolio

Rehearsal v0.9. Follow these steps in order. You supply your résumé, choose a personality, and approve the result. AI handles the website files. No coding, terminal commands, Git installation, Firecrawl setup, or Playwright MCP setup is required.

## 1. Download the starter folder

1. Click [Download portfolio-starter.zip](https://github.com/RaiqaRasool/PBSG-Sessions/raw/refs/heads/main/4.ResumeToPortfolio/portfolio-starter.zip).
2. Open **Downloads** on your computer.
3. On a Mac, double-click the ZIP. On Windows, right-click it, choose **Extract All**, then **Extract**.
4. Open the extracted `my-portfolio` folder. It contains the guides, `AGENTS.md`, a fictional sample résumé, and a `references` folder. You do not need to edit the instruction files.
5. Move `my-portfolio` to your Desktop. For a second rehearsal, rename the new folder `my-portfolio-test-2` rather than replacing your existing work.

**Expected result:** a normal extracted folder. Keep this guide open in your browser; do not open the ZIP as your project or download the whole sessions repository.

## 2. Complete the one-time setup

Follow [SETUP.md](SETUP.md). It links existing official installation guides, project illustrations, a plugin video, and GitHub help.

Set up the desktop app with Codex access, then connect its GitHub plugin. GitHub sign-in or account creation happens as part of that connection. You do not need to start a chat until your folder is attached in Step 3.

**Expected result:** the AI app is open and GitHub is connected. Repository installation access is checked in Step 7; signing in alone does not guarantee upload permission.

## 3. Open the folder and start your first chat

Keep [the official project/folder guide](https://learn.chatgpt.com/docs/projects#use-local-projects-for-folders-and-codebases) beside you if needed.

1. In the desktop app, open **Projects** and create a project named **My Portfolio**. For a fresh second rehearsal, use **My Portfolio — rehearsal 2** so the old folder and chat stay separate.
2. Open its menu, choose **Edit project**, then **Add folder**.
3. Select the extracted `my-portfolio` folder on your Desktop and confirm. If several folders are attached, use **Make primary** on this one.
4. Select **Codex**, then start a new chat inside **My Portfolio**. This is your portfolio-building chat. Do not use the workshop planning folder.
5. Copy and send:

```text
Read AGENTS.md in this project's primary folder. Confirm that you can read DESIGN-OPTIONS.md and references/ and create files here. Check the connected GitHub tool capabilities for reading, remote commits, repository creation, Pages configuration, and deployment-status checks. State actual limitations upfront; don't infer capabilities from the plugin name. We will prepare repository access in Step 7, so don't ask me to choose a repository now. Identify an available preview method that needs no new plugin or browser-control setup. Do not build, publish, or require Firecrawl, Git installation, or terminal commands.
```

**Expected result:** AI confirms the folder and reports capabilities. In the first rehearsal, remote commits were available but repository creation and Pages configuration needed manual clicks. Missing optional automation does not stop content/design work. If the files cannot be found, check that the extracted folder is primary.

## 4. Put your résumé in the folder as MY-RESUME.md

Use this one filename so later prompts work without editing paths.

1. Open [CloudConvert PDF to Markdown](https://cloudconvert.com/pdf-to-md).
2. Click **Select File** and choose your résumé PDF. Start the conversion and download the Markdown result. This sends the PDF to CloudConvert; use the fictional sample below if you do not want that extra upload. If your résumé is already Markdown, skip conversion.
3. In Downloads, right-click the downloaded Markdown file and choose **Rename**. Name it exactly **MY-RESUME.md**. On a Mac you can also select it and press Return. Do not leave `.txt` or a second `.md` extension on the name; if uncertain, ask AI to check the folder filenames.
4. Move `MY-RESUME.md` into the extracted `my-portfolio` folder, beside `AGENTS.md`.

**Expected result:** your folder contains `MY-RESUME.md`. AI will flag extraction problems in the draft. No résumé text needs to be pasted into the chat.

**Backup only — no résumé with you?** Skip conversion and use the supplied [SAMPLE-RESUME.md](SAMPLE-RESUME.md). It is entirely fictional. Choose the sample prompt in Step 5; never combine sample facts with your own identity.

## 5. Draft website content from the facts

For your own résumé, send:

```text
Use MY-RESUME.md to draft my portfolio content. Do not use SAMPLE-RESUME.md. Follow AGENTS.md. Select useful website sections rather than copying every résumé heading. Rewrite for scanning: a short introduction, purposeful headings, concise summaries, and supported highlights. Do not invent facts, require Projects, or ask for more material. List what would be public and any important extraction uncertainty. Save CONTENT.md as a draft; do not build or publish yet. We will adapt its voice after I select a personality.
```

The literal filename works without an @ mention. If your app offers file mentions, you can optionally type `@` and select `MY-RESUME.md`.

**Sample backup prompt instead:**

```text
Use SAMPLE-RESUME.md for a fictional practice portfolio. Do not use other résumé files. Follow AGENTS.md and draft concise, skimmable website content from the supplied facts. Choose useful sections; do not add Projects or ask for more material. Preserve a visible Fictional workshop demo label and omit unsupported contact actions. Save CONTENT.md as a draft. Do not build or publish yet.
```

**Expected result:** a draft website outline and copy, not a wall of résumé paragraphs. AI may combine, rename, shorten, or omit sections. References and application objectives usually stay out. Projects, publications, awards, photos, and contact links are not mandatory.

Check names, dates, facts, and the proposed public details. Tell AI any corrections. Continue to Step 6 to choose the personality before approving final copy.

## 6. Choose the personality, approve its copy, then build

1. Open [DESIGN-OPTIONS.md](DESIGN-OPTIONS.md). Each choice links a prepared brief and the original website.
2. Optionally explore original links. You are choosing design and personality, not someone else's achievements, content volume, or page count. A short résumé is enough.
3. Pick a name or number. If unsure, try Seán for soft/expressive, Brittany for structured/professional, or Cassidy for compact/personal.
4. Send this, replacing Seán Halpin with your choice if needed:

```text
Use the prepared Seán Halpin option in DESIGN-OPTIONS.md. Read its local brief and my CONTENT.md draft. Before building, revise CONTENT.md to express that personality through the headline, section names, introduction, and highlight summaries while preserving my voice and every factual boundary. Keep the copy short and easy to scan; don't fill space with generic claims. Show the revised copy and a few before/after examples. In DESIGN.md record 3–5 defining visual cues and 2–3 personality traits, the font/fallback choice, and how they will appear in my site. Use the prepared files without browsing the original or requiring Firecrawl. Wait for my approval; do not build or publish yet.
```

5. Check that the wording feels appropriate and the facts/public details are correct. Ask for changes if needed. When satisfied, send:

```text
I approve the revised CONTENT.md, public details, and design/personality plan. Build the one-page portfolio following AGENTS.md. Use normally formatted, readable HTML/CSS/JavaScript under site/. Open an available native preview, or give me a clickable local site/index.html that opens directly in a browser without a server. Do not require Playwright MCP, additional browser setup, or browser automation access. Compare the preview against the defining visual cues and personality traits in DESIGN.md, fix mismatches, and check desktop/phone layouts where tools allow. Report any checks you could not perform and tell me how to inspect those myself. Do not publish yet.
```

**Expected result:** a preview that reflects both the visual direction and presentation style. The files should be readable and easy to edit. On phones, short navigation may stay visible; a longer menu can use an accessible toggle. AI should not claim visual testing it could not perform.

If automatic preview is unavailable, open the local `site/index.html` link or double-click that file inside the folder. Narrow the browser window to check the phone layout. You do not need to give AI control of your browser.

Request refinements naturally: “Make research more prominent; keep the chosen personality and update the preview without publishing.”

**Optional later:** [prepare your own reference](OPTIONAL-REFERENCE.md). Sites hosting is also a separate optional experiment, not required for this GitHub Pages path.

## 7. Prepare your website's GitHub address and app access

GitHub calls the online project folder a **repository**. For an account's main website, its name must be **your-github-username.github.io**, giving **https://your-github-username.github.io/**. An arbitrary repository name creates a different project address; it does not rename the account website. Only one main account site exists per account.

1. Send:

```text
Prepare the GitHub destination for this portfolio without uploading the website yet. Use connected GitHub tools only; do not control my browser or use a CLI. Identify the connected personal account if supported; otherwise ask me for my GitHub username once. Default to its main username.github.io website repository. Inspect any existing repository/site before choosing it, and confirm before replacing an existing site. Check which creation, installation-access, write, and Pages-settings capabilities are actually available. Explain known limitations before asking me to act, then give one concrete next action with a direct link. Save the confirmed destination in AGENTS.md. Do not claim app write access is verified from my user admin/push status or a successful read. Do not upload or publish yet.
```

2. If creation is unsupported and you do not already have the repository, AI should provide a prefilled GitHub creation link. Open it, check **Owner** is your own account, and use the exact lowercased `username.github.io` name. Choose **Public**, turn **Add README** on, then click **Create repository**. Keep other optional settings unchanged. The README avoids an empty-repository initialization problem. Use [GitHub's screenshot guide](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site) if needed.
3. If AI could not discover the new address, copy it from your browser and give it to the chat once. It must save it for later use. Do not create a second repository just because connection access fails.
4. Open [Installed GitHub Apps](https://github.com/settings/installations) on the account that owns the website repository. Find the connection's app (reported as **Codex Connector** in the rehearsal), click **Configure**, and confirm the correct installation account. Under **Repository access**, choose **Only select repositories**, select your website repository, and **Save**. If it already has the intended repository, review the app's granted permissions rather than widening access blindly. See [GitHub's app-access guide](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps).
5. Return to the chat and say: “The app has my website repository selected. Recheck access and save the destination.” Any missing app installation must be completed through the connection's installation flow. Work-account restrictions may need an administrator.

**Expected result:** the repository is confirmed and the installation-access check is documented. Reads can succeed even when writes are blocked; the authorized upload in Step 8 is the actual write check. In the reported rehearsal, the tools could upload but could not create the repository or select Pages settings. Expect the one-time settings clicks below if those tools are still absent.

## 8. Publish the approved preview

For a new, website-only account repository, we use **main** and **/(root)**. AI uploads only the public files from local `site/` into the remote repository root. Your résumé and internal instruction/content files stay local. If an existing site uses /docs or a custom domain, AI must inspect and confirm the existing arrangement rather than silently change it.

1. Send:

```text
Publish the preview I approved to the destination saved in AGENTS.md. Use connected GitHub MCP tools for repository inspection, remote commits, and deployment checks. Do not use browser automation or a CLI. Inspect current remote files first and preserve unrelated work. Upload only the approved public files from local site/ to the confirmed remote publishing folder. For a new website-only username.github.io repository, use main + /(root), with index.html and .nojekyll at the root. Do not upload my résumé, CONTENT.md, AGENTS.md, reference briefs, or starter guides. Prefer one complete site commit, but initialize an empty repository first if required and supported. If a capability or permission is missing, explain it and give me one direct-link action instead of silently switching tools. Save the publishing settings and expected live address. Report upload, deployment, and live-content verification separately. Do not add a custom workflow for this no-build site.
```

2. If GitHub denies the upload with **403**, ask AI to diagnose the app installation/repository selection and granted write permissions first, then any relevant branch restrictions. Having user admin/push permission does not establish that the connection app can write. Do not repeatedly retry the same upload or grant browser control as a workaround.
3. If Pages configuration is unsupported, AI should give you the exact repository **Settings → Pages** link. Open it and set:

| Setting | Select |
| --- | --- |
| Source | **Deploy from a branch** |
| Branch | **main** |
| Folder | **/(root)** for the new website-only repository |

4. Click **Save**. For an existing confirmed /docs site, use that saved folder instead; do not guess or change it to root.
5. Return to the chat and send:

```text
I saved the confirmed Pages branch and folder. Check deployment using connected tools, and read the live website where network access permits. Verify the approved content and required assets. Save the confirmed repository address, local-to-remote file mapping, publishing settings, live address, and separate verification states in AGENTS.md. Give me the live link. If a network permission is needed to check the site, explain that separately from deployment success; do not call an unverified page verified.
```

**Expected result:** AI distinguishes **files uploaded**, **deployment succeeded/pending/failed**, and **live content verified/not verified**. Open the live link yourself too. GitHub says publication can take up to 10 minutes; a completed upload is not immediate proof of the new page. If an old version remains, refresh after deployment and ask AI to check status before another upload.

Once enabled, GitHub Pages automatically republishes changes committed to the selected branch/folder. No custom CI/CD workflow or résumé watcher is needed. Keep using Step 9 to review and approve changes before sending them online.

## 9. Update your résumé, review the changes, then publish

1. Keep your existing portfolio folder and select **My Portfolio** in the app. Resume its chat or start a new Codex chat in the same project. Do not download a fresh kit over it: AGENTS.md holds your saved destination.
2. Edit `MY-RESUME.md` in a text editor: replace or add the new résumé text and save. Alternatively convert your updated PDF again and replace that file with the new Markdown under the same filename. If practising with the sample, edit `SAMPLE-RESUME.md` and name that file in the next prompt instead.
3. Send:

```text
Read AGENTS.md, DESIGN.md, and CONTENT.md. Compare my updated MY-RESUME.md with the current approved website content and inspect the current saved remote website before proposing edits where connected access permits. Summarize additions, changes, removals, and uncertainties. Distinguish source facts from website wording and flag any existing website-only edits so they are not silently discarded. Propose revised copy in the saved personality and identify affected sections. Do not modify approved CONTENT.md, website files, or publish yet. Wait for me to accept or correct the proposal. Do not ask for saved URLs or extra portfolio material.
```

4. Review the proposed changes. When satisfied, send:

```text
I approve the proposed content changes with these corrections: [say none, or describe corrections]. Update CONTENT.md and the local website, preserving the approved design/personality and saved publishing destination. Check and open the preview using the existing method. Do not upload or publish yet; wait for my preview approval.
```

5. Inspect the preview. When satisfied, send:

```text
I approve this preview. Publish only these approved website changes through connected GitHub tools using the destination and file mapping already saved in AGENTS.md. Check for intervening remote changes first. Report upload, deployment status, and live-content verification separately, then give me the saved live link. Mention any propagation delay or verification permission still needed. Do not change the destination or create another website.
```

**Expected result:** the same website address eventually shows the approved update. No link lookup, Git setup, or automatic publication of unfinished edits is needed.

## If a step fails

Tell AI the numbered step and the exact error. It should check capabilities, explain the limitation, and give one concrete next action. Do not delete the repository, install Git/Playwright, repeatedly upload unchanged files, or start over because a permission or network check failed.

For setup help, return to [SETUP.md](SETUP.md). These are rehearsal instructions; report confusing screens and results to the facilitator before improvising.
