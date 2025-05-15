-- PIP INSTALL LIST HISTORY

-- Python Version 3.13.x

python.exe -m pip install --upgrade pip

pip install bs4
pip install lxml
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
pip install --upgrade google-cloud-aiplatform

pip install faiss-cpu

pip install langchain
pip install langchain_community

gcloud projects add-iam-policy-binding astalgia --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" --role="roles/aiplatform.user"

gcloud auth login

gcloud config set account ${GOOGLE_CLOUD_ACCOUNT}

gcloud projects add-iam-policy-binding astalgia \
    --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" \
    --role="roles/aiplatform.admin"

gcloud projects remove-iam-policy-binding astalgia \
    --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" \
    --role="roles/aiplatform.admin"

gcloud dns managed-zones describe astalgia

watch dig astalgia.com @ns-cloud-d1.googledomains.com
watch dig astalgia.com @ns-cloud-d2.googledomains.com
watch dig astalgia.com @ns-cloud-d3.googledomains.com
watch dig astalgia.com @ns-cloud-d4.googledomains.com

watch dig +short NS astalgia.com