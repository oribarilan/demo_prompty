from pathlib import Path

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import AzureChatOpenAI
from langchain_prompty import create_chat_prompt  # type: ignore


class Roaster:
    def __init__(self, lm: AzureChatOpenAI) -> None:
        prompty_path = Path(__file__).parent / "roaster.prompty"
        prompt = create_chat_prompt(str(prompty_path))
        self._chain = prompt | lm | StrOutputParser()

    def roast(self, text: str) -> str:
        return self._chain.invoke({"input": text})
