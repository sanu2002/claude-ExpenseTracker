---

description: Quick git commit workflow 
allowed-tools: Bash(git:*), Bash(pytest:*)

---

#Quick Commit 

1. Refractor code 
2. Run tests:`pytest -v`
3. Update Readme.md 
4. If test pass:
  - Show status : `git status`
  - Stage all : `git add . `
  - Ask for commit -m "{message}"
  - Push: `git push `

6. Done 