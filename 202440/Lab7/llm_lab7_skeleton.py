#########################
#   TODO: import Llama  #
#########################

'''
llama(): Initializes and simulates a conversational loop with the mock Llama API.

This function initializes the Llama model, sets up an initial system message, 
and starts a loop to interact with the user. It takes user input, generates 
responses from the test API, and streams these responses one token at a time. 
The loop ends when the user types "quit".
'''
def llama():
    ####################################
    #   TODO: initialize the test API  #
    ####################################
    
    
    ########################################
    #   TODO: declare your system message  #
    ########################################
    
    
    ##############################################
    #   TODO: initialize your response variable  #
    ##############################################
    
    
    ############################################################
    #   TODO: initialize and complete the conversational loop  #
    ############################################################
    
    print("\n")


''' 
experienceDiary() allows you to reflect on and document your programming process.
This is meant to be filled out after you have completed this lab. Once your chatbot 
is working according to the lab 7 description, you will use it to complete this function.

Complete this by inserting your answers after colon.
'''        
def experienceDiary():
    
    #Q1 Please insert the system message you have designed for your chatbot.
    Q1 = "Q1: "
    
    #Q2 Explain the intended purpose and the expected impact of this message on user interaction. 
    # What were the primary considerations you had while crafting this message.
    Q2 = "Q2: "
    
    #Q3 Reflect on the ethical responsibilities in AI that your message addresses. 
    # How does your message contribute to the ethical use of AI in a conversational context?
    Q3 = "Q3: "
    
    #Q4 Describe any challenges you faced in creating an ethical and safe message, and the solutions 
    # you implemented. What did you learn from this process?
    Q4 = "Q4: "
    
    #Q5 Consider the potential impacts of your message on user interaction and perception. What positive or 
    # negative effects could your message have, and how have you mitigated the latter?
    Q5 = "Q5: "
    
    
    print("\n")
    print ("Reflection \n")
    print (Q1, "\n\n",Q2, "\n\n",Q3, "\n\n",Q4, "\n\n",Q5, "\n\n")


'''
main() runs the Llama chatbot and experience diary.
It calls the llama() to start the conversational loop and 
the experienceDiary() to print reflection responses.
'''
def main():
    llama()
    experienceDiary()


if __name__ == "__main__":
    main()
    
#END
