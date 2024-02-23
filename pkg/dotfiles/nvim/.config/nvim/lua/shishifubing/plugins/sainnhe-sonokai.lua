return {
    "sainnhe/sonokai",
    lazy = false,
    priority = 1000,
    enabled = true,
    config = function()
        vim.g.sonokai_style = "default"
        vim.g.sonokai_colors_override = {
            bg0 = { "#333333", "235" },
        }
        vim.cmd.colorscheme("sonokai")
    end,
}
