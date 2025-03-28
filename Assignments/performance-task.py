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
"""
# Code inside string from https://github.com/folke/tokyonight.nvim
,
    "multi_file": """
return {
  "folke/tokyonight.nvim",
  lazy = false,
  priority = 1000,
  opts = {},
}
"""
# Code inside string from https://github.com/folke/tokyonight.nvim     
    },
  "lualine": {
      "name": "lualine",
      "single_file": """
{
  'nvim-lualine/lualine.nvim',
  dependencies = { 'nvim-tree/nvim-web-devicons' }
}
"""
# Code inside string from https://github.com/nvim-lualine/lualine.nvim
,
    "multi_file": """
return {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' }
}
"""
# Code inside string from https://github.com/nvim-lualine/lualine.nvim
  },
  "auto-pairs": {
     "name": "auto-pairs",
     "single_file": """
{
    'windwp/nvim-autopairs',
    event = "InsertEnter",
    config = true,
    opts = {}
}
"""
# Code inside string from  https://github.com/windwp/nvim-autopairs
,
"multi_file": """
return {
    'windwp/nvim-autopairs',
    event = "InsertEnter",
    config = true
    opts = {}
}
"""
# Code inside string from  https://github.com/windwp/nvim-autopairs
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