**Objective**

These Python scripts allow to interact with the OpenAI API.
You can manipulate the main abstractions of the OpenAI model:

* Conversations
* Responses
* Inputs
* Items
* Vector Stores
* Files

**Requirements**

* Python installed on the machine running this application.
* Credentials for accessing the OpenAI API - you will need to singup to the [OpenAI portal](https://platform.openai.com). You will then be able to craete your credentials from within the portal.

**How to run this application**

* Copy the file `config-sample.py` to `config.py`.

* Edit `config.py` with your credentials and defaults.

* Each script has a number of mandatory parameters in strict order:
  
  | Script                                  | Parameter 1       | Parameter 2     | Parameter 3     | Purpose                                                  |
  | --------------------------------------- | ----------------- | --------------- | --------------- | -------------------------------------------------------- |
  | `cancel_model_response.py`              | `response_id`     |                 |                 | Cancel a Response running in the background              |
  | `create_conversation.py`                |                   |                 |                 | Create a new Conversation                                |
  | `create_image.py`                       | `model_id`        | `prompt`        |                 | Create an image based on the prompt description          |
  | `create_model_response.py`              | `conversation_id` | `model_id`      | `input_message` | Create a Response within a Conversation                  |
  | `create_text_item.py`                   | `conversation_id` | `input_message` |                 | Create a user input or instruction within a Conversation |
  | `create_vector_store.py`                |                   |                 |                 | Create a Vector Store                                    |
  | `create_vector_store_file.py`           | `vector_store_id` | `file_id`       |                 | Create a File in a Vector Store                          |
  | `delete_conversation.py`                | `conversation_id` |                 |                 | Delete a Conversation                                    |
  | `delete_file.py`                        | `file_id`         |                 |                 | Delete a File                                            |
  | `delete_item.py`                        | `conversation_id` | `item_id`       |                 | Delete an Item (input or Response) from a Conversation   |
  | `delete_model_response.py`              | `response_id`     |                 |                 | Delete a Response                                        |
  | `delete_vector_store.py`                | `vector_store_id` |                 |                 | Delete a Vector Store                                    |
  | `delete_vector_store_file.py`           | `vector_store_id` | `file_id`       |                 | Delete a File from a Vector Store                        |
  | `list_files.py`                         |                   |                 |                 | List all uploaded Files                                  |
  | `list_input_items.py`                   | `response_id`     |                 |                 | List all input Items used to generate a Response         |
  | `list_items.py`                         | `conversation_id` |                 |                 | List all Items (inputs or Responses) in a Conversation   |
  | `list_vector_store_files.py`            | `vector_store_id` |                 |                 | List all Files in a Vector Store                         |
  | `list_vector_stores.py`                 |                   |                 |                 | List all Vector Stores                                   |
  | `modify_vector_store.py`                | `vector_store_id` | `metadata`      |                 | Update a Vector Store metadata                           |
  | `retrieve_conversation.py`              | `conversation_id` |                 |                 | Retrieve a Conversation                                  |
  | `retrieve_file.py`                      | `file_id`         |                 |                 | Retrieve a File                                          |
  | `retrieve_file_content.py`              | `file_id`         |                 |                 | Retrieve the content of File                             |
  | `retrieve_item.py`                      | `conversation_id` | `item_id`       |                 | Retrieve an Item from a Conversation                     |
  | `retrieve_model_response.py`            | `response_id`     |                 |                 | Retrieve a model Response                                |
  | `retrieve_vector_store.py`              | `vector_store_id` |                 |                 | Retrieve a Vector Store                                  |
  | `retrieve_vector_store_file.py`         | `vector_store_id` | `file_id`       |                 | Retrieve a File from a Vector Store                      |
  | `retrieve_vector_store_file_content.py` | `vector_store_id` | `file_id`       |                 | Retrieve the content of a File from a Vector Store       |
  | `update_conversation.py`                | `conversation_id` | `metadata`      |                 | Update a Conversation metadata                           |
  | `update_vector_store_file.py`           | `vector_store_id` | `file_id`       | `attributes`    | Update a File attributes                                 |
  | `upload_file.py`                        | `filename`        | `path-to-file`  |                 | Upload a File to the OpenAI platform                     |

* To execute these scripts run `python3 <script.py> <parameter_1> ...`.
