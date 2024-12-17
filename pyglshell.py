import random, pyglet
from utils.components.window import ComponentWindowsManager
from utils.components.layout import ComponentBorderStack
from utils.types.t_vectors import SVEC2, VEC2
from utils.types.t_colors import RGB

def window(b_maximize=True, icon='static/favicon.ico', *args, **kwargs):
    '''
    
    '''
    
    '''
    Description:
    w_*** - windows objects.
    '''
    
    windows_manager = ComponentWindowsManager(*args, **kwargs)
    windows_manager.layout = ComponentBorderStack()
    w_tools = windows_manager.create_window(anchor='north')
    w_tools_file_manager = windows_manager.create_window(anchor='east')
    w_status= windows_manager.create_window(anchor='south')
    w_object_observer = windows_manager.create_window(anchor='west')
    w_viewer = windows_manager.create_window(anchor='center')

    # w_tools.background_color = RGB(255,10,50)
    # w_tools_file_manager.background_color = RGB(10,255,50)
    # w_status.background_color = RGB(150,255,0)
    windows_manager.layout.on_init()

    if (b_maximize):
        windows_manager.window.maximize()

    if (not icon == ''):
        windows_manager.window.set_icon(pyglet.resource.image(icon))

    windows_manager.on_init()
    windows_manager.run()


if __name__ == "__main__":
    subtitle = random.choice([
        'Why did the developer become so poor? Because he cleared his cache.', 
        'Why do Java developers wear glasses? They can’t C#.',
        'How many programmers does it take to change a lightbulb? None, it’s a hardware problem.',
        'Have you heard of that new band “1023 Megabytes”? They’re pretty good, but they don’t have a gig just yet.',
        'There are 10 types of people in the world: those who understand binary, and those who don’t.',
        'I joined a support group for former computer hackers: Anonymous Anonymous.',
        'My internet router is in my basement. You could say that I come from a LAN down under.',
        'An SQL query goes into a bar, walks up to two tables, and asks, “Can I join you?”',
        'I’d love to give the man who invented incognito mode a cookie. Sadly, it was erased.',
        'Why do most programmers use a dark theme while coding? Because light attracts bugs.',
        'I get anxious whenever I have to use the default Microsoft web browser. Using Chrome helps take the Edge off.',
        'There’s no place like 127.0.0.1',
        'What’s it called when it takes you a while to find RAM for your computer? Short-term memory loss.',
        'Why does task manager use the phrase “kill the application”? Because they are all executable!',
        'Why does x86 have so many instructions? Because having too few would be RISC-y.',
        'Why was the IT guy in the hospital? He touched the firewall.',
        'Where do naughty disk drives get sent? Boot camp.',
        'Why do programmers never run the AC? They prefer to open windows.',
        'Where does the USA keep its backups? USB.',
        'My mother asked if I could change the DNS server settings. I told her ICANN.'
        ]) # These puns are taken from: https://www.atera.com/blog/a-compilation-of-best-it-puns/
    window(resizable=True, caption='Pyglshell - ' + subtitle)
   
