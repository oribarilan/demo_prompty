from pprint import pprint

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from comebackability_evaluator.comebackability_evaluator import ComebackabilityEvaluator  # type: ignore
from langchain_openai import AzureChatOpenAI
from roaster.roaster import Roaster  # type: ignore

endpoint = "https://genai-w.openai.azure.com/"
deployment = "gpt-4o-mini"
api_version = "2024-05-01-preview"

token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")

lm = AzureChatOpenAI(
    azure_ad_token_provider=token_provider,
    azure_endpoint=endpoint,
    api_version=api_version,
    azure_deployment=deployment,
)

roaster = Roaster(lm=lm)

roast = roaster.roast("I have a soft spot for junk food. The cheaper & slizzier, the better.")

print(f"Roast:\n{roast}\n")

comebackability = ComebackabilityEvaluator(lm=lm).eval(roast)

print("Comebackability:\n")
pprint(comebackability.model_dump())
