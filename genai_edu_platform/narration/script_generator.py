from langchain.llms import AzureOpenAI

def enhance_topic(topic):
    llm = AzureOpenAI(deployment_name="gpt-4", model_name="gpt-4")
    prompt = f"Please explain the following topic for students in an engaging way:\n\n{topic}"
    return llm(prompt)