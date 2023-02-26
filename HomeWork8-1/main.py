import configuration.messages as messages
import user_interface as interface

print(f'\n{messages.MSG1.center(len(messages.MSG8))}\n{messages.MSG8}')

def invitation():
    interface.programm_action_choice()

invitation()