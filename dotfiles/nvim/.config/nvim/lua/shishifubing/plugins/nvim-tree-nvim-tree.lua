return {
    "nvim-tree/nvim-tree.lua",
    version = "*",
    lazy = false,
    enabled = false,
    dependencies = {
        --{ "nvim-tree/nvim-web-devicons" },
    },
    config = function()
        local tree = require("nvim-tree")
        local api = require("nvim-tree.api")
        tree.setup({
            renderer = {
                icons = {
                    show = {
                        file = false,
                        folder = false,
                        folder_arrow = false,
                        git = true,
                        modified = true,
                        diagnostics = true,
                        bookmarks = true,
                    },
                },
            },
        })
        api.tree.open()
    end,
}
