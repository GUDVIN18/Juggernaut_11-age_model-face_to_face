from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def data_server(server_name, server_address, server_port, 
                server_auth_token, server_max_process,
                process_backend_id, task_id, file_path, prompt):
    
    print(f'----------{file_path}-----------')

    print(f'----------{prompt}-----------')

    files = {
        "file": (f"image_{process_backend_id}.png", open(file_path, "rb")),
    }

    print(f'files ----------{files}-----------\n\n')
    

    inswapper_config_upscale = 2
    inswapper_config_codeformer_fidelity = 0.87

    data = {
        "server_name": server_name,
        "server_address": server_address,
        "server_port": server_port,
        "server_auth_token": server_auth_token,
        "server_max_process": server_max_process,
        # "user_tg_id": user_tg_id,
        "process_backend_id": process_backend_id,
        "inswapper_config_upscale": inswapper_config_upscale,
        "inswapper_config_codeformer_fidelity": inswapper_config_codeformer_fidelity,
        "task_id": task_id,
        "prompt": prompt,
        # "emoji": emoji,
        # 'original_photo_id': original_photo_id,

    }

    
    server_ip = server_address
    server_port = server_port

    print(server_ip, server_port)
    
    url = f"http://{server_ip}:{server_port}/get_data"
    
    try:
        res = requests.post(url, data=data, files=files)
        print(f"PRINT RES {res.content}\n\n\n")
        return res.content
    except requests.RequestException as e:
        print(f'Данные не переданы > {e}')


import uuid
print('name', __name__)
if __name__ == "__main__":
    data_server(server_name = "2xRTXA5000",
                server_address = "81.94.156.236",
                server_port = "8080",
                server_auth_token = 12345,
                server_max_process = 10,
                process_backend_id = uuid.uuid4(),
                task_id = 999,
                file_path = "/home/ubuntu/project/face_to_face_server/server_1/i.jpg",
                prompt = ''' 
A successful businessman in a luxurious setting, stylized art, a cartoon rich man in a brown suit, a wide cinematic plan, the New York skyline against a sunset background, floating diamonds, gold bubbles, bundles of money, luxury watches, keys to a sports car, a model of a private plane, golden bitcoin symbols, stock market charts going up, cups, premium champagne bottles, muted candles, silk curtains, rich interior, magical atmosphere, golden hour lighting, dreamy visualization of success, symbols of prosperity, digital art style, modern illustration, bright colors, glossy details
'''
                )