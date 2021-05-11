# LeetCode

## Dependencies

### Python

- Python version: 3.7.\*

  - Note: Python ^3.8.0 will break VSCode python intellisense and autocomplete, hence Python 3.7.\* (see [reference thread](https://github.com/microsoft/vscode-python/issues/9321#issuecomment-570038262))

### VSCode

- [VSCode LeetCode Extension](https://marketplace.visualstudio.com/items?itemName=shengchen.vscode-leetcode)

  - Allows opening LeetCode questions within VSCode
  - Generates files base on LeetCode Questions
  - See [VSCode LeetCode Extension Settings](#vscode-leetcode-extension-settings) for setup steps

- [Custom LeetCode snippets](.vscode/LeetCode.code-snippets)

  - Since VSCode Python extension removed snippets, added `main` and `test` for local testing

#### VSCode LeetCode Extension Settings

VSCode LeetCode extension requires user sign-in before it can be used. To do so, follow the steps bellow (see reference [here](https://github.com/LeetCode-OpenSource/vscode-leetcode/issues/478#issuecomment-564757098)).

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
   3. Copy entire `cookie` in Request Header

4. Input the cookie either
   1. In VSCode LeetCode plugin
   2. In Terminal with `leetcode user -c`
