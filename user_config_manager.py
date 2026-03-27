def add_setting(settings: dict, setting_pair: tuple):
    key, value = setting_pair
    
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        print(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        settings[key] = value
        print(f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(settings: dict, settings_pair: tuple):
    key, value=settings_pair
    key=key.lower()
    value=value.lower()

    if key in settings:
        settings[key]=value
        print(f'Setting {key} updated to {value} successfully!')
    else:
        print(f'Setting {key} does not exist! Cannot update a non-existing setting.')

def delete_setting(settings: dict, key):
    key=key.lower()

    if key in settings:
        del settings[key]
        print(f'Setting {key} deleted successfully!')
    else:
        print(f'Setting not found!')

def view_settings(settings: dict):
    if not settings: 
        print(f'No settings available')
    else:
        result='Current User Settings:'

        for key, value in settings.items():
            result+=f'\n{key.capitalize()}:{value}'
    
        print(result)

#testing dictionary

test_settings={
    'Theme':'dark',
    'Notifications': 'disabled',
    'Volume':'low'
}

add_setting({'theme': 'light'}, ('THEME', 'dark')) 
add_setting({'theme': 'light'}, ('volume', 'high'))  

update_setting({'theme': 'light'}, ('theme', 'dark'))
update_setting({'theme': 'light'}, ('volume', 'high'))

delete_setting({'theme': 'light'}, 'theme')



    

    