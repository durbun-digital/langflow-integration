## Getting Started

### 1. Install LangFlow

Visit [LangFlow Desktop](https://www.langflow.org/desktop) and download the LangFlow application. Follow the on-screen instructions to complete the installation and registration process.

![Generate LangFlow API Key](assets/generate-langflow-api-key.png)
*Example: generating an API key in LangFlow.*

---

### 2. Launch the LangFlow Application

After installing, open the LangFlow application. The graphical interface (GUI) will appear, allowing you to manage and run flows.
When you launch the application, it starts a **local server** listening on port `7860`.

![API Access Example](assets/api-access-example.png)
*Example: API access settings in LangFlow.*

---

### 3. Load a Flow

In the LangFlow GUI, go to the project page and click **Upload a Flow**. Select any `flow.json` file from the integration folders to import and run the flow.

---

### 4. Access the Flow via API

You can interact with the flow programmatically using the local API. Each flow has a unique Flow ID (e.g., `a8745b57-9454-48bc-82ea-f6688110a6c8`), which is randomly generated when the flow is created. Use this ID in the API request URL::

```bash
curl --request POST \
     --url 'http://localhost:7860/api/v1/run/a8745b57-9454-48bc-82ea-f6688110a6c8?stream=false' \
     --header 'Content-Type: application/json' \
     --header 'x-api-key: YOUR_LANGFLOW_API_KEY' \
     --data '{
         "output_type": "chat",
         "input_type": "chat",
         "input_value": "who are you",
         "session_id": "test"
     }'
```

> **Note:** Replace `YOUR_LANGFLOW_API_KEY` with the API key you created in the previous step.

Besides `curl`, you can also access the API through **Python** and **JavaScript** code snippets provided by LangFlow. In the GUI, click **Share → API Access** to view the example snippets.
