from langchain_core.prompts import PromptTemplate

template=""" 
you are a helpful assistant.

User level: {level}
Task: {task}
Give reponse accordingly.
"""
prompt=PromptTemplate(
    input_variables=["level","task"],
    template=template
)

final_prompt=prompt.format(
    level="beginner",
    task="Explain Python loops"
)

print(final_prompt)