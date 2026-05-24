# ⌨️ Human-Like Document Typer

A cross-platform Python script that simulates natural, organic human typing speeds [Claim 1]. Perfect for typing up text drafts in applications like Google Docs and Microsoft Word with a fully randomized typing cadence that looks completely human to version history trackers [Claim 1].

---

## 🚀 One-Command Installation Guide

Choose the command block below for your operating system. Open your terminal/command prompt, paste the text, and hit **Enter**.

### 🍏 For Mac Users
This single command downloads Python 3.14 directly from the official servers, installs it quietly in the background, configures your secure internet certificates, and installs the required typing library.

```bash
curl -O https://python.org && sudo installer -pkg python-3.14.5-macos11.pkg -target / && open "/Applications/Python 3.14/Install Certificates.command" && python3.14 -m pip install pyautogui --break-system-packages
```
*(Note: It will ask for your Mac user password to authorize the package setup installer in the background).*

### 🪟 For Windows Users
This command leverages Windows' built-in `winget` engine to fetch and install Python 3.14, configures your system environment variables, and configures the dependencies.

```cmd
winget install Python.Python.3.14 && pip install pyautogui
```

---

## 🛠️ How to Use It

1. Save your script code as **`automator.py`** in your project folder.
2. Open your terminal or text editor and run the file:
   * **Mac:** `python3.14 automator.py`
   * **Windows:** `python automator.py`
3. You will have exactly **5 seconds** to quickly switch windows and click your cursor inside your Google Doc or Word document page.
4. The system will safely begin typing out your paragraph character-by-character using randomized human pauses.

---

## 🚨 Emergency Safety Stop (Fail-Safe)

If your text script starts typing out of control or you need to shut it off early:
* **Slam your mouse pointer into any of the four extreme corners of your computer screen.**
* This instantly trips the automation's built-in hardwired security brake, crashing the execution process and restoring immediate manual typing control to your device layout.
