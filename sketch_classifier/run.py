import http.client, urllib.request, urllib.parse, urllib.error, base64

training_key = "976d352470b24c4db45c7d6d65b9620f"
projectId = "sketch_classifier"
tagIds = 'dog'
file_path = 'dog.0.png'

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Training-key': training_key
}

params = urllib.parse.urlencode({
    # Request parameters
    # 'tagIds': '{array}',
    'tagIds': tagIds
})

try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    # conn.request("POST", "/customvision/v1.0/Training/projects/{projectId}/images/image?%s" % params, "{body}", headers)

    with open(file_path, 'rb') as f:
        data = f.read()
    conn.request("POST", "/customvision/v1.0/Training/projects/{0}/images/image?{1}".format(projectId, params),
        body=data, headers=headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))