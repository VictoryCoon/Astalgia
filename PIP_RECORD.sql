-- PIP INSTALL LIST HISTORY

python.exe -m pip install --upgrade pip

pip install bs4
pip install jinja2
pip install dotenv
pip install requests
pip install fastapi[all]
pip install python-multipart
pip install uvicorn[standard]

pip install google-genai
pip install google-generativeai
pip install google-auth-httplib2
pip install google-auth-oauthlib
pip install google-cloud-aiplatform

pip install faiss-cpu

pip install langchain
pip install langchain_community

gcloud projects add-iam-policy-binding astalgia --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" --role="roles/aiplatform.user"