return {
    "nvim-treesitter/nvim-treesitter",
    dependencies = {
        "nvim-treesitter/nvim-treesitter-textobjects",
    },
    build = ":TSUpdate",
    opts = {
        ensure_installed = {
            "c",
            "cpp",
            "go",
            "lua",
            "python",
            "rust",
            "tsx",
            "javascript",
            "typescript",
            "vimdoc",
            "vim",
            "bash",
            "html",
            "yaml",
            "json",
            "toml",
            "css",
            "bash",
            "dockerfile",
            "gomod",
            "markdown",
            "gowork",
            "groovy",
            "kotlin",
        },
        auto_install = true,
        highlight = {
            enable = true,
            additional_vim_regex_highlighting = false,
        },
        indent = {
            enable = true,
        },
    },
    config = function(_, opts)
        local keymaps = require("shishifubing.keymaps").config_treesitter
        opts["incremental_selection"] = keymaps.incremental_selection
        opts["textobjects"] = keymaps.textobjects
        require("nvim-treesitter.configs").setup(opts)
    end,
}
