return {
    {
        -- Set lualine as statusline
        "nvim-lualine/lualine.nvim",
        -- See `:help lualine.txt`
        opts = {
            options = {
                theme = "tokyonight",
                icons_enabled = false,
                component_separators = "|",
                section_separators = "",
            },
        },
    },
}
