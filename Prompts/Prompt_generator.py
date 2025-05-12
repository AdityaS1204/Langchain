from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    template= """
    please summarize the research paper titled "{paper_input}" with the following specifications:
explaination style:{style_input}
explaination length:{length_input}
1. Mathematical Details:
- include relevent mathematical equations if present in the paper.
- Explain mathematical concepts using simple , intuitive code snippets where aplicable.
2. analogies:
- use relatable analogies to simplify complex ideas.
If certain information is not avaliable in the paper respond with: "insuffcient Information available" instead of guessing.
insure that the summary provided is correct, acurate , clear and aligned with the provided style and length.
    """,
    input_variables=["paper_input","length_input","style_input"],
    validate_template=True
)

template.save('Prompt_Template.json')