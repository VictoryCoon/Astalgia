-- PIP INSTALL LIST HISTORY

-- Python Version 3.13.x

python.exe -m pip install --upgrade pip

pip install bs4
pip install lxml
pip install jinja2
pip install dotenv
pip install requests
pip install gunicorn
pip install python-multipart
pip install uvicorn[standard]
pip install fastapi[all]

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

--git clone -b fastapi-deploy-google-cloud-platform https://github.com/VictoryCoon/Astalgia.git

-- AppEngine Settings
git clone https://github.com/VictoryCoon/Astalgia.git

virtualenv -V

virtualenv env

source env/bin/activate

pip freeze > requirements.txt

entrypoint: gunicorn -w 4 -k  uvicorn.workers.UvicornWorker -b 0.0.0.0:10000 app:app

--TXT 레코드
"google-site-verification=7bnIP9NjJUOz-Pug0SA4t15tPxpznmAQLEwJF9FHHPo"

gcloud app repair

gsutil iam ch allUsers:objectViewer gs://staging.astalgia.appspot.com


gcloud projects add-iam-policy-binding astalgia \
    --member="user:victorycoon@gmail.com" \
    --role="roles/owner"

gcloud projects add-iam-policy-binding astalgia \
  --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"

gcloud projects add-iam-policy-binding astalgia \
    --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding astalgia \
    --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding astalgia \
    --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" \
    --role="roles/cloudbuild.builds.editor"

gcloud projects add-iam-policy-binding astalgia \
    --member="serviceAccount:astalgia@astalgia.iam.gserviceaccount.com" \
    --role="roles/cloudbuild.builds.builder"

gcloud projects add-iam-policy-binding astalgia \
    --member="user:victorycoon@gmail.com" \
    --role="roles/iam.serviceAccountUser" \
    --condition="expression=resource.name == 'projects/astalgia/serviceAccounts/239136801275-compute@developer.gserviceaccount.com',title=AllowImpersonateComputeSA"

gcloud iam service-accounts add-iam-policy-binding projects/astalgia/serviceAccounts/astalgia@astalgia.iam.gserviceaccount.com \
    --member="serviceAccount:service-239136801275@gcp-sa-run.iam.gserviceaccounts.com" \
    --role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding astalgia \
  --member="serviceAccount:239136801275@cloudbuild.gserviceaccount.com" \
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding astalgia \
  --member="serviceAccount:239136801275@cloudbuild.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"

gcloud services enable run.googleapis.com --project=astalgia

gcloud iam service-accounts add-iam-policy-binding projects/astalgia/serviceAccounts/astalgia@astalgia.iam.gserviceaccount.com \
    --member="serviceAccount:service-239136801275@serverless-robot-prod.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountTokenCreator"

gcloud run deploy astalgia \
    --source . \
    --region asia-northeast1 \
    --platform managed \
    --allow-unauthenticated \
    --build-service-account=projects/astalgia/serviceAccounts/astalgia@astalgia.iam.gserviceaccount.com \
    --service-account=astalgia@astalgia.iam.gserviceaccount.com

/*
도메인 매핑은 다음 리전에서 사용할 수 있습니다.
asia-east1
asia-northeast1
asia-southeast1
europe-north1
europe-west1
europe-west4
us-central1
us-east1
us-east4
us-west1
*/