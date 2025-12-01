# hellO_Ollama

![img_llama](llama.png)
*image generated with nano banana pro*

This is a tiny playground for talking to **local LLMs with Ollama** from Python.

This is **Phase 1** of my pAgeNt (personal agent) experiments: just get comfy with:
- running models locally via Ollama, and  
- calling them from Python (notebook + simple chat loop)

Currently tested with `gemma3:1b` and `phi3` (but works with any Ollama model you’ve pulled).

## Features

**Local-first LLM chat**

- Uses [Ollama](https://ollama.com/) as the local model runtime.
- Simple Python client calls with `ollama.chat`.

**Notebook playground**

- `ollama_playground.ipynb` (or similar) shows:
- Loading a small model
- Single-turn chat calls
- Playing with `temperature` and `num_predict` (max new tokens)
- Optional streaming vs non-streaming responses

**Streaming chat loop (CLI)**

- `chat_loop_with_log.py`:
- Stateful conversation (keeps `history` of messages)
- Streaming tokens to the terminal as they are generated
- Simple exit commands: `exit`, `quit`, `\q`

**Conversation logging**

- Each chat session is saved as a JSON file under `logs/`, e.g.:
    - `logs/chat_2025-11-30T16-12-03.123456.json`
- Logged fields:
    - `model`, `temperature`, `num_predict`
    - `started_at`, `ended_at`
    - `messages`: list of `{role, content, timestamp}`

This will be useful later for building and evaluating the actual pAgeNt agent.

## Project Structure

```text
hello-ollama/
├── README.md
├── requirements.txt          # Python dependencies (ollama, jupyter, etc.)
├── ollama_playground.ipynb   # Basic Ollama-from-Python playground
├── chat_loop.py              # Streaming chat loop
├── chat_loop_with_log.py     # Streaming chat loop + JSON logging
│
└── chat_logs/
    └── chat_*.json           # Saved conversation sessions
```

## Limitations & Future Ideas

Current limitations:
- No persistence beyond simple JSON logs (no RAG or vector search yet)
- No multi-model routing or tools, just “raw LLM chat”
- No evaluation / scoring of responses

Potential next steps (for future pAgeNt phases):
- Use logs as test conversations for agent evaluation
- Add a config file for switching models and parameters
- Wrap this in a small CLI or TUI with nicer UX
- Plug into an MCP server + basic tools (filesystem, web search, etc.)
- Build RAG over PDFs / notes and route queries through the local model
(we will go through all of that and more in future Phases)

## License

MIT License.

## Contact

For questions or suggestions, open an issue or reach out via GitHub: @0lekz

This repo is mainly a learning & playground project.
Feel free to fork it, hack on it, and adapt it to your needs.