import re
import long_responses as long
# import client as client


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks', 'thank you', 'great'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_BOOK, ['ride now', 'book', 'cab'], required_words=['book', 'cab'])
    response(long.R_BOOKLATER, ['ride later', 'prebook', 'book'], required_words=['later'])
    response(long.R_PLOC, ['pickup', 'set', 'location'], required_words=['pickup', 'location'])
    response(long.R_DLOC, ['destination', 'drop', 'set', 'location'], required_words=['drop', 'location'])
    response(long.R_TRACK, ['track', 'cab'], required_words=['track'])
    response(long.R_OTP, [ 'otp','OTP'], single_response=True)
    response(long.R_PAY, ['pay', 'payment'], single_response=True)
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    if response=="I don't quite understand, would you like to talk to a real person instead? ":
        print("Bot: I don't quite understand, would you like to talk to a real person instead? ")
        c=input('You: ')
        if c=="yes" or "Yes" or "YES":
            import client as client
        else:
            response="okay"
            return response
    else:
        return response


# Testing the response system
print("Bot: Hey there! i'm trained to assist you in all cab related queries to my knowledge\nAsk away!")
while True:
    print('Bot: ' + get_response(input('You: ')))
