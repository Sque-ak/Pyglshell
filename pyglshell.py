from components.window import ComponentWindowsManager 

def make_window(*args, **kwargs):
    windows_manager = ComponentWindowsManager(*args, **kwargs)
    windows_manager.create_window()
    windows_manager.on_init()
    windows_manager.run()

if __name__ == "__main__":
    make_window(width=512, height=512)