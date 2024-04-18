from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate,MessagesPlaceholder
import yaml


def order_prompt():
    with open('tutorial/order.yaml', 'r', encoding='utf-8') as file:
        examples = yaml.safe_load(file)

    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{answer}"),
        ]
    )
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
        # output_parser = parser
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "you are a helpful assistant"
            ),
            few_shot_prompt,
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
    return final_prompt
def menu_prompt():
    with open('tutorial/menu.yaml', 'r', encoding='utf-8') as file:
        examples = yaml.safe_load(file)

    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{answer}"),
        ]
    )
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
        # output_parser = parser
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "you are a helpful assistant"
            ),
            few_shot_prompt,
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
    return final_prompt

def main_prompt():
    with open('tutorial/main.yaml', 'r', encoding='utf-8') as file:
        examples = yaml.safe_load(file)

    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{answer}"),
        ]
    )
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
        # output_parser = parser
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "few_shot_prompt의 내용에 따라서 답변하고 template answer에 벗어나게 대답하지 않는다. "
            ),
            few_shot_prompt,
            ("human", "{input}"),
        ]
    )
    return final_prompt