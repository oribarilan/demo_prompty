from pathlib import Path

from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import AzureChatOpenAI
from langchain_prompty import create_chat_prompt  # type: ignore
from pydantic import BaseModel, Field


class ComebackabilityEvaluatorInput(BaseModel):
    roast: str = Field(description="The roast to evaluate.")


class ComebackabilityEvaluatorOutput(BaseModel):
    reason: str = Field(description="A concise explanation for the given score.")
    score: int = Field(description="A number from 1 to 5.")


class ComebackabilityEvaluator:
    def __init__(self, lm: AzureChatOpenAI) -> None:
        prompty_path = Path(__file__).parent / "comebackability_evaluator.prompty"
        prompt = create_chat_prompt(str(prompty_path))
        parser = PydanticOutputParser(pydantic_object=ComebackabilityEvaluatorOutput)
        self._chain = prompt | lm | parser

    def eval(self, combackability_input: ComebackabilityEvaluatorInput) -> ComebackabilityEvaluatorOutput:
        return self._chain.invoke({"roast": combackability_input.roast})
