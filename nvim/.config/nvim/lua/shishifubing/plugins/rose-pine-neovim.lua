return {
    {
        "rose-pine/neovim",
        name = "rose-pine",
        enabled = false,
        lazy = false,
        priority = 1000,
        opts = {
            disable_background = true,
            dark_variant = "main",
        },
        config = function()
            vim.cmd.colorscheme("rose-pine")
        end,
    },
}
