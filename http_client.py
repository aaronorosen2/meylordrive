import requests

headers = { "Authorization" : "Token 324c476fb691f603a2ff7691f3f56cbce1c9661e79608a1cf75ce37d86d1c9f6"}


body = {
    "repo": "git@gitlab.com:a4496/django-zillow.git",
    "name": "AgentStat project service",
}
req = requests.post(
    "https://api.dreampotential.org/api/project-service",
     headers=headers,
    json=body)
print(req.status_code)
print(req.json())


body = {'value': "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDk2ZJWJ1vVtEoKDN8eXWUvJwOO2LDogqXsOBLXXrHKw5ULFXnmt5iFmDYZr5pAvh+scYANMxmvJIthoJpkBrtjy7NkcsriESrEcj1r8+GMIQCGdbXzo736ckJHfpnIUNiFei+m5TwZ/zT+Ehah00nUDrrwBlIqV87Iau3+WIdhvuan2aKVbybsXaDLT9xiJJbBrr8hMAk29hC3KOb59umkuNxWmo4OiUzo73/bvUY5tl8aOC9eX1kAkilId4t43fyNKRdcxy48Hu1SGFt6oKVpPzq2C9IUGnq21FBbmcnoLnGxRVQkoQuGhnG5u2N8KNRX5w8kzosQkX73bo7l6GMtc7LXMCVtlT2+kueex1GxoY0cfS6YtYku3GkSKK5OpXN6aXRfTLN+TSvZbF03BMEMJL6pUAIcoMpTeMjg9dfIHVVBMReZEzMRzxPV5YJlixZKnTMItxcasDVdMxUTbLEZ8g2nfwi/SSd4uBtPwEsF4Nrl+oWDqYtr27GRdkMvYw0= arosen@arosen-laptop"}
req = requests.post(
    "https://api.dreampotential.org/api/create-keypair", headers=headers, json=body)

print(req.json())
