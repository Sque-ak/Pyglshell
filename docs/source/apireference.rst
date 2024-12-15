Classes
=======================

Classes serve as abstract structures of an object. For example, we have a class called ``Window``, and all objects of this class belong to the Window class. They have a main class, ``WindowManager``, which manages and composes these classes. This section will describe classes of this kind.

Window && WindowsManager
------------------------

These abstract classes describe windows and a window manager, which is needed for managing and composing windows. Thanks to these classes, we can access the main window manager and retrieve all currently open windows.

In the Window class, the methods ``run`` and ``on_init`` must be defined. They are necessary for initializing the window and executing specific actions or loops within it.

In the WindowsManager, you also need to define the methods ``create_window`` and ``destroy_window`` for managing windows within the manager. This way, it's not necessary to create a new class and pass it to the WindowManager; you can directly create and initialize an object from within the WindowManager according to the manager's specifications.

.. _RST Window:

Window
~~~~~~~~~~

Abstract class, main structure for windows.

By default: 
*************

* ``self._name = 'Window';``
* ``self._parent = self;``

Methods
**********

* ``get_manager():WindowManager`` - Returns the windows manager to which the current window belongs;
* ``is_exist(window: Window):bool`` - Checks if the window exists in the current window;
* ``is_windows_manager():bool`` - Checks if the current window is a windows manager, by default equals False;
* ``is_composite():bool`` - Checks if the current window is composite, by default equals False;
* ``set_nonexistant_name(window: Window, index = 1):Window`` - Sets a unique name for the window if the current name already exists. Return the window with new name.
* ``add(window: Window):None`` - Adds a window to the collection, ensuring it has a unique name. Sets the parent of the added window to the current window.
* ``remove(window: Window):None`` - Removes a specified window from the collection. If the window is found, it is deleted from the collection.
* ``get(name:str):Window`` - Retrieves a window by its name from the collection. If not found, the method attempts to retrieve it from child windows recursively.

Abstract Methods
****************

* ``on_init():None`` - This method is needed for initializing windows, such as certain parameters.

    Why can't parameters be initialized in ``__init__()``?

    For example, we want to obtain the window manager during initialization, but we created the object manually rather than through the windows manager. In this case, the `get_manager()` method is called during initialization, which refers to the parent and doesn't find the manager, resulting in self. To avoid this, we can first create the object, assign it to a specific window manager, and then initialize it.

* ``run():None`` - This method is needed for performing certain actions, and the manager can call it in a loop.

Properties
**********

**Public:**

* ``name:str`` - The name of the window;
* ``parent:Window`` - The parent of the window.;

**Protected:**

* ``_parent:Window`` - The name of the window;
* ``_name:str`` - The name of the window;
* ``_children: Dict[Window]`` - The children windows;


WindowsManager
~~~~~~~~~~~~~~~~~~~~

Abstract class, main structure for Windows Manager, composing window. The class inherits from the ``Window`` class.

* extends: :ref:`RST Window`

By default: 
*************

* ``is_windows_manager() = True;``
* ``is_composite() = True;``
* ``self._name = 'WindowsManager';``

Abstract Methods
****************

* ``create_window(name:str):Window`` - Creates a new window with the specified name.
* ``destroy_window(name:str):None`` - Destroys the window with the specified name.
