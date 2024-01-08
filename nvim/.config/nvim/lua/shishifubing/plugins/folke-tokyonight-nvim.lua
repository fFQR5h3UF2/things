return {
    {
        "folke/tokyonight.nvim",
        lazy = false,
        priority = 1000,
        enabled = true,
        config = function()
            require("tokyonight").setup({
                style = "storm",
                on_colors = function(colors) end,
            })
            vim.cmd.colorscheme("tokyonight")
        end,
    },
}
