from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app = Flask(__name__, template_folder='templates')

# Загрузка локальной модели и токенизатора
model_path = "./local_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Создание пайплайна с локальной моделью
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    
    # Подсказка для модели
    prompt = f"Ответь на русском: {user_input}"
    
    response = chatbot(prompt, max_length=50, num_return_sequences=1)
    return jsonify({"response": response[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
