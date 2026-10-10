import gradio as gr
from langchain_core.messages import HumanMessage

from relection_agent.graph import workflow


def run_agent(message, history):
    # The reflection agent works on one request at a time,
    # so we send only the new message (not the chat history).
    result = workflow.invoke([HumanMessage(content=message)])

    # The last message is the final, refined post.
    return result[-1].content


if __name__ == "__main__":
    demo = gr.ChatInterface(
        fn=run_agent,
        title="LinkedIn Post Agent",
        description="Ask for a LinkedIn post. The agent drafts it, critiques it, and refines it.",
    )
    demo.launch()