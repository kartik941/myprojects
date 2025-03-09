from django.http import JsonResponse
from web3 import Web3
from django.conf import settings

# Connect to blockchain
web3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
contract = web3.eth.contract(address=settings.CONTRACT_ADDRESS, abi=settings.CONTRACT_ABI)


def get_storage(request):
    """Retrieve stored value from blockchain."""
    try:
        value = contract.functions.get().call()
        return JsonResponse({"value": value})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def set_storage(request):
    """Set a new value on the blockchain."""
    try:
        new_value = int(request.GET.get("value", 0))
        tx_hash = contract.functions.set(new_value).transact({"from": web3.eth.accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        return JsonResponse({"message": "Value updated", "transaction": tx_hash.hex()})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
