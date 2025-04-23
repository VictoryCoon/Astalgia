import os
import vertexai
from vertexai.language_models import TextEmbeddingModel
from vertexai.preview.generative_models import GenerativeModel
from google.oauth2 import service_account

#GCP PROJECT INFO
KEY_PATH = os.path.abspath("C:/Astalgia/astalgia-63599d9916b4.json")
PROJECT_ID = "astalgia"     #239136801275
LOCATION = "us-central1"
#LOCATION = "asia-northeast3"   # 왜 안되는지 통 모르겠다.

#MODEL INFO
EMBBEDING_MODEL_NAME = "text-multilingual-embedding-002"
GEMINI_MODEL = "gemini-2.0-flash-001"
#GEMINI_MODEL = "gemini-2.0-flash-lite-001"


# Vertex AI API : AUTHENTICATION WITH CLOUD
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)

def QuestionAndAnswer(Q):
    chat_model = GenerativeModel(model_name=GEMINI_MODEL)
    response = chat_model.generate_content(Q)
    print(response.text)

    return response

def Embedding(Q):
    try:
        model = TextEmbeddingModel.from_pretrained(EMBBEDING_MODEL_NAME)
        embeddings = model.get_embeddings(Q)
        return embeddings
    except FileNotFoundError:
        print(f"Error - Key is not found - Path : '{KEY_PATH}'")
    except ValueError as e:
        print(f"Error: {e}")
        print("모델 이름 또는 리전을 확인하거나 라이브러리를 업데이트해 보세요.")
    except Exception as e:
        print(f"기타 오류 발생: {e}")