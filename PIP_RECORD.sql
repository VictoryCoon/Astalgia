-- PIP INSTALL LIST HISTORY

python.exe -m pip install --upgrade pip

pip install bs4 dotenv fastapi[all] uvicorn[standard] jinja2 python-multipart requests google-cloud-aiplatform google-generativeai google-genai google-auth-oauthlib google-auth-httplib2

gcloud projects add-iam-policy-binding astalgia --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" --role="roles/aiplatform.user"