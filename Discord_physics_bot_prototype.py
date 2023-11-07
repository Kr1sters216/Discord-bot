import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there, im a physics bot that will ask you questions, currently im a prototype that still needs alot of work.!'

    if p_message == 'roll':
        return str(random.randint(1, 12))

    if p_message == 'help':
        return 'Curently there are no help commands, the bot is still in development.'

    if p_message == 'Developers':
        return 'The current developers of this bot are, Emils Jansons, Roberts Višs, Kristers Jurģis.'

    return "I quite didnt understand your question, can you repeat it?"