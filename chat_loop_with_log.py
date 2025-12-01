from datetime import datetime
import json
import os
import ollama

MODEL_NAME = "gemma3:1b"


def chat_loop(
    model: str = MODEL_NAME, temperature: float = 1.1, num_predict: int = 512
):
    history = []
    print(f"Starting chat with {model}. Type '\\exit', '\\q' or '\\quit' to quit.")

    session_start = datetime.now().isoformat()
    log = {
        "model": model,
        "temperature": temperature,
        "num_predict": num_predict,
        "started_at": session_start,
        "messages": [],
    }

    try:
        while True:
            try:
                user_input = input("> ")
            except (KeyboardInterrupt, EOFError):
                print("\nerror, ending chat...")
                break

            if user_input.strip().lower() in {"\\exit", "\\q", "\\quit"}:
                print("\n \\quit command, ending chat...")
                break

            now = datetime.now().isoformat()

            user_msg = {"role": "user", "content": user_input}
            history.append(user_msg)
            log["messages"].append(
                {
                    "role": "user",
                    "content": user_input,
                    "timestamp": now,
                }
            )

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
            assistant_msg = {"role": "assistant", "content": assistant_message}
            history.append(assistant_msg)

            now = datetime.now().isoformat()

            log["messages"].append(
                {
                    "role": "assistant",
                    "content": assistant_message,
                    "timestamp": now,
                }
            )

    finally:
        log["ended_at"] = datetime.now().isoformat()
        os.makedirs("chat_logs", exist_ok=True)

        safe_start = session_start.replace(":", "-")
        log_path = os.path.join("chat_logs", f"chat_{safe_start}.json")

        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(log, f, ensure_ascii=False, indent=4)

        print(f"chat log saved to {log_path}")


if __name__ == "__main__":
    chat_loop()
