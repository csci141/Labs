# Dion Udokop
# November 4, 2024
# Test class to simulate a llama_cpp API. Students use this to generate responses without needing to knowledge on dictionaries.
import time

class Llama:
    '''
    A mock class to simulate an llm model.
    '''
    def __init__(self, model_path="", verbose=False, n_ctx=2048):
        self.response_index = 0

        self.responses = [
            "I have no information about that topic.",
            "Really, I know nothing.",
            "Seriously."
        ]

    def __call__(self, text: str, max_tokens: int = 10, stop: [] = None, stream: bool = False) -> str: # type: ignore
        '''
        Simulates a streaming generator for responses to user input
        
        Parameters:
        - text: The input text to complete.
        - max_tokens: The maximum number of tokens to generate.
        - stop: Optional list of stop words.
        - stream: Flag to determine if the response should be streamed.
        '''
        response_text = self.responses[self.response_index]

        # increment response index to go to the next response
        self.response_index = (self.response_index + 1) % len(self.responses)

        # simulate streaming each word in the response
        # print each token with a slight delay to mimic streaming
        tokens = response_text.split()
        for token in tokens:
            time.sleep(0.1)
            yield token + " "
