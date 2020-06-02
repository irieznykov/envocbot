answers = {
    '/start': {
        'new_user': 'Welcome!'
                    '\nThe list of the commands you can use:'
                    '\n- /new_list: creates a new list for today\'s date. After the new list has been created you can '
                    'add the new words into it. Just type one word per message. '
                    'Once you\'ve done type /save_list command.'
                    '\n- /save_list: saves the previously created list and makes it ready for notifications.'
                    '\n- /get_list: returns the created or saved list for today\'s date.'
                    '\n- /get_commands: returns the list of the commands you are able to use.',
        'old_user': 'Welcome back! '
                    '\nThe list of the commands you can use:'
                    '\n- /new_list: creates a new list for today\'s date. After the new list has been created you can '
                    'add the new words into it. Just type one word per message. '
                    'Once you\'ve done type /save_list command.'
                    '\n- /save_list: saves the previously created list and makes it ready for notifications.'
                    '\n- /get_list: returns the created or saved list for today\'s date.'
                    '\n- /get_commands: returns the list of the commands you are able to use.',
    },
    '/get_commands': 'The list of the commands you can use:'
                     '\n- /new_list: creates a new list for today\'s date. After the new list has been created you can '
                     'add the new words into it. Just type one word per message. '
                     'Once you\'ve done type /save_list command.'
                     '\n- /save_list: saves the previously created list and makes it ready for notifications.'
                     '\n- /get_list: returns the created or saved list for today\'s date.'
                     '\n- /get_commands: returns the list of the commands you are able to use.',
    '/new_list': {
        'existed': {
            'created': 'You already have an unsaved list, feel free to add the new words. '
                       'Keep in mind that each word should be typed as a new message',
            'saved': 'You already have a saved list for today\'s date.',
        },
        'not_existed': 'The list has been successfully created. Start typing the words you want to add into it. '
                       'Keep in mind the format - one word per message.'
    },
    '/save_list': {
        'existed': 'The list has been saved successfully.',
        'not_existed': 'There are no created but unsaved lists found for today\'s date.'
    },
}
