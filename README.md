[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/BUCOMPAdvancedDevelopment/advanced-development-assignment-AhmedElatreby)

# Advanced development assignment

# Ahmed El-Atreby

Build your container image using Cloud Build, by running the following command from the directory containing the
Dockerfile:

```
gcloud builds submit --tag gcr.io/ad-project-328808/ad-project --project=ad-project-328808
```

Deploying to Cloud Run -- To deploy the container image use the following command:

```
gcloud run deploy --image gcr.io/ad-project-328808/ad-project --platform managed  --project=ad-project-328808

```

Use the Docker command to test locally

```
PORT=8080 && docker run -p 9090:${PORT} -e PORT=${PORT} IMAGE_URL
```