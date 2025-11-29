import ollama

MODEL_NAME = "phi3"  # You can change to another model if you have it pulled locally


def chat_loop(model=MODEL_NAME, temperature=1.1, num_predict=256):
    history = []
    print(f"Starting chat with {model}. Type 'exit' to quit.")

    while True:
        user_input = input("> ")
        if user_input.strip().lower() in {"exit", "\\q", "\\quit"}:
            print("ending chat...")
            break

        history.append({"role": "user", "content": user_input})

        stream = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            options={
                "temperature": temperature,  # try more randomness
                "num_predict": num_predict,
            },
            stream=True,
        )
        full = []
        for chunk in stream:
            content = chunk["message"]["content"]
            print(content, end="", flush=True)
            full.append(content)
        print()

        assistant_message = full[0][1]
        history.append({"role": "assistant", "content": assistant_message})
        # print(f"model: {assistant_message}")


chat_loop()
