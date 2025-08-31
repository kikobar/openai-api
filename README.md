**Objective**

These Python scripts allow to interact with the OpenAI API.
You can manipulate the main abstractions of the OpenAI model:

* Conversations
* Responses
* Inputs
* Items

**Requirements**

* Python installed on the machine running this application.
* Credentials for accessing the OpenAI API - you will need to singup to the [OpenAI portal](https://platform.openai.com). You will then be able to craete your credentials from within the portal.

**How to run this application**

* Copy the file `config-sample.py` to `config.py`.
* Edit `config.py` with your credentials and defaults.
* Each script has a number of mandatory parameters in strict order:
| Script                       | Parameter 1       | Parameter 2     | Parameter 3     | Purpose                                                  |
| ---------------------------- | ----------------- | --------------- | --------------- | -------------------------------------------------------- |
| `cancel_model_response.py`   | `response_id`     |                 |                 | Cancel a Response running in the background              |
| `create_conversation.py`     |                   |                 |                 | Create a new Conversation                                |
| `create_model_response.py`   | `conversation_id` | `model_id`      | `input_message` | Create a Response within a Conversation                  |
| `create_text_item.py`        | `conversation_id` | `input_message` |                 | Create a user input or instruction within a Conversation |
| `delete_conversation.py`     | `conversation_id` |                 |                 | Delete a Conversation                                    |
| `delete_item.py`             | `conversation_id` | `item_id`       |                 | Delete an Item (input or Response) from a Conversation   |
| `delete_model_response.py`   | `response_id`     |                 |                 | Delete a Response                                        |
| `list_input_items.py`        | `response_id`     |                 |                 | List all input Items used to generate a Response         |
| `list_items.py`              | `conversation_id` |                 |                 | List all Items (inputs or Responses) in a Conversation   |
| `retrieve_conversation.py`   | `conversation_id` |                 |                 | Retrieve a Conversation                                  |
| `retrieve_item.py`           | `conversation_id` | `item_id`       |                 | Retrieve an Item from a Conversation                     |
| `retrieve_model_response.py` | `response_id`     |                 |                 | Retrieve a model Response                                |
| `update_conversation.py`     | `conversation_id` | `metadata`      |                 | Update a Conversation metadata                           |
* To execute these scripts run `python3 <script.py> <parameter_1> ...`.

