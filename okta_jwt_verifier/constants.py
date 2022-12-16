import os


# Default values described in technical design

MAX_RETRIES = os.environ.get('JWT_VERIFIER_MAX_RETRIES', 1)
MAX_REQUESTS = os.environ.get('JWT_VERIFIER_MAX_REQUESTS', 10)
REQUEST_TIMEOUT = os.environ.get('JWT_VERIFIER_REQUEST_TIMEOUT', 30)
LEEWAY = os.environ.get('LEEWAY', 120)


# Constant URLs used in error messages

DEV_OKTA = "https://developer.okta.com"
FINDING_OKTA_DOMAIN = ("%s/docs/guides/find-your-domain/overview" % DEV_OKTA)
GET_OKTA_API_TOKEN = ("%s/docs/guides/create-an-api-token/overview" % DEV_OKTA)
FINDING_OKTA_APP_CRED = ("%s/docs/guides/find-your-app-credentials/overview" % DEV_OKTA)


# Misc
ADMIN_DOMAINS = ('-admin.okta.com', '-admin.oktapreview.com', '-admin.okta-emea.com')
