    json_data = json.loads(response.text)
    return json_data['url']