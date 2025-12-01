import ollama

MODEL_NAME = "phi3"  # You can change to another model if you have it pulled locally


def chat_loop(model=MODEL_NAME, temperature=1.1, num_predict=512):
    history = []
    print(f"Starting chat with {model}. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("> ")
        except (KeyboardInterrupt, EOFError):
            print("\nending chat...")
            break

        if user_input.strip().lower() in {"exit", "\\q", "\\quit"}:
            print("ending chat...")
            break

        history.append({"role": "user", "content": user_input})

        stream = ollama.chat(
            model=model,
            messages=history,
            options={
                "temperature": temperature,  # try more randomness
                "num_predict": num_predict,
            },
            stream=True,
        )
        full_chunks = []
        print(f"{model}: ", end="")
        for chunk in stream:
            content = chunk["message"]["content"]
            print(content, end="", flush=True)
            full_chunks.append(content)
        print()

        assistant_message = "".join(full_chunks)
        history.append({"role": "assistant", "content": assistant_message})


if __name__ == "__main__":
    chat_loop()
