from .llm import *
from langgraph.graph import MessageGraph
from typing import List, Sequence, Annotated, TypedDict
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage
from .prompt import generation_prompt, reflection_prompt
# Initialize a predefined MessageGraph
graph = MessageGraph()


generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm
#route function to determine the next step based on the current state
def should_continue(state: List[BaseMessage]):
    print(state)
    print(len(state))
    print("----------------------------------------------------------------------")
    if len(state) > 6:
        return END
    return "reflect"
#first_node
def generation_node(state: Sequence[BaseMessage]) -> List[BaseMessage]:
    generated_post = generate_chain.invoke({"messages": state})
    return [AIMessage(content=generated_post.content)]
#second_node
def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflect_chain.invoke({"messages": messages})  # Passes messages as input to reflect_chain
    return [HumanMessage(content=res.content)]  # Returns the refined message as HumanMessage for feedback

graph.add_node("generate", generation_node)
graph.set_entry_point("generate")
graph.add_node("reflect", reflection_node)
graph.add_edge("reflect", "generate")
graph.add_conditional_edges("generate", should_continue)
workflow = graph.compile()
