#verify_ssl=False
#https://api.coffeecloud.doop.works
#"X-API-Key": "rHlI-kXgf-Hk7Q"
from coffeecloud_rest_api_client import AuthenticatedClient
client = AuthenticatedClient(base_url="https://api.coffeecloud.doop.works", token="rHlI-kXgf-Hk7Q", verify_ssl=True)
from coffeecloud_rest_api_client.api.machine.home_call import sync_detailed as home_call
from coffeecloud_rest_api_client.api.machine.register_machine import sync_detailed as register_machine


res = home_call(client=client, x_api_key="rHlI-kXgf-Hk7Q")
print(res)