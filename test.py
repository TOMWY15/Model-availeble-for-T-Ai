import google.generativeai as genai

genai.configure(api_key="AIzaSyAXD151RzFmZy17-C_xaDAs1n6y36vfPUo")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)