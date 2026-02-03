---
command: expense-report-docs
description: Generate and maintain comprehensive documentation from code, keeping it in sync with the implementation
argument-hints:
  - --api
  - --readme
  - --check
  - --help
allowed-tools:
  - Bash(ls:*)
  - Bash(cat:*)
  - Bash(grep:*)
  - Bash(find:*)
---

# Expense Report Documentation Generator

This command generates and maintains project documentation directly from the codebase, ensuring documentation stays aligned with the current implementation.

---

## Usage Examples

### Basic documentation generation
```bash
/expense-report-docs
Generate API documentation
/expense-report-docs --api
Check documentation coverage
/expense-report-docs --check
Generate or update README
/expense-report-docs --readme
Help and options
/expense-report-docs --help
Supported Arguments
Argument	Description
--api	Generate API documentation from code
--readme	Generate or update README.md
--check	Validate documentation coverage
--help	Show usage information


Implementation Logic
1. Help Handling
If $ARGUMENTS contains help or --help:

Display usage information

Exit immediately

2. Parse Arguments
Parse documentation options from $ARGUMENTS:

--api

--readme

--check

Specific module or file paths (optional)

3. Check Existing Documentation
List existing markdown files (excluding dependencies):

find . -name "*.md" | grep -v node_modules | head -20
Check if README exists:

test -f README.md && echo "README exists" || echo "No README.md found"
Find Python files with docstrings:

find . -name "*.py" -exec grep -l '"""' {} \;
4. Generate Documentation
Extract inline documentation and docstrings

Generate markdown files for APIs or modules

Keep documentation structure consistent

Update existing files instead of duplicating content

Output
Updated or newly generated .md files

Optional README.md

Coverage feedback when using --check

