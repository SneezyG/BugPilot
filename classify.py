import openai
import os
from prompts import build_prompt
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_bug(title, description):
    prompt = build_prompt(title, description)
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    result = response.choices[0].message.content.strip()
    
    # Parse result (assumes JSON-style output in your prompt)
    try:
        tags_line = [line for line in result.splitlines() if line.startswith("Tags")][0]
        category_line = [line for line in result.splitlines() if line.startswith("Category")][0]
        summary_line = [line for line in result.splitlines() if line.startswith("Summary")][0]

        return {
            "tags": eval(tags_line.split(":")[1].strip()),
            "category": category_line.split(":")[1].strip(),
            "summary": summary_line.split(":")[1].strip()
        }
    except Exception as e:
        raise ValueError("Failed to parse LLM output.")
