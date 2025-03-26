import cutie
single_file_mode = cutie.prompt_yes_or_no("is your setup single file?")

tokyonight = {
        "name": "tokyonight",
        "single_file_code": """{
  "folke/tokyonight.nvim",
  lazy = false,
  priority = 1000,
  opts = {},
}"""
    }

plugins = [tokyonight["name"]]

cutie.select(plugins)