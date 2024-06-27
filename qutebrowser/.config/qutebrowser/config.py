import catppuccin

config.load_autoconfig()

config.bind(',r', 'config-source') 
config.bind(',c', 'config-edit')

catppuccin.setup(c, 'macchiato', True)



c.editor.command = ["nvim", "{file}"]
