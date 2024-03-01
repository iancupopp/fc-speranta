import os
import random
from grazie.api.client.gateway import AuthType, GrazieApiGatewayClient, GrazieHeaders
from grazie.api.client.chat.prompt import ChatPrompt
from grazie.api.client.endpoints import GrazieApiGatewayUrls
from grazie.api.client.profiles import Profile

token = open("token.txt", "r").read()

# In a real application, you would have to supply the client's IP address
client_ip = "{}.{}.{}.{}".format(*[str(random.randint(0, 255)) for octet in range(4)])
client = GrazieApiGatewayClient(
    url=GrazieApiGatewayUrls.STAGING,
    grazie_jwt_token=token,
    auth_type=AuthType.APPLICATION,
)
response = client.chat(
    chat=(
        ChatPrompt()
        .add_system("You are a helpful assistant.")
        .add_user("Who won the world series in 2020?")
    ),
    profile=Profile.OPENAI_GPT_4,
    headers={
        GrazieHeaders.ORIGINAL_USER_IP: client_ip,
    }
)
print(response.content)
