import shopify
import json

shop_creds = "shop_creds.json"

with open(shop_creds) as f:
    shop_creds = json.load(f)

merchant = 'https://dmstores-com-br.myshopify.com'

api_session = shopify.Session(merchant, '2022-04', shop_creds['api_token'])
shopify.ShopifyResource.activate_session(api_session)


def get_data(object_name):
    all_data=[]
    attribute=getattr(shopify, object_name)
    data=attribute.find(since_id=0, limit=250)
    for d in data:
        all_data.append(d)
    while data.has_next_page():
        data=data.next_page()
        for d in data:
            all_data.append(d)
    return all_data


dir(shopify)

