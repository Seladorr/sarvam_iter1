from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)
CORS(app)

# Load the free conversational model (DialoGPT-medium)
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# In-memory conversation storage (for demo purposes)
# In production, use a persistent store like Redis or a database.
conversations = {}

def generate_response(user_id, user_input):
    # Retrieve conversation history; if not found, initialize as empty list.
    conversation_history = conversations.get(user_id, [])
    
    # Append the new user input
    conversation_history.append(user_input)
    
    # Create the prompt by joining previous exchanges
    prompt = " ".join(conversation_history)
    
    # Tokenize the prompt
    input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
    
    # Generate response (extend prompt by up to 50 tokens)
    output_ids = model.generate(input_ids, max_length=input_ids.shape[1] + 50, pad_token_id=tokenizer.eos_token_id)
    
    # Decode generated tokens and extract the response part
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    response = generated_text[len(prompt):].strip()
    
    # Append the bot response to the conversation history
    conversation_history.append(response)
    conversations[user_id] = conversation_history
    
    return response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = data.get("user_id", "default")
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = generate_response(user_id, user_message)
    return jsonify({"response": response, "conversation": conversations[user_id]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
