import cutie
single_file_mode = cutie.prompt_yes_or_no("is your setup single file?")
value_counter = 0
plugins = {
    "tokyonight": {
        "name": "tokyonight",
        "single_file": """
{
  "folke/tokyonight.nvim",
  lazy = false,
  priority = 1000,
  opts = {},
}
""",
    "multi_file": """
return {
  "folke/tokyonight.nvim",
  lazy = false,
  priority = 1000,
  opts = {},
}
"""     
    },
  "lualine": {
      "name": "lualine",
      "single_file": """
{
  'nvim-lualine/lualine.nvim',
  dependencies = { 'nvim-tree/nvim-web-devicons' }
}
""",
    "multi_file": """
return {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' }
}
"""
  }
}


selected = cutie.select(plugins)

def intructions(counter):
    for key, value in plugins.items():
        if counter == selected:
          if single_file_mode:
            print(value["single_file"])
          else:
             print(value["multi_file"])
        counter += 1
intructions(value_counter)