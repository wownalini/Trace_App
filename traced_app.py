from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

# Create the model
llm = ChatOpenAI(model="gpt-4o-mini")

# Three different prompts
prompts = [
    "What is the capital of France?",
    "Explain photosynthesis in one sentence.",
    "Write a short poem about a rainy day."
]

# Send each prompt and print the answer
for prompt in prompts:
    print(f"Prompt: {prompt}")
    response = llm.invoke(prompt)
    print(f"Answer: {response.content}")
    print("-" * 40)