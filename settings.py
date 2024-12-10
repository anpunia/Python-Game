from _vars import *

def pcs(var):
    x = var.split(".")
    parent = '.'.join(x[:-1])
    child = x[-1]
    return [eval(parent), child]

def create_entry(location, name, variables, copy = False):
    frame = tk.Frame(location)
    frame.pack()

    label = tk.Label(frame, text=name, font=("Arial", 8))
    label.pack(side=tk.LEFT)

    entries = []
    split_vars = []

    for i in range(len(variables)):
        split_var = pcs(variables[i])
        split_vars.append(split_var)
        entry = tk.Entry(frame, width=5)
        entry.pack(side=tk.LEFT)
        entries.append(entry)

    def command():
        for i in range(len(variables)):
            setattr(split_vars[i][0], split_vars[i][1], int(entries[i].get()))
            if name == "Window Size":
                screen.reset()

    button = tk.Button(frame, text="", width=1, height=1, padx=0, pady=0, command = command)
    button.pack(side=tk.RIGHT)

def create_slider(location, name, variable, bounds, default_value):
    frame = tk.Frame(location)
    frame.pack()
    label = tk.Label(frame, text=name, font=("Arial", 8))
    label.pack(side=tk.TOP)
    split_var = pcs(variable)
    def command(_):
        prev_scale = player[0].scale
        setattr(split_var[0], split_var[1], slider.get())
        if name == "Player Scale":
            player[0].pos.y -= player[0].scale - prev_scale

    slider = tk.Scale(frame, from_=bounds.x, to=bounds.y, orient=tk.HORIZONTAL,
                      resolution=0.000001, showvalue=False, length=200, width=10, command=command)
    slider.pack(side=tk.LEFT)
    slider.set(default_value)

    def button_command():
        prev_scale = player[0].scale
        setattr(split_var[0], split_var[1], default_value)
        slider.set(default_value)
        if name == "Player Scale":
            player[0].pos.y -= player[0].scale - prev_scale


    button = tk.Button(frame, text="", width=1, height=1, padx=0, pady=0,
                       command=button_command)
    button.pack(side=tk.RIGHT)

def create_toggle(location, name, variable):
    var = tk.BooleanVar()
    split_var = pcs(variable)
    toggle = tk.Checkbutton(location, text=name, variable=var, onvalue=True, offvalue=False,
                            command=lambda: setattr(split_var[0],split_var[1] , var.get()))
    toggle.pack()

def add_settings(tk, screen):
    menu_bar = tk.Menu(screen.root)
    settings_menu = tk.Menu(menu_bar, tearoff=0)

    window_settings = tk.Frame(screen.root)
    settings_menu.add_command(label="Window", command=lambda: [window_settings.place(x=10,y=10), window_settings.lift()])
    create_slider(window_settings,"Screen zoom", "screen.zoom", Vector2(0.1, 5), 1)
    create_entry(window_settings, "Window Size", ["screen.size.x", "screen.size.y"])
    close_window_settings = tk.Button(window_settings, text="Close", command=window_settings.place_forget)
    close_window_settings.pack()

    admin_settings = tk.Frame(screen.root)
    settings_menu.add_command(label="Admin", command=lambda: [admin_settings.place(x=10,y=10), admin_settings.lift()])
    create_slider(admin_settings,"Player Scale", "player[0].scale", Vector2(1, 100), 10)
    create_slider(admin_settings,"Player Speed","player[0].move_speed", Vector2(0, 5), 0.15)
    create_slider(admin_settings, "Jump Power","player[0].jump_power", Vector2(0, 5), 0.5)
    create_slider(admin_settings,"Gravity Power","player[0].gravity_power", Vector2(0, 0.05), 0.002)
    create_entry(admin_settings, "Teleport", ["player[0].pos.x", "player[0].pos.y"])
    create_toggle(admin_settings,"Infinite Jumps", "player[0].infinite_jumps")
    close_admin_settings = tk.Button(admin_settings, text="Close", command=admin_settings.place_forget)
    close_admin_settings.pack()

    menu_bar.add_cascade(label="Settings", menu=settings_menu)
    screen.root.config(menu=menu_bar)
