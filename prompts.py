def build_prompt(title, description):
    return f"""
You are an AI that helps classify bug reports.

Given a bug title and description, return:
- Tags (as a Python list of strings, max 3)
- Category (e.g., backend, frontend, auth, UX, performance, infra)
- Summary (a one-line summary)

Bug Title: {title}
Bug Description: {description}

Format:
Tags: [...]
Category: ...
Summary: ...
"""
