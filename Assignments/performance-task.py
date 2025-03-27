import cutie
single_file_mode = cutie.prompt_yes_or_no("is your setup single file?")
i_counter = 0
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
    },
  "lualine": {
      "name": "lualine",
      "single_file": """
{
  'nvim-lualine/lualine.nvim',
  dependencies = { 'nvim-tree/nvim-web-devicons' }
}
"""
  }
}

for i, j in plugins.items():
    print(j["single_file"])

selected = cutie.select(plugins)