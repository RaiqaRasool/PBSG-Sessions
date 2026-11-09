# From résumé to portfolio

You’ll make a one-page website on your computer, open it in a browser, and revise it by talking to Codex. If you want a public link, the optional publishing guide takes you to `https://YOUR-USERNAME.github.io/`.

## 1. Make a folder for your résumé

1. On a Mac, open **Finder**. On Windows, open **File Explorer**.
2. Go to **Documents**. On Mac, choose **File → New Folder**. On Windows, choose **New → Folder**. Name it `my-portfolio`.
3. Copy your résumé into that folder. Start with the file you have. A text-based PDF or a Word document is fine to try. If Codex can’t read it accurately, open it yourself, copy the text into a plain-text editor, and save it in that folder as `resume.txt`. On Mac, use TextEdit and choose **Format → Make Plain Text** before saving. On Windows, use Notepad. If you can’t select text in your PDF, try the original Word document or the sample below.
4. If you have a screenshot you like, copy it into the same folder. You can also paste a website address into the chat or describe a look in your own words. A reference is optional.

**No résumé handy?** Open the [fictional sample résumé](SAMPLE-RESUME.md) and use **Raw** on GitHub to open the plain text. Copy it into TextEdit or Notepad and save it as `sample-resume.txt` in your folder. If you already downloaded and unpacked the starter, the sample is included. Tell Codex you’re using the fictional sample.

## 2. Open your folder in Codex

1. Install the **ChatGPT desktop app** for your Mac or Windows computer if you need it. Open it and sign in to your ChatGPT account. Use the illustrated official quickstart if you need help finding the download or opening Codex. [OpenAI desktop quickstart](https://learn.chatgpt.com/docs/quickstart?setup=app)
2. In the app, open **Projects** and create a **local project** for this workshop. Select your `my-portfolio` folder. If the project is already open and you still need to connect the folder, open its menu and choose **Edit project → Add folder**. If more than one folder is connected, use **Make primary** on `my-portfolio`. [OpenAI guide to local projects](https://learn.chatgpt.com/docs/projects#use-local-projects-for-folders-and-codebases)
3. Start a new **Codex** chat from that project. Check that the selected project or working folder is `my-portfolio`. This gives Codex a place to read your résumé and save your website. If Codex says it can’t find the file, check the folder in Finder or File Explorer, then check which folder the project is using. If you can’t find Codex after signing in, ask the facilitator to help you check access.

## 3. Paste this into the chat

Copy the whole box. If you have a reference URL, paste it at the end before sending.

```text
Help me turn the résumé in this folder into a one-page portfolio website.

Ask me whatever you need to understand what the site should feel like and what it should highlight. You can ask about personality, audience, or visual references when they would help. Invite me to share a screenshot, a URL, or a description if useful. If I say “surprise me,” choose a distinctive direction and explain it briefly. When you have enough to propose a good direction, move ahead with a short proposal for me to review.

Use any reference as inspiration for an original design. If you can’t open the URL, ask me for a screenshot or a description of what I like. Use my résumé as evidence and choose sections that suit my work. Leave out unsupported sections and application-only details. Show me the proposed copy and design direction before building, and check which personal details or contact links I want visible. If I selected the fictional sample, visibly label the site as a fictional demo and leave out contact actions.

After I approve, create the website files in a folder named portfolio. Put the page and its text in index.html, the design in styles.css, and any necessary interactions in script.js. Use clear names, consistent indentation, and readable formatting. Keep the original résumé and reference files outside the website folder.

Make the complete page work by double-clicking index.html in a browser. Use relative paths for styles, scripts, and local images. Use plain HTML and CSS and a classic script tag if needed. Avoid JavaScript modules, fetch calls for local content, a build step, or a server. Use responsive layouts and check links, keyboard access, and readability.

Check the actual file in a browser if available and tell me which file to open. If you could only inspect the code, say so and tell me how to check it myself. Keep this local. I’ll handle Git and publishing separately if I choose to publish.
```

Answer in everyday language. “I want it to feel like a field notebook, and I want my research to come first” is enough to start. When Codex proposes the copy and direction, check names, dates, claims, and contact details. Ask for changes or tell it to build.

## 4. Open your website

1. In Finder or File Explorer, open **Documents → my-portfolio → portfolio**.
2. Double-click `index.html`. Your browser should show the designed page. If it opens in a text editor, right-click the file and choose **Open With**, then select Chrome, Edge, Safari, or Firefox.
3. Make the browser window narrow to check the layout. Click the links and look for missing images or information you meant to keep private.

If the page has no styling or an image is missing, leave the files together and tell Codex what you see. Ask it to check the file names and relative paths using the directly opened page.

## 5. Make a change

Return to the same chat and paste this prompt. Replace the bracketed text with what you want.

```text
Update my existing portfolio: [describe what you want to change].
If I added a new résumé, compare it with the current website and show me which facts would change before editing. Preserve the parts of the design and copy I didn’t ask to change. Keep the files readable and the page working by opening index.html directly. Tell me what changed and which file to open. Keep the edits local.
```

Refresh the browser after Codex saves its changes. Use **Cmd+R** on Mac or **Ctrl+R** on Windows. You have a working portfolio at this point.

## Optional. Give it a public address

Follow [Publish at your own GitHub Pages address](PUBLISH.md) for account setup, screenshots from GitHub’s guides, and the steps to publish and send later edits to the same address.
