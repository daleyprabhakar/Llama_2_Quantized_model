from ctransformers import AutoModelForCausalLM

model_path = "C:/Users/arpan.ghosh/Documents/Modulr/Teaching_Project/llama-2-7b-chat.Q4_K_M.gguf"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    model_type="llama",
    gpu_layers=0  # Run on CPU
)
response = model("Tell me a joke about AI.")
print(response)