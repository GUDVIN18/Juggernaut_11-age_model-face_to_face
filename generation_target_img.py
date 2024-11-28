from diffusers import StableDiffusionPipeline, DiffusionPipeline, DPMSolverMultistepScheduler
import torch
from huggingface_hub import login
from random import randint

login("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")

# # def create_pipeline():
# #     # model_path = "SG161222/Realistic_Vision_V6.0_B1_noVAE"
# #     # model_path = "RunDiffusion/Juggernaut-X-v10"
# #     model_path = "SG161222/RealVisXL_V4.0"
# #     pipe = DiffusionPipeline.from_pretrained(
# #         model_path,
# #         torch_dtype=torch.float16,
# #         use_safetensors=True,
# #         safety_checker=None,
# #         variant="fp16"
# #     )
# #     pipe = pipe.to("cuda")

# #     pipe.scheduler = DPMSolverMultistepScheduler.from_config(
# #         pipe.scheduler.config, 
# #         use_karras_sigmas=True
# #     )
    
# #     pipe.enable_model_cpu_offload()
# #     return pipe

# def generate_image(prompt):
#     model_path = "RunDiffusion/Juggernaut-X-v10"
#     pipe = DiffusionPipeline.from_pretrained(
#             model_path,
#         ).to("cuda")
#     params = {
#         "prompt": prompt,
#         "height": 768,
#         "width": 512,
#         "num_inference_steps": 25,
#         "guidance_scale": 3.5
#     }
        
#     image = pipe(**params).images[0]
#     path = f"/home/ubuntu/project/face_to_face_server/server_1/media/jugernaut_xl/{randint(100000000000, 9999999999999)}.png"
#     image.save(path)
#     return path




import torch
from diffusers import DiffusionPipeline

def generate_image(prompt):
    # Распределение моделей между двумя GPU
    model_path = "RunDiffusion/Juggernaut-XI-v11"
    pipe = DiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
    ).to('cuda')




    n_promt = '''
photorealistic, hyperrealistic, low quality, blurriness, noise, distortion, poor anatomy, poor proportions, poor textures, amateur drawing, children's drawing, oversaturated, dark lighting, dim colors, poor composition, poor perspective, deformed face'''
    
    params = {
        "prompt": prompt,
        "negative_prompt": n_promt,
        "height": 768,
        "width": 512,
        "num_inference_steps": 40,
        "guidance_scale": 7.5
    }
    
    # Временное переключение между GPU для разных этапов генерации

    image = pipe(**params).images[0]
    
    path = f"/home/ubuntu/project/face_to_face_server/server_1/media/jugernaut_xl/{randint(100000000000, 9999999999999)}.png"
    image.save(path)
    return path



# if __name__ == "__main__":
#     t = generate_image(prompt="A 19 year-old man in a NASA astronaut suit, without the helmet, standing on the ground., 8k")
#     print(t)









# import requests
# from PIL import Image
# from io import BytesIO
# import base64
# from random import randint



# def generate_image(prompt):
#     url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    
#     payload = {
#         "prompt": prompt,
#         "steps": 20,
#         "width": 512,
#         "height": 768,
#         "cfg_scale": 7,
#         "override_settings": {
#             "sd_model_checkpoint": "/home/ubuntu/project/stable-diffusion-webui/models/Stable-diffusion/Juger_XL.safetensors"
#         }
#     }
    
#     response = requests.post(url, json=payload)
#     r = response.json()
    
#     # Decode base64 image
#     image = Image.open(BytesIO(base64.b64decode(r['images'][0])))
#     save_path = f"/home/ubuntu/project/face_to_face_server/server_1/media/SD/{randint(100000000, 9999999999)}.png"
#     image.save(save_path)
#     return save_path



