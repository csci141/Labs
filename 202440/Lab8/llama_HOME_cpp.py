# Logan Sizemore
# November 4, 2023
# Mock class to simulate Llama_cpp API. For students to test their program at home without access to the Llama model.
from typing import List, Generator, Any, Optional
import time
import logging

class Llama():
    """A mock class to simulate a text completion model."""
    
    def __init__(self, model_path: str, *args, **kwargs):
        """Initialize the Llama model with a given path."""
        self.model_path = model_path

    def __call__(self, text: str, max_tokens: int = 10, stop: Optional[List[str]] = None, stream: bool = False) -> Any:
        """
        Generate a text completion or return a streaming generator for text completion.
        
        Parameters:
        - text: The input text to complete.
        - max_tokens: The maximum number of tokens to generate.
        - stop: Optional list of stop words.
        - stream: Flag to determine if the response should be streamed.
        
        Returns:
        - A dictionary with the completion result, or a generator if stream is True.
        """
        if stop is None:
            stop = []

        return_text = (
            "You are using the debug version of Llama_cpp for CSCI 141 at WWU.\n\n" +
            "This line is here to similate a new line token. If you see this, then you did not include '\\n' as string in your stop list.\n" +
            "### This line is here for the '#' token. If you see this, then you did not include the '#' in your stop list"
        )
        
        if not stream:
            # Simulate a processing delay
            time.sleep(1)
            return self._generate_response(return_text, text, max_tokens, stop)
        else:
            return self._stream_response(return_text, max_tokens, stop)

    def _generate_response(self, return_text: str, text: str, max_tokens: int, stop: List[str]) -> dict:
        """Generate a non-streaming text completion response."""
        stop_index = -1  # Initialize with a value indicating no stop condition has been met
        for stop_substring in stop:
            stop_index = return_text.find(stop_substring)
            if stop_index != -1:
                return_text = return_text[:stop_index]
                break
        
        return_text = return_text[:max_tokens]  # To simulate the max_tokens behavior.

        return {
            'id': 'cmpl-79bd65c0-180f-46d7-84c3-51c012ee6e3f',
            'object': 'text_completion',
            'created': int(time.time()),
            'model': self.model_path,
            'choices': [{
                'text': return_text,
                'index': 0,
                'logprobs': None,
                'finish_reason': 'length'
            }],
            'usage': {
                'prompt_tokens': len(text),
                'completion_tokens': max_tokens,
                'total_tokens': len(text) + max_tokens
            }
        }

    def _stream_response(self, return_text: str, max_tokens: int, stop: List[str]) -> Generator[dict, None, None]:
        """Generate a streaming text completion response."""
        generated_tokens = 0
        current_text = ''

        for token in return_text:
            if generated_tokens >= max_tokens:
                break

            current_text += token
            generated_tokens += 1

            stop_condition_met = any(current_text.endswith(stop_string) for stop_string in stop)
            if stop_condition_met:
                break

            # Simulate a streaming delay
            time.sleep(0.1) 
            yield {
                'id': 'cmpl-894cc983-5fa6-4685-bfb1-582a9b472deb',
                'object': 'text_completion',
                'created': int(time.time()),
                'model': self.model_path,
                'choices': [{
                    'text': token,
                    'index': 0,
                    'logprobs': None,
                    'finish_reason': 'length'
                }]
            }

def main():
    # Tests
    logging.basicConfig(level=logging.INFO)
    llm = Llama(model_path="path/to/model")
    result = llm("sample text")
    logging.info(f"Non-streaming result: {result}")

    stop_phrases = ['\n', '#']  # Example stop phrases
    result = llm("sample text", stop=stop_phrases)
    logging.info(f"Non-streaming result (stop words): {result}")

    stream = llm("sample text", stream=True)
    logging.info("Streaming result:")
    for token in stream:
        logging.info(token)

    stop_phrases = ['\n', '#']  # Example stop phrases
    stream = llm("sample text", max_tokens=10, stop=stop_phrases, stream=True)
    logging.info("Streaming result (stop words):")
    for token in stream:
        logging.info(token)


if __name__ == "__main__":
    main()
