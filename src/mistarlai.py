import re
from mistralai import Mistral
from datetime import date

class MistrialAI:
    _prompt= ""

    def __init__(self,  api_key=str):
        
        # you can change the model id as per your requirement
        self.model_id = "mistral-small-latest"  

        self.client =  Mistral(api_key=api_key)

        # Initialize with an initial system message and a starting prompt for the conversation.
        self.history = [
            {"role": "system", "content": self._prompt},
        ]

    def chat(self,inputText: str )-> str:
        try:
            # take user input
            self.history.append({"role": "user", "content": inputText})
            
            # Call the mistral model to generate the next step in the conversation
            chat_response = self.client.chat.complete(
                model= self.model_id,
                messages = self.history
            )
            
            assistant_reply = chat_response.choices[0].message.content

            # Update the history with the assistant's response
            self.history.append({"role": "assistant", "content": assistant_reply})
            return assistant_reply
            
        
        except Exception as e:
            print("Error in booking confirmation process:", e)
            return "There was an error processing your request!"
