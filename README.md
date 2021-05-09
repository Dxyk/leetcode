# LeetCode

## Project Structure

```text
.
+-- Python
|   +-- TODOs
|   +-- utils
+-- .gitignore
+-- LICENSE
+-- README.md
```

## Python Solutions

### Dependencies

- Python version: 3.9.4
- Snippets
  - [LeetCode snippets](.vscode/LeetCode.code-snippets): use `main` or `test` for local testing snippet

## VSCode LeetCode Extension

Practiced using VSCode's [LeetCode extension](https://marketplace.visualstudio.com/items?itemName=shengchen.vscode-leetcode)

### Sign In using Cookie

To sign in using Cookies, use the following steps (see reference [here](https://github.com/LeetCode-OpenSource/vscode-leetcode/issues/478#issuecomment-564757098))

1. Install NodeJs version 8+ if necessary
2. Install latest LeetCode-CLI using npm

   ```sh
   # to remove the old version
   npm uninstall -g leetcode-cli
   # to install the up-to-date version(2.6.17+)
   npm install -g leetcode-tools/leetcode-cli
   ```

3. Log into [LeetCode](https://leetcode.com) in the browser and extract the cookie

   1. Open developer console
   2. Trigger any XHR request
   3. Copy entire `cookie` in request header

4. Input the cookie either
   1. In VSCode LeetCode plugin
   2. In Terminal with `leetcode user -c`
