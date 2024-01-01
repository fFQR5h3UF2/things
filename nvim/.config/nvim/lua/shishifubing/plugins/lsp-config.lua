return {

    {
        -- LSP Configuration & Plugins
        "neovim/nvim-lspconfig",
        dependencies = {
            -- Automatically install LSPs to stdpath for neovim
            { "williamboman/mason.nvim", config = true, opts = {} },
            { "williamboman/mason-lspconfig.nvim", opts = {} },

            -- Useful status updates for LSP
            -- NOTE: `opts = {}` is the same as calling `require('fidget').setup({})`
            { "j-hui/fidget.nvim", opts = {} },

            -- Additional lua configuration, makes nvim stuff amazing!
            { "folke/neodev.nvim", opts = {} },
        },
        opts = {
            servers = {
                yamlls = {
                    settings = {
                        yaml = {
                            customTags = {
                                "!reference sequence",
                            },
                        },
                    },
                },
            },
        },
    },
}
