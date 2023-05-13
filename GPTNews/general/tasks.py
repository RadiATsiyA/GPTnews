import openai
from craiyon import Craiyon

from django.conf import settings

from general.models import Article
from general.forms import SuggestionForm


def send_prompt_to_chatgpt(theme):
    openai.api_key = settings.OPENAI_API_KEY
    prompt = f'Generate a fantastic news and write an article for 250 words, on topic "{theme}"'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300,
        temperature=1
    )
    return response


def send_prompt_to_craiyon(theme):
    generator = Craiyon()
    result = generator.generate(f"{theme}", negative_prompt="spoon", model_type="art")
    url = result.images.pop(0)
    return url


def send_prompt_to_chatgpt_and_craiyon_and_save_obj_and_get_id(theme: str) -> int:
    craiyon_response = send_prompt_to_craiyon(theme)
    chat_response = send_prompt_to_chatgpt(theme)

    article_obj = Article(name=theme, text=chat_response['choices'][0]['text'], image_url=craiyon_response)
    article_obj.save()
    return article_obj.id

