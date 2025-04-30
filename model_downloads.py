from transformers import AutoModelForCausalLM, AutoTokenizer

#model_name = "distilgpt2"
model_name = "sberbank-ai/rugpt3large_based_on_gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Сохранение модели и токенизатора локально
model.save_pretrained("./local_model")
tokenizer.save_pretrained("./local_model")
