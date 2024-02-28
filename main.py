from flask import Flask, request, jsonify
import streamlit as st


st.set_page_config("Webhook")

st.title("Webhook")
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Obtén el contenido del cuerpo de la solicitud POST
        request_data = request.get_data(as_text=True)
        print("Contenido de la solicitud POST:", request_data)

        return jsonify({"message": "Probando local"}), 200
    except Exception as e:
        print("Error al procesar la webhook:", str(e))
        return jsonify({"status": "error", "message": "Error al procesar la webhook"}), 500

app.run()
