import os

print("Current files:", os.listdir())
print("Model folder:", os.listdir("model") if os.path.exists("model") else "No model folder")