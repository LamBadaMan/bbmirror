from app.dependencies.config import GIE_KEY
from gie import GiePandasClient

gieconnect = GiePandasClient(api_key=GIE_KEY)

def get_gie_client():
    return gieconnect