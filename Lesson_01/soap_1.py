from zeep import Client, Settings
import yaml

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


def check_text(text):
    settings = Settings(strict=False)
    client = Client(data['wsdl_url'], settings=settings)
    result = client.service.checkText(text)[0]['s']
    return result